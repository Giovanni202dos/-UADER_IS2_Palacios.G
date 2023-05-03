from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
#Represente la lista de piezas componentes de un ensamblado con sus
#relaciones jerárquicas. Empiece con un producto principal formado por tres
#sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases
#que representen esa configuración y la muestren.
#Luego agregue un subconjunto opcional adicional también formado
#por cuatro piezas. (Use el patrón composite).

class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Pieza(Component):
    def operation(self) -> str:
        return "pieza node"


class Subconjunto(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
            #print('ff ',results)
        return f"Subconjunto({'+'.join(results)})"
        #return results


class ProductoPrincipal:
    def __init__(self, component: Component):
        self.component=component
    def agregar_canti_de_subconjunto_y_canti_de_piezas_por_branch(self, canti_branch,canti_hijos):    #que serian branch y hijos(leaf)
        for i in range(canti_branch):
            branch = Subconjunto()    #creamos el subconjunto (la rama)
            for i in range(canti_hijos):    #le agregamos las piezas (las hojas)
                branch.add(Pieza())

            self.component.add(branch)  #finalmente la agregamos al arbol

def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")

       
if __name__ == "__main__":

    print("\n")

    arbolsito = Subconjunto()
    configuracion_del_producto= ProductoPrincipal(arbolsito)
    print('agregamos 3 subconjutos con 4 Piezas cada uno')
    configuracion_del_producto.agregar_canti_de_subconjunto_y_canti_de_piezas_por_branch(3,4)
    client_code(arbolsito)
    print()
    print('agregamos un subconjuto mas con 4 Piezas')
    configuracion_del_producto.agregar_canti_de_subconjunto_y_canti_de_piezas_por_branch(1,4)
    client_code(arbolsito)
    print("\n")
