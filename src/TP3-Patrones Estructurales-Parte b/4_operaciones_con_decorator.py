
class Numero():  
    def operation(self) -> str:
        pass



class ConcreteNumero(Numero): #se le debe pasar un numero
    def __init__(self,num) -> None:
        self.num = num
    def operation(self) -> str:   #devuelve la operacion q se realiza
        return f"ConcreteNumero: {self.num}"

        


class Decorator(Numero):
    _numero: Numero = None    

    def __init__(self, numero: Numero) -> None:
        self._numero = numero

    @property
    def numero(self) -> Numero:   #@property es un decorador, hace q cuando se llame al metodo no sea necesario usar los parentesis al final
        return self._numero

    def operation(self) -> str:
        return self._numero.operation()






class ConcreteDecoratorSumar2(Decorator):    #ConcreteDecoratorSumar2
    def operation(self) -> str:
        return f"ConcreteDecoratorSumar2({self.numero.operation()})"



class ConcreteDecoratorMulti2(Decorator):    #ConcreteDecoratorMulti2
    def operation(self) -> str:
        return f"ConcreteDecoratorMulti2({self.numero.operation()})"



def client_code(component: Numero) -> None:
    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...


if __name__ == "__main__":

    # This way the client code can support both simple components...

    simple = ConcreteNumero(4)
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.

    sumar2 = ConcreteDecoratorSumar2(simple)
    multi2 = ConcreteDecoratorMulti2(sumar2)

    print("Client: Now I've got a decorated component:")
    client_code(multi2)

    print("\n")
   
