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

m1 = MyClass()
m2 = MyClass(1)
if id(m1) == id(m2):
    print("Son iguales")
else:
    print("Son diferentes")


# Crear la clase usando type() con valores por defecto en los parámetros
MC = type('MC', (object,), {
    '__init__': lambda self, v1=None, v2=None: (setattr(self, '__atributo1', v1), setattr(self, '__atributo2', v2)) or None,
    'atributo': 1,
    'funcion': lambda self: print(f'atributo1: {self.__atributo1} atributo2: {self.__atributo2}')
})

# Instanciar la clase pasando un valor solo para v1 (el valor de v2 será None por defecto)
obj1 = MC(None, None)
#obj1.funcion()  # Salida: atributo1: 100 atributo2: None

# Instanciar la clase pasando ambos valores para v1 y v2


