from os import environ
from sys import platform as _sys_platform
from functools import wraps

def getplatform():
    kivy_build = environ.get('KIVY_BUILD', '')
    if kivy_build in {'android', 'ios'}:
        return kivy_build
    elif 'P4A_BOOTSTRAP' in environ:
        return 'android'
    elif 'ANDROID_ARGUMENT' in environ:
        return 'android'
    elif _sys_platform in ('win32', 'cygwin'):
        return 'win'
    elif _sys_platform == 'darwin':
        return 'macosx'
    elif _sys_platform.startswith('linux'):
        return 'linux'
    elif _sys_platform.startswith('freebsd'):
        return 'linux'
    return 'unknown'

platform = getplatform()

class Platform:

    @classmethod
    def is_android(cls) -> bool:
        return platform == "android"

    @classmethod
    def is_linux(cls) -> bool:
        return platform == "linux"

    @classmethod
    def android(cls, func):
        @wraps(func)
        def callback(*args, **kwargs):
            if Platform.is_android():
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    return False
            else:
                print("METHOD ONLY FOR ANDROID PLATFORM")
                return False
        return callback