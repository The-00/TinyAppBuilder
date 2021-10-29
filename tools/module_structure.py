import json



class TABModule():    
    def __init__(self, app):
        self._app = app        
        self._route = ""
        self.__name__ = self.__module__

        
    def _add_route(self, route, method, callback):
        while len(route)>0 and route[-1] == "/": route = route[:-1]
        while len(route)>0 and route[0]  == "/": route = route[1:]
        self._app.route(f'{self._route}/{route}', method=method, callback=callback)

class TABModuleBack(TABModule):
    def __init__(self, app):
        super().__init__(app)
        self._route = "/api/" + "/".join(self.__module__.split("."))
        self._database = self._app._database
        self._default_route()


    def _default_route(self):
        # API SPECIAL
        self._add_route(route='config', method="POST", callback=self.config)
        self._add_route(route='status', method="POST", callback=self.status)
        self._add_route(route='permissions', method="POST", callback=self.permissions)

    def status(self):
        return json.dumps({})
    def config(self):
        return json.dumps({})
    def permissions(self):
        return json.dumps({"module": self.__module__, "permissions": [ r for r in self._app._rights if r.startswith(self.__module__)] })

class TABModuleFront(TABModule):
    def __init__(self, app):
        super().__init__(app)
        self._back = "/api/" + "/".join(self.__module__.split(".")[:-1]) + "/back"
