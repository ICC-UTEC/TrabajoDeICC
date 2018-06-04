n=int(input('Ingrese el rango de valores :'))
sumapar=0
sumaimpar=0
for i in range(n):
    k=int(input("Ingrese los números: "))
    if k//2>=0 and k%2==0:
        sumapar=sumapar+(k**2)
    else:
        sumaimpar=sumaimpar+(k**2)
print(sumapar)
print(sumaimpar)

#listas alternas
n = int(input("ingres el numero de numeros:"))
arreglo1 = []
arreglo2 = []

for i in range(n * 2):
    valor = int(input("Ingrese el numero de valores:"))

    if i % 2 == 0:
        arreglo1.append(valor)
    else:
        arreglo2.append(valor)

suma_minimos = min(arreglo1) + min(arreglo2)
print(suma_minimos)
