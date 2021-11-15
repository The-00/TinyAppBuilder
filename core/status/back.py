import tools.module_structure
from core.profiles.back import permission

class StatusBack(tools.module_structure.TABModuleBack):
    def __init__(self, app):
        super().__init__(app)
        self._add_route("plugin", "GET", self._plugin_status)
        self._add_route("core",   "GET", self._core_status  )
        self._add_route("route",  "GET", self._route_status )

    @permission("list.plugins")
    def _plugin_status(self):
        status_plugins = [
            (pl.__name__, pl.status())
            for pl in self._app._plugins if isinstance(pl, tools.module_structure.TABModuleBack)
        ]
        
        response = {
            "response": [
                {
                    "plugin_name": p[0],
                    "plugin_status": p[1]
                }
                for p in status_plugins
            ]
        }
        
        return response
    
    @permission("list.core")
    def _core_status(self):
        status_core = [
            (pl.__name__, pl.status())
            for pl in self._app._cores if isinstance(pl, tools.module_structure.TABModuleBack)
        ]
        
        response = {
            "response": [
                {
                    "core_name": c[0],
                    "core_status": c[1]
                }
                for c in status_core
            ]
        }
        
        return response

    @permission("list.route")
    def _route_status(self):
        response = {
            "response": [
                {
                    "route_method"  : r.method,
                    "route_rule"    : r.rule
                }
                for r in self._app.routes
            ]
        }
        
        return response
    
    def status(self):
        return {"state":"Loaded", "test":"test"}