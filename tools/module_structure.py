
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
        return {}
    def config(self):
        return {}
    def permissions(self):
        return {"module": self.__module__, "permissions": [ r for r in self._app._rights if r.startswith(self.__module__)] }

class TABModuleFront(TABModule):
    def __init__(self, app):
        super().__init__(app)
        
        back_module_name = ".".join(self.__module__.split('.')[:-1]) + ".back"
        back_module_type = self.__module__.split('.')[0]
        list_modules = app._cores if back_module_type == "core" else app._plugins
        self._back = None
        for m in list_modules:
            if m.__name__ == back_module_name:
                self._back = m
                
        self._back_route = "/api/" + "/".join(self.__module__.split(".")[:-1]) + "/back"
