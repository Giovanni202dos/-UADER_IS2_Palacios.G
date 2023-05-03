"""
Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho
dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro
de 10 mts. Genere una clase que represente a las láminas en forma genérica al
cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el
patrón bridge en la solución).
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Lamina:  
    def __init__(self, implementation: Laminador) -> None:
        self.implementation = implementation
        
    def producir(self) -> str:
        pass


class ExtendedLaminas(Lamina):
    def __init__(self,espesor, ancho,implementation: Laminador) -> None:
        self.espesor= espesor
        self.ancho= ancho
        self.implementation=implementation  

    def producir(self) -> str:
        return (f"ExtendedLaminas: extenediendo la operation:\n"
                f"{self.implementation.producir_lamina(self.espesor,self.ancho)}")


class Laminador(ABC):  
    @abstractmethod
    def producir_lamina(self, espesor , ancho) -> str:
        pass

class Laminadores5mts(Laminador):  
    def producir_lamina(self, espesor , ancho) -> str:
        return f"Laminador5MTS produciendo una lamina de de un espesor: {espesor} y un ancho: {ancho}..."


class Laminadores10mts(Laminador): 
    def producir_lamina(self, espesor , ancho) -> str:
        return f"Laminador10MTS produciendo una lamina de de un espesor: {espesor} y un ancho: {ancho}..."
    
class LaminaAcero(Lamina):  
    def __init__(self, espesor,ancho, implementation: Laminador) -> None:
        self.espesor = espesor
        self.ancho = ancho
        self.implementation=implementation

    def producir(self) -> str:
        return (f"LaminaAcero: operation:\n"
                f"{self.implementation.producir_lamina(self.espesor,self.ancho)}")

def client_code(lamina: Lamina) -> None:
    print(lamina.producir())


if __name__ == "__main__":
    implementation = Laminadores5mts()  #se crea el laminador q se desea
    lamina_acero= LaminaAcero(1,5,implementation)   #se crea el tipo de lamina con su espesor y ancho y se le carga el laminador
    #abstraction = Lamina(implementation)   
    client_code(lamina_acero)   #se lo manda al cliente

    print("\n")

    implementation = Laminadores10mts()  
    abstraction = ExtendedLaminas(2,5,implementation)   
    client_code(abstraction)

    print("\n")
