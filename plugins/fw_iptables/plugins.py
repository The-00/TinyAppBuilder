import json

class Iptables():
    def __init__(self, app):
        # verify installation
        self._app = app
        self._route()
        pass

    def installation(self):
        # execute database insert
        pass

    def _route(self):
        self._app.route('/api/tables', method="GET", callback=self._getTables)
        
        self._app.route('/api/iptables/config', method="POST", callback=self.config)
        self._app.route('/api/iptables/status', method="GET",  callback=self.status)
        self._app.route('/api/iptables/rights', method="GET",  callback=self.rights)

    def _getTables(self):
        return '<h1>test</h1>'


    def status(self):
        return json.dumps({})
    def config(self):
        return ""
    def rights(self):
        return ""
