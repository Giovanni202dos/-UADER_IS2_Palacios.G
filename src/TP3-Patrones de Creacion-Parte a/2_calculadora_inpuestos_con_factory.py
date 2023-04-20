
from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC): #clase abstract que deriva de la clase ABC(Abstract Base Class) definida en python...es una plantilla para crear clases abstractas
    @abstractmethod
    def calcular_impuestos(self):
        pass
    def some_operation(self,base_imponible) -> str:
        # calculamos el impuesto
        impuesto = self.calcular_impuestos(base_imponible)
        # lo mostramos
        result = f"el impuesto es: {impuesto}\n"
        return result



class CalculadoraImpuestosSimplificada(Creator):
    def calcular_impuestos(self, base_imponible) -> float:
        total_impuestos= 0
        total_impuestos+=base_imponible* 0.21   #IVA
        total_impuestos+=base_imponible* 0.05   #iibb
        total_impuestos+=base_imponible* 0.012  #contrib_municipales
        return total_impuestos

class CalculadoraImpuestosCompuesta(Creator):
    def calcular_impuestos(self, base_imponible) -> float:
        total_impuestos= 0
        total_impuestos+=base_imponible* 0.05   #iibb
        total_impuestos+=base_imponible* 0.020  #contrib_municipales
        return total_impuestos


#metodo intermediario
def client_code(creator: Creator) -> None:
    base_imponible=345
    print(f"Yo soy un mero intermediario tipo FACTORY que no se que es lo que estoy creando, pero lo creo.\n"
          f"{creator.some_operation(base_imponible)}", end="")

#PROGRAMA
if __name__ == "__main__":

    print("\n\n")
    print("App: Creando una calculadora")
    client_code(CalculadoraImpuestosSimplificada())
    print("\n")


