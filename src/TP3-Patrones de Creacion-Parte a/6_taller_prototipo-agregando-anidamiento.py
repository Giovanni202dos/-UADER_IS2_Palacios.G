#*-------------------------------------------------------------------------
#* prototipo.py
#* Ejemplo para creación de prototipos
#*-------------------------------------------------------------------------
from abc import ABC, abstractmethod
import time
from datetime import datetime   #libreria para obtener la fecha y hora del sistema
import copy
import os   #libreria para trabajar con direcotrios desde el terminal(creo)

#*-------------------------------------------------------------------------
#* La clase prototipo utilizada como ejemplo puede estar en una librería
#* externa y ser importada.
#* Define los atributos mandatorios y relevantes, simula actividad por
#* medio de retardos
#*-------------------------------------------------------------------------
# Class Creation
class Prototype(ABC):
    # Constructor:
    def __init__(self):
        # Mocking an expensive call
        time.sleep(1)   #simula un retardo
        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

#*------------------------------------------------------------------------------
#* El método clone() no está definido en el prototipo y mediante @abstractmethod
#* se fuerza a que cualquier instancia que se haga de ésta clase lo tenga que
#* definir.
#*------------------------------------------------------------------------------
    # Clone Method:
    @abstractmethod
    def clone(self):
        pass 

#*------------------------------------------------------------------------------
#* Clase productiva que puedo querer usar como plantilla
#*------------------------------------------------------------------------------
class Shopkeeper(Prototype):    #para crear Shopkeeper va a tradar 6 seconds ya que llama al constructor Super(en donde esta el otro time.sleep)
    def __init__(self, height, age, defense, attack):
        super().__init__()
        # Mock expensive call
        time.sleep(1)   #simula un retardo
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Subclass-specific Attribute
        self.charisma = 30


    # Implementa el método de clonado mediante una copia de arbol de métodos
    def clone(self):
        return copy.deepcopy(self)   #creamos una copia del objeto 

#*-------------------------------------------------------------------------
#* clase 
#* define un atributo específico
#*-------------------------------------------------------------------------
class Warrior(Prototype):       #este no va a tardar nada ya que no llama al constructor Super
    def __init__(self, height, age, defense, attack):
        # Call superclass constructor, time.sleep() and assign base values
        # Concrete class attribute
        self.stamina = 60
    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self)  

#*--------------------------------------------------------------------------
class Mage(Prototype):  #lo mismo q el anterior
    def __init__(self, height, age, defense, attack):
    # Call superclass constructor, time.sleep() and assign base values
        self.mana = 100

    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self) 

#*--------------------------------------------------------------------------
#* Punto de entrada de ejecución
#*--------------------------------------------------------------------------
os.system("clear")
print("Ejemplo de taller para patrón prototipo")

dt = datetime.now()
print('Comienzo creando un objeto Shopkeeper NPC: ', dt)
shopkeeper = Shopkeeper(180, 22, 5, 8)                  #si sumamos los sleep q hay para crear el objeto de la clase Prototype y luego Shopkeeper dan como resultado 6 seconds se tardanza

dt = datetime.now()
print('Finaliza la creación del objeto Shopkeeper NPC: ', dt)
print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))

dt = datetime.now()
print('Instanciando ahora trader: ', dt)    #creamos a 5 Shopkeeper en total tardariamos (5*6) son 30 seconds
for i in range(20):
    shopkeeper = Shopkeeper(180, 22, 5, 8)
    dt = datetime.now()
    print(f'Creo Shopkeeper NPC {i} at: ', dt)

dt = datetime.now()
print('Finalizó de crear el grupo trader: ', dt)

dt = datetime.now()
print('Puedo hacerlo masivamente con 20 NPCs: ', dt)
shopkeeper_template = Shopkeeper(180, 22, 5, 8)
warrior_template = Warrior(185, 22, 4, 21)
mage_template = Mage(172, 65, 8, 15)
for i in range(20):  #creo una copia de los objetos
    shopkeeper_clone = shopkeeper_template.clone()
    warrior_clone = warrior_template.clone()
    mage_clone = mage_template.clone()
    dt = datetime.now()
    print(f'Finaliza la creación de tripletes mediante clone {i} at: ', dt)

dt = datetime.now()
print('Finalizó la creación de la población NPC: ', dt)
