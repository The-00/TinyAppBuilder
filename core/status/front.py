import json
import tools.module_structure
import requests
from core.profiles.back import permission

class StatusFront(tools.module_structure.TABModuleFront):
    def __init__(self, app):
        super().__init__(app)
        self._add_route(route="/status", method="GET", callback=self._getStatus)

    @permission("show")
    def _getStatus(self):
        status_route = self._back._route_status()
        status_plugin = self._back._plugin_status()
        status_core = self._back._core_status()

        return f"""
<head><!--<meta http-equiv="refresh" content="5" >--></head>
<body>
    <h1>STATUS PAGE</h1>
    {status_route}
    <hr>
    {status_core}
    <hr>
    {status_plugin}

</body>
"""
