import tools.module_structure
import json

class StatusBack(tools.module_structure.TABModuleBack):
    def __init__(self, app):
        super().__init__(app)
        self._add_route("plugin", "POST", self._plugin_status)
        self._add_route("core",   "POST", self._core_status  )
        self._add_route("route",  "POST", self._route_status )

    def _plugin_status(self):
        status_plugins = [
            (pl.__name__, json.loads(pl.status()))
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
        
        return json.dumps(response)
    
    def _core_status(self):
        status_core = [
            (pl.__name__, json.loads(pl.status()))
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
        
        return json.dumps(response)

    def _route_status(self):
        response = {
            "response": [
                {
                    "route_method"  : r.method,
                    "route_rule"    : r.rule,
                    "route_module"  : r.callback.__self__.__class__.__module__
                }
                for r in self._app.routes
            ]
        }
        
        return json.dumps(response)
    
    def status(self):
        return json.dumps({"state":"Loaded", "test":"test"})