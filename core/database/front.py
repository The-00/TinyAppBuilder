import tools.module_structure

class DatabaseFront(tools.module_structure.TABModuleFront):
    def __init__(self, app):
        super().__init__(app)
        self._add_route(route="/database",method="GET", callback=self._configProfiles)

    def _configProfiles(self):
        return "<h1>Config Database</h1>"
