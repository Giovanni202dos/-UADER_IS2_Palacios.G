#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
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

desde, hasta =sys.argv[1].split('-')
desde =int(desde)
hasta =int(hasta)
if len(sys.argv) == 1 or desde>hasta:  #cambie por 1(habia un cero) si hay un elemento guardado es porque no ingreso el numero
   print("Debe informar un rango adecuado!")
   sys.exit()
else: 
    print('entroo')
    for i in range(desde, hasta+1):
        print("Factorial ",i,"! es ", factorial(i)) 

