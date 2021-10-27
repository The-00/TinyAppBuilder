import tools.database
import tools.module_structure

class ProfileFront(tools.module_structure.TABModule):
    def __init__(self, app):
        super().__init__(app)
        self._route()

    def _route(self):
        # front
        self._app.route('/config/profiles', method="GET", callback=self._configProfiles)

    def _configProfiles(self):
        return "<h1>configProfiles</h1>"
