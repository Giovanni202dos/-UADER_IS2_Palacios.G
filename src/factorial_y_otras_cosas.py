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

if len(sys.argv) == 0:
   print("Debe informar un número!")
   sys.exit()
num=int(sys.argv[1])
print("Factorial ",num,"! es ", factorial(num)) 

max = int(input("Find primes up to what number? : "))
primeList = []
#for loop for checking each number
for x in range(2, max + 1):
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
print(primeList)
#-------------------------------------------------------------
# prime number calculator: find the first n primes
count = int(input("Find how many primes?: "))
primeList = []
x = 2
while len(primeList) < count:
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
	x += 1
print(primeList)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   