"""
Clase ABTRACTA que obtiene el valor de una clave
"""
from abc import ABC,abstractmethod
class AbractClaveBanco(ABC):
    """
    Clase que ABTRACTA
    """
    @abstractmethod
    def getvalor(self,clave):
        """
        retorna el valor de un clave del JSON proporcionado
        """
