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
        self._default_route()


    def _default_route(self):
        # API SPECIAL
        self._add_route(route='config', method="POST", callback=self.config)
        self._add_route(route='status', method="POST", callback=self.status)
        self._add_route(route='rights', method="POST", callback=self.rights)

    def status(self):
        return json.dumps({})
    def config(self):
        return json.dumps({})
    def rights(self):
        return json.dumps({})

class TABModuleFront(TABModule):
    def __init__(self, app):
        super().__init__(app)
        self._back = "/api/" + "/".join(self.__module__.split(".")[:-1]) + "/back"
