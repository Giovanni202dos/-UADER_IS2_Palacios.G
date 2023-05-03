"""
Provea una clase ping que luego de creada al ser invocada con un método
“execute(string)” realice 10 intentos de ping a la dirección IP contenida en
“string” (argumento pasado), la clase solo debe funcionar si la dirección IP
provista comienza con “192.”. Provea un método executefree(string) que haga
lo mismo pero sin el control de dirección. Ahora provea una clase pingproxy
cuyo método execute(string) si la dirección es “192.168.0.254” realice un ping a
www.google.com usando el método executefree de ping y re-envie a execute
de la clase ping en cualquier otro caso. (Modele la solución como un patrón
proxy).
"""

from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
    @abstractmethod
    def check_access(self,ip) -> bool:
        pass
    @abstractmethod
    def executefree(self,ip) -> None:
        pass

class Ping(Subject):
    def execute(self, ip) -> None:
        if self.check_access(ip):
            for i in range(10):
                print(f'intento de ping: {i} a la ip: {ip}')
        else:
            print('No es posible realizar la solicitud')
            
    def check_access(self,ip) -> bool:  #chequea si la ip comienza con 192
        print("### Chequeando si coniscide la ip ###")
        if int(ip[:3])==192:
            return True
        else:
            return False
        
    def executefree(self,ip) -> bool:   #sin checkear ip
        print('sin chequear ip (executefree)')
        for i in range(10):
            print(f'intento de ping: {i} a la ip: {ip}')


class pingProxy(Subject):

    def __init__(self, ping: Ping) -> None:
        self._ping = ping

    def execute(self,ip) -> None:   #con comprobacion de ip
        if self.check_access(ip):   #si el chequeo es exitoso se conecta a la IP
            print('conectando a www.google.com...')
            self._ping.executefree(ip)
        else:
            print('conexion fallida...')
            print('intentando con execute')
            self._ping.execute(ip)
            
    def check_access(self,ip) -> bool:  #chequea si la ip coincide
        print("### Chequeando si coniscide con la ip guardada###")
        if ip =='192.168.0.254':
            return True
        else:
            return False
    def executefree(self,ip) -> bool:   #sin checkear ip
        print('no es posible usar desde proxy')

def client_code(subject: Subject) -> None:
    print('con chequeo de ip')
    subject.execute('192.168.0.254')
    print()
    print('sin chequeo de ip')
    subject.executefree('192.168.1.1')
    print()
    


if __name__ == "__main__":

    print("Client: Executing the client code with a real subject:")
    ping = Ping()
    client_code(ping)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = pingProxy(ping)
    client_code(proxy)

    print("")

