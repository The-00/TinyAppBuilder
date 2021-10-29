import tools.module_structure
import bottle
import json

class ProfileBack(tools.module_structure.TABModuleBack):
    def __init__(self, app):
        global permission
        super().__init__(app)
        self._app._rights = []
        permission = self.permission
        
        self._add_route("list", "GET", self._list)
    
    def _list(self):
        return json.dumps(self._app._rights)
    
    def permission(self, rights):
        def decorator(callback):
            
            for r in rights:
                r_name = f"{callback.__module__}.{r}"
                if r_name not in self._app._rights:
                    self._app._rights.append(r_name)
                    
            
            # test if ok to use
            
            return callback
        return decorator
