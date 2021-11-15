from bottle import Bottle
from tools import load
import sys

app = Bottle()

# setting path
sys.path.append('.')

# import core and plugins
app._database= ""
app._core = []
app._plugins = []
core_package,core_module,core_class       = load.core(app)
plugin_package,plugin_module,plugin_class = load.plugins(app)

app._host    = "localhost"
#app._cores   = core_class
app._plugins = plugin_class


app.run(host=app._host, port=80, server='paste', reloader=True)
