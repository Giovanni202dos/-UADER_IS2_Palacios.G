._factorial.py                                                                                      000666  000766  000024  00000000252 14216473352 013741  0                                                                                                    ustar 00PCOLLA                          staff                           000000  000000                                                                                                                                                                             Mac OS X            	   2   x      ª                                      ATTR       ª   ˜                     ˜     com.apple.quarantine q/0081;00000000;;                                                                                                                                                                                                                                                                                                                                                       PaxHeader/factorial.py                                                                              000666  000766  000024  00000000163 14216473352 015476  x                                                                                                    ustar 00PCOLLA                          staff                           000000  000000                                                                                                                                                                         62 LIBARCHIVE.xattr.com.apple.quarantine=MDA4MTswMDAwMDAwMDs7
53 SCHILY.xattr.com.apple.quarantine=0081;00000000;;
                                                                                                                                                                                                                                                                                                                                                                                                             factorial.py                                                                                        000666  000766  000024  00000001610 14216473352 013523  0                                                                                                    ustar 00PCOLLA                          staff                           000000  000000                                                                                                                                                                         #!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un nÃºmero                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un nÃºmero negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 0:
   print("Debe informar un nÃºmero!")
   sys.exit()
num=int(sys.argv[1])
print("Factorial ",num,"! es ", factorial(num)) 

                                                                                                                        ._primos.py                                                                                         000666  000766  000024  00000000252 14221173672 013304  0                                                                                                    ustar 00PCOLLA                          staff                           000000  000000                                                                                                                                                                             Mac OS X            	   2   x      ª                                      ATTR       ª   ˜                     ˜     com.apple.quarantine q/0081;00000000;;                                                                                                                                                                                                                                                                                                                                                       PaxHeader/primos.py                                                                                 000666  000766  000024  00000000163 14221173672 015041  x                                                                                                    ustar 00PCOLLA                          staff                           000000  000000                                                                                                                                                                         62 LIBARCHIVE.xattr.com.apple.quarantine=MDA4MTswMDAwMDAwMDs7
53 SCHILY.xattr.com.apple.quarantine=0081;00000000;;
                                                                                                                                                                                                                                                                                                                                                                                                             primos.py                                                                                           000666  000766  000024  00000001555 14221173672 013076  0                                                                                                    ustar 00PCOLLA                          staff                           000000  000000                                                                                                                                                                         # prime number calculator: find all primes up to n
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