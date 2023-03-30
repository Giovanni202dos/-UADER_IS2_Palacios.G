import sys
import matplotlib.pyplot as plt
import numpy as np

def collatz(num,contador=0):
    #print('principal')
    #print('num: ',num)
    #print('contador: ',contador)
    #input()
    if num%2==0:    #si es par
        #print('entro al par')
        num=num/2
        contador+=1
        contador=collatz(num,contador) 
        #print('fff: ',contador) 
        #print("nummm: ",num) 
    elif(num!=1):   #si es impar y diferente de 1(ya q si es uno se termina todo)
        #print('entro al impar')
        num=(3*num)+1
        contador+=1
        #print('num-desp: ',num)
        #print('contador-desp: ',contador)
        contador=collatz(num,contador)
        #print('fffaaa: ',contador) 
    return contador

#sys.argv.append('2-3')
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
        lista=[]
        for i in range(desde,hasta+1):
            iteraciones = collatz(i)+1
            lista.append([i,iteraciones])   #guardo en una lista el n con la cantidad de iteracciones
            #print('el:',i,' con: ',iteraciones)

        for i in range(0,len(lista)):
            print(lista[i])

for i in range(0,len(lista)-1): #las grafico
    x_1=lista[i][0]
    x_2=lista[i+1][0]

    y_1=lista[i][1]
    y_2=lista[i+1][1]

    xaxis = np.array([x_1,x_2 ])
    yaxis = np.array([y_1,y_2])
    plt.plot(xaxis , yaxis)
plt.show()