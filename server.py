from bottle import Bottle
from tools import load
import sys


app = Bottle()

# setting path
sys.path.append('.')

# import core and plugins
_,_,app._core = load.core(app)
_,_,app._plugins =  load.plugins(app)

app.run(host='localhost', port=80)
