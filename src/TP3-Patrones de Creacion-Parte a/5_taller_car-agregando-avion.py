import os

class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getCar(self):
      car = Car()
      
      # Primero el chasis
      body = self.__builder.getBody()
      car.setBody(body)
      
      # Luego el motor
      engine = self.__builder.getEngine()
      car.setEngine(engine)
      
      # Finalmente (4) ruedas
      i = 0
      while i < 4:
        wheel = self.__builder.getWheel()
        car.attachWheel(wheel)
        i += 1

      # Retorna el vehiculo completo
      return car

   def getAvion(self):
      avion = Avion()
      # Primero el chasis
      body = self.__builder.getBody()
      avion.setBody(body)

      # Luego el tiene 2 turbinas
      i = 0
      while i < 2:
         turbinas = self.__builder.getTurbinas()
         avion.setTurbinas(turbinas)
         i += 1
   
      # 2 alas
      i = 0
      while i < 2:
        ala = self.__builder.getAlas()
        avion.setAlas(ala)
        i += 1
      # tren de aterrizaje
      engine = self.__builder.getTrenAterrizaje()
      avion.setTrenAterrizaje(engine)
      #arma
      arma = self.__builder.getArmas()
      avion.setArmas(arma)
      return avion

class Car:
   def __init__(self):
      self.__wheels = list()
      self.__engine = None
      self.__body = None

   def setBody(self, body):
      self.__body = body

   def attachWheel(self, wheel):
      self.__wheels.append(wheel)

   def setEngine(self, engine):
      self.__engine = engine

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print ("planta motora: %d" % (self.__engine.horsepower))
      print ("ruedas: %d\'" % (self.__wheels[0].size))

class Avion:
   def __init__(self):
      self.__body = None
      self.__turbinas = list()
      self.__alas = list()
      self.__trenAterrizaje = None
      self.__armas=None
      
   def setBody(self, body):
      self.__body = body

   def setTurbinas(self, turbina):
      self.__turbinas.append(turbina)

   def setAlas(self, ala):
      self.__alas.append(ala)

   def setTrenAterrizaje(self, trenAterrizaje):
      self.__trenAterrizaje = trenAterrizaje

   def setArmas(self, arma):
      self.__armas = arma

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print ("turbinas: %d\'" % (self.__turbinas[0].horsepower))
      print ("alas: %d\'" % (self.__alas[0].tamaño))
      print ("Tren de aterrizaje: %d\'" % ( self.__trenAterrizaje.rodado))
      print ("Armas: ",self.__armas.existe)

#partes de un avion
class Turbinas:
   horsepower = None
class Alas:
   tamaño = None
class TrenAterrizaje:
   rodado = None
#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
   def getBody(self):pass

class CarBuilder(Builder):
      def getWheel(self): pass
      def getEngine(self): pass
      def getBody(self): pass

class AvionBuilder(Builder):
      def getBody(self): pass
      def getAlas(self): pass
      def getTurbinas(self): pass
      def getTrenAterrizaje(self): pass
      def getArmas(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Jeep
#* Establece instancias para tomar ruedas, motor y chasis
#* estableciendo las partes específicas que (en un Jeep) 
#* deben tener esas partes
#*-------------------------------------------------------
class JeepBuilder(CarBuilder):
   
   def getWheel(self):
      wheel = Wheel()
      wheel.size = 22
      return wheel
   
   def getEngine(self):
      engine = Engine()
      engine.horsepower = 400
      return engine
   
   def getBody(self):
      body = Body()
      body.shape = "SUV"
      return body


class AvionDeCargaBuilder(AvionBuilder):
   
   def getAlas(self):
      ala = Alas()
      ala.tamaño=400
      return ala

   def getTurbinas(self):
      turbina = Turbinas()
      turbina.horsepower=3000
      return turbina

   def getTrenAterrizaje(self):
      trenAterrizaje = TrenAterrizaje()
      trenAterrizaje.rodado=22
      return trenAterrizaje
   
   def getBody(self):
      body = Body()
      body.shape = "GRANDE"
      return body

   def getArmas(self):
      arma =ArmaGenerica()
      arma.existe=False
      return arma

class AvionMilitarBuilder(AvionBuilder):
   
   def getAlas(self):
      ala = Alas()
      ala.tamaño=360
      return ala

   def getTurbinas(self):
      turbina = Turbinas()
      turbina.horsepower=100000
      return turbina

   def getTrenAterrizaje(self):
      trenAterrizaje = TrenAterrizaje()
      trenAterrizaje.rodado=15
      return trenAterrizaje
   
   def getBody(self):
      body = Body()
      body.shape = "AERODINAMICO"
      return body

   def getArmas(self):
      arma =ArmaGenerica()
      arma.existe=True
      return arma
#*----------------------------------------------------------------
#* Define partes genéricas para un vehiculo (sin inicializar)
#*----------------------------------------------------------------
class Wheel:
   size = None

class Engine:
   horsepower = None

class Body:
   shape = None

class ArmaGenerica:
   existe = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   #jeepBuilder = JeepBuilder() # initializing the class
   avionBuilder =AvionDeCargaBuilder()
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Jeep
#*----------------------------------------------------------------   
   #director.setBuilder(jeepBuilder)
   director.setBuilder(avionBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Jeep según
#* la hoja de ruta
#*----------------------------------------------------------------
   #jeep = director.getCar()
   avion_de_carga = director.getAvion()

#AHORA CREAMOS UN AVION DE GUERRA
   avionBuilder=AvionMilitarBuilder()
   director.setBuilder(avionBuilder)
   avion_militar=director.getAvion()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   #print('creando un jeep:\n')
   #jeep.specification()
   print ("\n\n")
   print('creando un avion de carga:\n')
   avion_de_carga.specification()
   print('\n')
   print('creando un avion militar:\n')
   avion_militar.specification()
#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un vehículo\n")

   main()
