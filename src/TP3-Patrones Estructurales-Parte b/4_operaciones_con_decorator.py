
class Numero():  
    def operation(self) -> tuple:
        pass



class ConcreteNumero(Numero): #se le debe pasar un numero
    def __init__(self,num) -> None:
        self.num = num
    def operation(self) -> tuple:   #devuelve la operacion q se realiza
        return f"ConcreteNumero: {self.num}",self.num


        


class Decorator(Numero):
    _numero: Numero = None    

    def __init__(self, numero: Numero) -> None:
        self._numero = numero

    @property
    def numero(self) -> Numero:   #@property es un decorador, hace q cuando se llame al metodo no sea necesario usar los parentesis al final
        return self._numero

    def operation(self) -> tuple:
        return self._numero.operation()







class ConcreteDecoratorSumar2(Decorator):    #ConcreteDecoratorSumar2
    def operation(self) -> tuple:
        texto, num =self.numero.operation()
        return f"ConcreteDecoratorSumar2({texto})",num+2



class ConcreteDecoratorMulti2(Decorator):    #ConcreteDecoratorMulti2
    def operation(self) -> tuple:
        texto, num =self.numero.operation()
        return f"ConcreteDecoratorMulti2({texto})",num*2

class ConcreteDecoratorDiv3(Decorator):    #ConcreteDecoratorMulti2
    def operation(self) -> tuple:
        texto, num =self.numero.operation()
        return f"ConcreteDecoratorDiv3({texto})",num/3



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
    div3 = ConcreteDecoratorDiv3(multi2)
    print("Client: Now I've got a decorated component:")
    client_code(div3)

    print("\n")
   
