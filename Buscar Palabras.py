#BUSCAR PALABRAS Y DECIR SI ESTA O NO
n=int(input())
palabras=[]
def palab(n):
    for i in range(n):
        pa=input()
        palabras.append(pa.upper())
palab(n)
#print(palabras)
k=input()
def comp(k):
    if k.upper() not in palabras:
        print(k, "no esta en la lista")
    else:
        print(k, "esta en la lista")
comp(k)
