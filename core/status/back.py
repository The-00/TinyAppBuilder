import tools.module_structure
import json

class StatusBack(tools.module_structure.TABModuleBack):
    def __init__(self, app):
        super().__init__(app)
        self._add_route("plugin", "POST", self._plugin_status)
        self._add_route("route",  "POST", self._route_status )

    def _plugin_status(self):
        status_plugins = [(pl.__name__, json.loads(pl.status())) for pl in self._app._plugins]
        
        tableHead=[e[0] for e in status_plugins]
        tableContent=[[e[1][k] for k in e[1]] for e in status_plugins]
        
        return json.dumps({"table":{"head":tableHead, "content":tableContent}})

    def _route_status(self):
        tableHead    = ["method", "rule", "source"]
        tableContent = [[e.method, e.rule, e.callback.__self__.__class__.__module__] for e in self._app.routes]
        
        return json.dumps({"table":{"head":tableHead, "content":tableContent}})