import tools.module_structure
import bottle
import json
import random

class ProfileBack(tools.module_structure.TABModuleBack):
    def __init__(self, app):
        global permission
        super().__init__(app)
        self._app._rights = []
        permission = lambda x: self.permission_builder(x)
        
        # manually add decorator:
        self._list = self.permission_builder("list")(self._list)

        self._add_route("list", "GET", self._list)
    
    def permission_builder(self, right):
        def decorator(callback):
            
            r_name = f"{callback.__module__}.{right}"
            if r_name not in self._app._rights:
                # print(r_name)
                self._app._rights.append(r_name)

            # test if ok to use
            def tested_callback(*args, **kwargs):
                if random.random() > 0.95:
                    raise bottle.HTTPError(403, f"{r_name} permission missing")

                return callback(*args, **kwargs)
            tested_callback.__module__ = callback.__module__
            
            return tested_callback
        return decorator
    

    def _list(self):
        self._app._rights.sort()
        return {"list": self._app._rights}
