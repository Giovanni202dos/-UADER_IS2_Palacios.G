from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request,monto) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler

        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any,monto) -> str:  #se encarga de pasarle al que le sigue(si existe uno)
        if self._next_handler:  #verifica si hay uno guardado
            return self._next_handler.handle(request,monto)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""

class Cuenta(AbstractHandler):
    def __init__(self, saldo_inicial,nombre):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def handle(self, request: Any, monto) -> str:  #verifica si el resquest es para el sino lo es lo pasa al super
        if request == self.nombre:
            #print(f"yess es mi banco {request}, mi saldo es:{self.saldo}")
            return self.hacer_pago(monto)
        else:   #si no quiere lo q se le esta dando se lo pasa al siguiente
            return super().handle(request, monto)

    def hacer_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False


if __name__ == "__main__":
    pass
    #cuenta1 = Cuenta(1000,'C598-ECF9-F0F7-881A')
    #cuenta2 = Cuenta(2000,'C598-ECF9-F0F7-881B')

    #cuenta1.set_next(cuenta2)

    #print(cuenta1.handle('C598-ECF9-F0F7-881A'))
