n=int(input('Ingrese el rango de valores que desee:'))
sumapar=0
sumaimpar=0
for i in range(n):
    k=int(input("Ingrese el número: "))
    if k//2>=0 and k%2==0:
        sumapar=sumapar+(k**2)
    else:
        sumaimpar=sumaimpar+(k**2)
print(sumapar)
print(sumaimpar)
