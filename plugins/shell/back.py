import tools.module_structure
import os
import bottle
import json

class ShellBack(tools.module_structure.TABModuleBack):
    def __init__(self, app):
        super().__init__(app)
        self._add_route("execute", "POST", self._execute)
        self.history = []
        
    def _execute(self):
        request_parameters = json.load(bottle.request.body)
        if "command" in request_parameters:
            command = request_parameters["command"]
            result = os.popen(command).read()
            self.history.append( {"command": command, "result": result} )
            return json.dumps({"state":"ok","result":result})
        else:
            return json.dumps({"state":"not ok","result":"no command provided"})

    def status(self):
        return json.dumps({"state":"Loaded", "history": self.history})
    
    def rights(self):
        rights = ["shell.execute"]
        return json.dumps(rights)