#Triángulo invertido
def triainvert(n,k,l):
    for i in range(n): # range (0, n)

        # for se ejectua siempre que cumpla la condicion i [0, n>
        for j in range(n - i):
            if (i + j) % 2 == 0:
                print(k,end='') # EOL \n
            else:
                print(l,end='')
        print('')
    print("Alli está el triángulo binario invertido de ",n, "ya sea de simbolos o numérico")

# n = 5
# iteraciones    lon cadena
# i = 0              5
# i = 1              4
# i = 2              3
# i = 3              2
# i = 4              1
# i = 5 corte        -

# (i + j) % 2 == 0 -> 1 else -> 0
p = int(input())
r=input()
s=input()
triainvert(p,r,s)