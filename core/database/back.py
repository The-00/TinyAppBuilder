import tools.module_structure
import bottle
import sqlite3 as lite
from core.profiles.back import permission

class DatabaseBack(tools.module_structure.TABModuleBack):
    def __init__(self, app):
        super().__init__(app)
        self.database = "res/database.db"
        self._app._database = self._route
        self._add_route("sql", "POST", self._execute)
    
    @permission("execute")
    def _execute(self):
        body = json.load(bottle.request.body)
        if "request" not in body:
            return {"state":"error", "result":"no request privided"}
                    
        sql   = body["request"]
        value = body["value"] if "value" in body else None
        
        con = None
        try:
            con = lite.connect(self.database)
            cur = con.cursor()  
            if value:
                cur.execute(sql, value)
            else:
                cur.execute(sql)
            con.commit()
            data = cur.fetchall()
        except lite.Error as e:   
            error = e.args[0]
            return {"state":"error", "result":error}
        finally:
            if con:
                con.close()
        return {"state":"ok", "result":data}
