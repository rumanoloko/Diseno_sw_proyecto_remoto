class MetaSingleton(type):
    _instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = type.__call__( cls, *args, **kwargs)
        return cls._instances

class MyClass(metaclass=MetaSingleton):
    def __init__(self, v1=None, v2=None):
        self.a = v1
        self.b = v2


