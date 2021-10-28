import tools.module_structure
import os
import bottle
import json

class ShellBack(tools.module_structure.TABModuleBack):
    def __init__(self, app):
        super().__init__(app)
        self._add_route("execute/<user>", "POST", self._execute)
        self._add_route("execute", "POST", self._execute)
        self.history = []
        
    def _execute(self, user=None):
        request_parameters = json.load(bottle.request.body)
        
        if user is None and "user" in request_parameters:
            user = request_parameters["user"]
        elif user is None:
            return json.dumps({"state":"not ok","result":"no user provided"})
        
        if "command" in request_parameters:
            return json.dumps( self.__execute_command(user, request_parameters["command"]))
        else:
            return json.dumps({"state":"not ok","result":"no command provided"})

    def __execute_command(self, user, command):
        if user != "root": command = f'su {user} -s "/bin/sh" -c "{command}"'
        result = os.popen(command).read()
        self.history.append( {"user": user, "command": command, "result": result} )
        return {"state":"ok","result":result}

    def status(self):
        return json.dumps({"state":"Loaded", "history": self.history})
    
    def rights(self):
        rights = ["shell._execute_root", "shell._execute"]
        return json.dumps(rights)