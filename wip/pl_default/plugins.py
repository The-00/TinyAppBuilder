import json

class default():
    def __init__(self, app):
        # verify installation
        self._app = app
        self._route()
        self._installation()
        pass

    def _installation(self):
        # execute database insert
        pass

    def _route(self):
        # FRONT
        self._app.route('/default', method="GET", callback=self._default)
        # API SPECIAL
        self._app.route('/api/default/config', method="POST", callback=self.config)
        self._app.route('/api/default/status', method="GET",  callback=self.status)
        self._app.route('/api/default/rights', method="GET",  callback=self.rights)
        # API
        self._app.route('/api/default', method="POST", callback=self._defaultDefault)
        

    def status(self):
        return json.dumps({})
    def config(self):
        return ""
    def rights(self):
        return ""
    
    def _defaultDefault(self):
        return ""

    def _default(self):
        return '<h1>get Default Plugin</h1>'



