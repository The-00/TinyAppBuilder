import tools.module_structure

class UserFront(tools.module_structure.TABModuleFront):
    def __init__(self, app):
        super().__init__(app)
        self._add_route(route="/users",method="GET", callback=self._configProfiles)

    def _configProfiles(self):
        return "<h1>Config Users</h1>"
