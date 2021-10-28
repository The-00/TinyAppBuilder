import json
import tools.module_structure
import requests

class StatusFront(tools.module_structure.TABModuleFront):
    def __init__(self, app):
        super().__init__(app)
        self._add_route(route="/status", method="GET", callback=self._getStatus)

    def _getStatus(self):
        status_route  = requests.post(f"http://{self._app._host}{self._back}/route").json()["response"]
        status_plugin = requests.post(f"http://{self._app._host}{self._back}/plugin").json()["response"]
        status_core   = requests.post(f"http://{self._app._host}{self._back}/core").json()["response"]

        status_route_html  = status_route
        status_plugin_html = status_plugin
        status_core_html = status_core

        return f"""
<head><!--<meta http-equiv="refresh" content="5" >--></head>
<body>
    <h1>STATUS PAGE</h1>
    {status_route_html}
    <hr>
    {status_core_html}
    <hr>
    {status_plugin_html}

</body>
"""
