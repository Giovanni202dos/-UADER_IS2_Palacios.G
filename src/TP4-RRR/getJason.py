"""
Título: Extractor de token
Autor: Desconocido-modificado
Fecha: 2023-06-16
Descripción: Extrae una valor pasandole un token(clave), sacandolo del JSON proporsionado
Copyright IS2 © 2022,2023 todos los derechos reservados.
"""
import json
import sys
import datetime
from abtraction_clave_banco  import AbractClaveBanco
from cadena_cuentas import Cuenta
from iterator import WordsCollection
class SingletonMeta(type,AbractClaveBanco):  #aca coordina que solo haya una sola instancia
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

    def getvalor(self,clave):
        pass

class ClaveBanco(metaclass=SingletonMeta):
    """
    Clase que obtiene el valor de una clave utilizando el patrón Singleton y utilizando metaclass
    """
    def getvalor(self,clave):
        """
        retorna el valor de un clave del JSON proporcionado
        """
        with open('sitedata.json', 'r', encoding='utf-8') as (myfile):
            data = myfile.read()
        obj = json.loads(data)
        try:
            return str(obj[clave])
        except KeyError:
            print(f'{clave} no encontrado')
            return None

class ServicioPago:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.todos_los_pagos = WordsCollection()

    def realizar_pago(self, numero_pedido, token, monto):
        CLAVE_API = ClaveBanco().getvalor(token)
        #print(CLAVE_API)
        if CLAVE_API !=None:    #si el token esta en el JSON
            #print('yesss')
            resultado = self.cuentas.handle(CLAVE_API, monto)  #buscamos la cuenta y efectuamos el pago
            #print(resultado)
            if resultado == True:#es porque se efectuo el pago, entonces creamos un recivo y lo guardamos
                self.todos_los_pagos.add_item(Recivo(numero_pedido,token,monto,True)) #guardamos el recivo
            else:
                print('no hay suficiente dinero')
                self.todos_los_pagos.add_item(Recivo(numero_pedido,token,monto,False)) #guardamos el recivo

    def get_todos_los_pagos_por_orden_de_llegada(self): #desde el mas antiguo(o primero en llegar) hasta el mas reciente
        for recivo in self.todos_los_pagos:
            print(recivo)

    def get_todos_los_pagos_efectuados_por_orden_de_llegada(self): #desde el mas antiguo(o primero en llegar) hasta el mas reciente
        for recivo in self.todos_los_pagos:
            if recivo.pagado:
                print(recivo)

    def get_todos_los_pagos_sin_efectuar_por_orden_de_llegada(self): #desde el mas antiguo(o primero en llegar) hasta el mas reciente
        for recivo in self.todos_los_pagos:
            if recivo.pagado ==False:
                print(recivo)

class Recivo:
    def __init__(self,numero_pedido, token,monto,pagado) -> None:
        self.numero_pedido = numero_pedido
        self.token = token
        self.monto = monto
        self.fecha_hora_actual = datetime.datetime.now()
        self.pagado = pagado

    def __str__(self) -> str:
        return f'hora-fecha: {self.fecha_hora_actual}\n numero de pedido: {self.numero_pedido}\n token: {self.token}\n monto: {self.monto}\n pagado: {self.pagado}\n'
        

if __name__ == "__main__":
    cuenta1 = Cuenta(1000,'C598-ECF9-F0F7-881A')
    cuenta2 = Cuenta(2000,'C598-ECF9-F0F7-881B')
    cuenta1.set_next(cuenta2)

    servicio =ServicioPago(cuentas=cuenta1)
    servicio.realizar_pago(1234,'token1',500)
    servicio.realizar_pago(1234567,'token2',600)
    servicio.realizar_pago(111111,'token1',1000)

    print('TODOS LOS INTENTO DE PAGOS EN ORDEN CRONOLOGICO:')
    servicio.get_todos_los_pagos_por_orden_de_llegada()
    print()
    print('PAGOS REALIZADOS(EFECTUADO CON EXITO) POR ORDEN CRONOLOGICO:')
    servicio.get_todos_los_pagos_efectuados_por_orden_de_llegada()
    print()
    print('PAGOS SIN EFECTUAR POR ORDEN CRONOLOGICO:')
    servicio.get_todos_los_pagos_sin_efectuar_por_orden_de_llegada()

