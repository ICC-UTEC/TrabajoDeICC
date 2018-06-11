n = int(input())

for i in range(n): # range (0, n)
# for se ejectua siempre que cumpla la condicion i [0, n>

    for j in range(n - i):
        if (i + j) % 2 == 0:
            print('1',end='') # EOL \n
        else:
            print('0',end='')

    print('')
print(n)
# n = 5
# iteraciones    lon cadena
# i = 0              5
# i = 1              4
# i = 2              3
# i = 3              2
# i = 4              1
# i = 5 corte        -
# (i + j) % 2 == 0 -> 1 else -> 0
