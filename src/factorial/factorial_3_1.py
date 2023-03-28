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


if len(sys.argv) == 1:  #cambie por 1(habia un cero) si hay un elemento guardado es porque no ingreso el numero
   print("Debe ingresar un numero!")
   sys.exit()
else: 
    hasta =int(sys.argv[1])
    if hasta>=1:
        for i in range(1, hasta+1):
            print("Factorial ",i,"! es ", factorial(i)) 
    else:
        print("Debe ingresar un numero adecuado!")
        sys.exit()


