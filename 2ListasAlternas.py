#!/usr/bin/python3

b = int(input("Cantidad de numeros a ingresar: "))
arreglo1 = []
arreglo2 = []

for i in range(0, b*2):
	if i%2==0:
		arreglo1.insert(0, int(input("Dame un numero: ")))
	else:
		arreglo2.insert(0, int(input("No, damelo a mi: "))) 

print(min(arreglo1) + min(arreglo2))
