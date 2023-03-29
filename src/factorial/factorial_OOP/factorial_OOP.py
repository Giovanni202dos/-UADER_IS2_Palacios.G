import sys

class Factorial:    #clase Factorial
    def __init__(self, min, max):   #constructor
        self.run(min,max)

    def run(self,min,max):  #Metodo run
        for num in range(min,max+1):
            numero=num
            if num < 0: 
                print("Factorial de un número negativo no existe")

            elif num == 0: 
                print("Factorial ",num,"! es ", 1)
                
            else: 
                fact = 1
                while(num > 1): 
                    fact *= num 
                    num -= 1
                print("Factorial ",numero,"! es ", fact)
            



if len(sys.argv) == 1:  #cambie por 1(habia un cero) si hay un elemento guardado es porque no ingreso el numero
   print("Debe ingresar un rango!")
   sys.exit()
else: 
    desde, hasta =sys.argv[1].split('-')
    desde =int(desde)
    hasta =int(hasta)
    if desde>hasta:
        print("Debe ingresar un rango adecuado!")
        sys.exit()
    else:
        factoriall = Factorial(desde , hasta) #creamos una instancia de la clase

