#!/usr/bin/python3

import random


n = int(input("Ingrese el numbero de veces que desea tirar el dado: "))
jugador01 = str(input("Ingrese nombre del jugador 1: "))
jugador02 = str(input("Ingrese nombre del jugador 2: "))


def dado():
	resultado_dado = random.randint(1,6)
	return resultado_dado

def lanzar(numero_de_veces):
	tiro = 0
	for i in range(n):
		tiro = dado() + tiro
	return tiro

def jugada(nombre1, nombre2):
	tiro1 = lanzar(n)
	tiro2 = lanzar(n)
	print(jugador01, "Ha sacado: ")
	print(tiro1)
	print(jugador02, "Ha sacado: ")
	print(tiro2)
	if tiro1 > tiro2:
		print(jugador01, "Ha ganado")
	else:
		print(jugador02, "Ha ganado")
	return

lanzar(n)
jugada(jugador01, jugador02)
