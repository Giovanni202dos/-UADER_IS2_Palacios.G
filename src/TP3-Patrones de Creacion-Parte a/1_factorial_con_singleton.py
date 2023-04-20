class SingletonMeta(type):  #aca coordina que solo haya una sola instancia
    """
    clase SingletonMeta
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Factorial(metaclass=SingletonMeta): 
    """
    Clase que calcula el factorial de un número utilizando el patrón Singleton y utilizando metaclass
    """

    def __init__(self):
        pass

    def getFactorial(self, n):  # de manera recursiva
        """
        Calcula el factorial de un número
        """
        if n == 0:
            return 1
        else:
            resultado = n * self.getFactorial(n-1)
            return resultado





if __name__ == "__main__":
    # The client code.

    s1 = Factorial()    #creamos dos instancias
    s2 = Factorial()

    if id(s1) == id(s2):    #verificamos que sean las mismas
        print("son las mismas instancias.")
        print(s1.getFactorial(12))
        print(s2.getFactorial(2))
    else:
        print("son diferentes")



