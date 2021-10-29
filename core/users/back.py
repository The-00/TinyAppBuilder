import tools.module_structure
import requests
import bottle
import bcrypt
import json

class UserBack(tools.module_structure.TABModuleBack):
    def __init__(self, app):
        super().__init__(app)
        self._add_route("get", "POST", self._users)
        self._add_route("add", "POST", self._add)
        self._add_route("install", "POST", self._installation)

    def _installation(self):
        res = requests.post(f"http://{self._app._host}{self._database}/sql",
                      json={"request": '''CREATE TABLE IF NOT EXISTS users (
                          id integer PRIMARY KEY,
                          name text NOT NULL,
                          password text NOT NULL,
                          role_id integer)'''
                          # FOREIGN KEY (role_id) REFERENCES roles (id))'''
                                }
                      )
        return res
                        
    def _add(self):
        body = json.load(bottle.request.body)
        if "user" not in body:
            return {"state":"not ok", "result":"no user provided"}
        if "password" not in body:
            return {"state":"not ok", "result":"no password provided"}
        if len(body["password"]) < 3:
            return {"state":"not ok", "result":"password too short"}
        
        user = body["user"]
        password = bcrypt.hashpw(body["password"].encode('utf-8'), bcrypt.gensalt())
        
        res = requests.post(f"http://{self._app._host}{self._database}/sql",
                      json={"request": f'INSERT INTO users(name,password,role_id) VALUES(?,?,?)',
                            "value"  : [user, password, 0]
                          }
                      )
        return res
    
    def _users(self):
        users = requests.post(f"http://{self._app._host}{self._database}/sql",
                      json={"request": "SELECT * FROM users"}
                      ).json()
        return users