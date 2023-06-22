import sys
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
    if len(sys.argv)>1:
            s1 = Factorial()
            num = int(sys.argv[1])
            print(s1.getFactorial(num))
    else:
        print('no has ingresado argumentos')



