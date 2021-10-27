import json
import tools.module_structure

class Status(tools.module_structure.TABModule):
    def __init__(self, app):
        super().__init__(app)
        self._route()

    def _route(self):
        self._app.route('/', method="GET", callback=self._getStatus)

    def _getStatus(self):

        plugins = self._app._plugins
        status_plugins = [(pl.__name__, json.loads(pl.status())) for pl in plugins]
        status_plugins_html = ""
        for pl in status_plugins:
            status_plugins_html += f"<table><tr><th>{pl[0]}</th></tr><tr><table>"
            for k in pl[1]:
                status_plugins_html += f"<tr><td>{k}</td><td>{pl[1][k]}</td></tr>"
            status_plugins_html += "</table></tr></table><br>"

        listRoutes = "<table><tr><th>method</th><th>rule</th><th>source</th></tr>" + "".join([ f"<tr><td>{r.method}</td><td>{r.rule}</td><td>{r.callback.__self__.__class__.__module__}</td></tr>"  for r in self._app.routes]) + "</table>"


        return f"""
<head><!--<meta http-equiv="refresh" content="5" >--></head>
<body>
    <h1>STATUS PAGE</h1>
    {listRoutes}
    <br><br>
    {status_plugins_html}

</body>
"""
