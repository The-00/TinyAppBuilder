import importlib
import inspect
import os

def core(app):
    packages = [ importlib.import_module('core') ]
    modules = []
    app._cores = []
    for module_name in ["profiles", "users", "database", "status", "plugin_manager"]:
        try:
            package = importlib.import_module(f"core.{module_name}", package="core")
            packages.append( package )
            for type_module in ["back", "front"]:
                try:
                    module = importlib.import_module(f"core.{module_name}.{type_module}", package="core")
                    modules.append( module )
                        
                    for x in dir(module):
                        obj = getattr(module, x)
                        if inspect.isclass(obj):
                            print( "loading core:", obj )
                            app._cores.append( obj(app) )
                except Exception as e:
                    print(e)                    
        except Exception as e:
            print(e)

    return packages, modules, app._cores

def plugins(app):
    packages = [ importlib.import_module('plugins') ]
    modules = []
    for module_name in os.listdir('plugins'):
        try:
            package = importlib.import_module(f"plugins.{module_name}", package="plugins")
            packages.append( package )
            for type_module in ["back", "front"]:
                try:
                    module = importlib.import_module(f"plugins.{module_name}.{type_module}", package="plugins")
                    modules.append( module )
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

    plugins = []
    for module in modules:
        for x in dir(module):
            obj = getattr(module, x)
            if inspect.isclass(obj):
                print( "loading plugin:", module.__name__ + "." + x )
                plugins.append( obj(app) )
                plugins[-1].__name__ = module.__name__ + "." + x

    return packages, modules, plugins
