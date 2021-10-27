import json
import tools.status


class TABModule():
    def __init__(self, app):
        self._app = app
        self._api_route = "/".join(self.__module__.split("."))
        self._default_route()

    def _default_route(self):
        # API SPECIAL
        self._app.route(f'/api/{self._api_route}/config', method="POST", callback=self.config)
        self._app.route(f'/api/{self._api_route}/status', method="GET",  callback=self.status)
        self._app.route(f'/api/{self._api_route}/rights', method="GET",  callback=self.rights)

    def status(self):
        return json.dumps({})
    def config(self):
        return json.dumps({})
    def rights(self):
        return json.dumps({})
