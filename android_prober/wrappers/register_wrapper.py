from functools import wraps, partial
from typing import Any, Union
from swagger_gen.lib.wrappers import swagger_metadata
from android_prober.app import AndroidProber

"""
These methods are using for achiving the same functionality as JSONRPC

NEED's to WORK AROUND
====================
* handle all the exception cases
    * reference same as expressjs

"""

def include_apis(cls):
    for key, value in vars(cls).items():
        if callable(value) and not (key.startswith("__") or key.endswith("__")):
            if not key.startswith("_") and key in dir(cls):
                response = value()
                setattr(cls, key, response)
    return cls

def get(func = None, handler_name: str = '', **kwgs):

    if func is None:
        return partial(get, handler_name = handler_name, **kwgs)

    @wraps(func)
    def get_callback(*args, **kwargs):
        """
        Please pass the very first as instance of the class
        """
        nonlocal handler_name
        class_name = func.__qualname__.split(".")
        
        if any(class_name):
            class_name = class_name[0].lower()
        
        if handler_name:
            pass
        else:
            handler_name = func.__name__

        if len(args):
            callback = partial(func, args[0])

        callback.__name__ = handler_name
        if class_name:
            view_function = AndroidProber.app.get(f"/{class_name}/{callback.__name__}")
        else:
            view_function = AndroidProber.app.get(f"/{callback.__name__}")
        
        fn = view_function(callback)
        swagger_metadata(**kwgs)(callback)
        return fn

    return get_callback

def post(func = None, handler_name: str = '', **kwgs):
    if func is None:
        return partial(post, handler_name = handler_name ,**kwgs)

    @wraps(func)
    def post_callback(*args, **kwargs):
        callback = None
        """
        Please pass the very first as instance of the class
        """
        nonlocal handler_name
        class_name = func.__qualname__.split(".")
        
        if any(class_name):
            class_name = class_name[0].lower()
        
        if handler_name:
            pass
        else:
            handler_name = func.__name__
        if len(args):
            callback = partial(func, args[0])
        
        callback.__name__ = handler_name
        if class_name:
            view_function = AndroidProber.app.post(f"/{class_name}/{callback.__name__}")
        else: 
            view_function = AndroidProber.app.post(f"/{callback.__name__}")

        fn = view_function(callback)
        swagger_metadata(**kwgs)(callback)
        return fn

    return post_callback

def error_handler(func = None, exec: Union[int, Exception] = 404):
    if func is None:
        return partial(error_handler, func = func, exec = exec)
    AndroidProber.app.errorhandler(exec)(func)
    return func

# just make the visibleity for flask app
def expose_api(class_instance : Union[Any, None] = None):
    for key , fn in vars(class_instance).items():
        if callable(fn) and "__" not in key :
            fn()

# which will use of JSONRPC
def register(route_handler, rpc_app = None, handler_name:str = ""):
    if route_handler is None:
        return partial(register, rpc_app, route_handler, handler_name)

    @wraps(route_handler)
    def callback(*args, **kwargs):
        if not handler_name:
            handler_name = route_handler.__name__
            if rpc_app is not None:
                rpc_app.register(route_handler, handler_name)
            else:
                AndroidProber.app.register(route_handler, handler_name)
            response = route_handler(*args, **kwargs)
        return response

    return callback

