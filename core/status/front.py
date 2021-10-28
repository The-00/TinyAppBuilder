import json
import tools.module_structure
import tools.style
import requests

class StatusFront(tools.module_structure.TABModuleFront):
    def __init__(self, app):
        super().__init__(app)
        self._add_route(route="/", method="GET", callback=self._getStatus)

    def _getStatus(self):
        status_route  = requests.post(f"http://{self._app._host}{self._back}/route").json()["table"]
        status_plugin = requests.post(f"http://{self._app._host}{self._back}/plugin").json()["table"]

        status_route_html  = tools.style.html_table(tableHead=status_route["head"],  tableContent=status_route["content"] )
        status_plugin_html = tools.style.html_table(tableHead=status_plugin["head"], tableContent=status_plugin["content"])

        return f"""
<head><!--<meta http-equiv="refresh" content="5" >--></head>
<body>
    <h1>STATUS PAGE</h1>
    {status_route_html}
    <br><br>
    {status_plugin_html}

</body>
"""
