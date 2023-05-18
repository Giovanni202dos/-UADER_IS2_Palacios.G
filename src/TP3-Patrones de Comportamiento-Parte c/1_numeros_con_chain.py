from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler

        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:  #se encarga de pasarle al que le sigue(si existe uno)
        if self._next_handler:  #verifica si hay uno guardado
            return self._next_handler.handle(request)

        return None


class NumerosPrimos(AbstractHandler):   #primo
    def handle(self, request: Any) -> str:  #verifica si el resquest es para el sino lo es lo pasa al super
        resultado=""
        if self.es_primo(request):
            resultado+="ES PRIMO\n"  #por si es ambas a la vez
        
        return resultado+super().handle(request) if super().handle(request)!=None else resultado    #lo va a concatenar si es diferente de None
    def es_primo(self, n) -> bool:
        """
        Verifica si un número es primo o no.
        Devuelve True si el número es primo, False si no lo es.
        """
        if n < 2:  # 0 y 1 no son números primos
            return False
        for i in range(2, int(n**0.5) + 1):  # Verificar divisibilidad hasta la raíz cuadrada de n
            if n % i == 0:
                return False
        return True


class NumerosPares(AbstractHandler): #Pares
    def handle(self, request: Any) -> str:
        resultado=""
        if self.es_par(request):
            resultado+="ES PAR\n"  #por si es ambas a la vez
        
        return resultado+super().handle(request) if super().handle(request)!=None else resultado    #lo va a concatenar si es diferente de None
    def es_par(self, n) -> bool:
        """
        Verifica si un número es par o no.
        Devuelve True si el número es par, False si no lo es.
        """
        if n % 2 == 0:
            return True
        else:
            return False



def client_code(handler: Handler) -> None:

    for numero in range(1,101):
        print(f"\n el {numero} es primo o par??")
        result = handler.handle(numero)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"    NO CONSUMIDO(no es niguno de los dos).", end="")


if __name__ == "__main__":

    primos = NumerosPrimos()
    par = NumerosPares()
    
    primos.set_next(par)



    print("Chain: primos > par\n")
    client_code(primos)
    print("\n")




