import sys

class Factorial:    #clase Factorial
    def __init__(self, min, max):
        pass

    def run(self,num):  #Metodo run (facotorial de un solo numero)
        if num < 0: 
            print("Factorial de un número negativo no existe")

        elif num == 0: 
            return 1
            
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 
    def factorial_en_range(self,min,max):   #Metodo para calcular el facotorial en un rango
        for i in range(min , max+1):
            num = max
            #print("num:", num)
            #print("max-antes:", max)
            fact = 1
            #print("fact:", fact)
            while(num >= min and num!=0): 
                fact *= num 
                #print('fff ', fact)
                num -= 1
                #print('num fff ', num)
            print("Factorial ",max,"! es ", fact) 
            max -=1
            #print("max-despues:", max)
            



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
        factoriall = Factorial() #creamos una instancia de la clase
        factoriall.factorial_en_range(desde , hasta)

