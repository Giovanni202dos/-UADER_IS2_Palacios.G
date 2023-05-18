

import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------

class Memento:
	def __init__(self, file, content):
		
		self.file = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):

		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string


	def save(self):	# retorna para guardar una version
		return Memento(self.file, self.content)

	def undo(self, memento):	#para restaurar una version
		self.file = memento.file
		self.content = memento.content
	def content_actual(self):
		print(f'contenido actual: {self.content}')


class FileWriterCaretaker:	#el que guarda todas las versiones (en este caso solo a una version anterior)

	def __init__(self) -> None:
		self.objs=[]

	def save(self, writer):	#se le pasa un FileWriterUtility
		if len(self.objs)<4:
			self.objs.append(writer.save())
		else:
			print('no hay capacidad')

	def undo(self, writer, num):
		if num<len(self.objs):
			#print('ggg',self.objs[num].content)
			self.objs.reverse()	#lo doy vuelta
			writer.undo(self.objs[num])
			self.objs.reverse()	#lo vuelvo a su estado original
		else:
			print('ubicacion excedida')

	def mostrar_todas(self):
		i=0
		print('Todas las versiones guardadas: ')
		for memento in self.objs:
			print(i,': ',memento.content)
			i+=1


if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar");
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	print("Se graba información adicional")
	writer.write("Material1\n")
	caretaker.save(writer)
	writer.content_actual()

	print("Se graba información adicional")
	writer.write("Material2\n")
	caretaker.save(writer)
	writer.content_actual()

	print("Se graba información adicional")
	writer.write("Material3\n")
	caretaker.save(writer)
	writer.content_actual()

	print("Se graba información adicional")
	writer.write("Material4\n")
	caretaker.save(writer)
	writer.content_actual()



	print("Se graba información adicional")
	writer.write("Material5\n")
	caretaker.save(writer)
	writer.content_actual()

	caretaker.mostrar_todas()

	writer.content_actual()
	print('restauro a versiones X')
	caretaker.undo(writer ,0)
	writer.content_actual()

	caretaker.undo(writer ,1)
	writer.content_actual()

	caretaker.undo(writer ,2)
	writer.content_actual()

	caretaker.undo(writer ,3)
	writer.content_actual()


