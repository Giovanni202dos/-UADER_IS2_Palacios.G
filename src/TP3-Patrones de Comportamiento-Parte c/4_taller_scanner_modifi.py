import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

	def scan(self):
		
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))



#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

	def __init__(self, radio):

		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:


	def __init__(self):
		
		self.fmstate = FmState(self)
		self.amstate = AmState(self)
		self.memory =[{"M1":'AM'},{"M2":'FM'},{"M3":'AM'},{"M4":'FM'}]	#AGREGADO POR MI
		self.pos_en_memory=0

#*--- Inicialmente en FM

		self.state = self.fmstate

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()

	def scan_memory(self):	#AGREGADO POR MI
		self.pos_en_memory += 1
		if self.pos_en_memory == len(self.memory):
			self.pos_en_memory = 0
		clave ,valor=list(self.memory[self.pos_en_memory].items())[0]
		#print(valor,' != ',self.state.name,' ??')
		if valor!=self.state.name:	#si no coinsicen habra q ccambiar a la otra frecuencia(AM O FM) para mantener los estados
			#print('yess, cambaimos de state')
			self.toggle_amfm()
		print("meorizacion... Estación",clave, valor)

		#print("meorizacion... Estación",list(self.memory[self.pos_en_memory].keys()))


#*---------------------

if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	actions = [radio.scan_memory] * 4 +[radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan_memory] * 4 + [radio.scan] * 3
	actions *= 2

#*---- Recorre las acciones ejecutando la acción

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()

