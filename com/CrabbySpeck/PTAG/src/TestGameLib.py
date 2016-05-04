import PythonGameLib
import Music
import time
import os

from threading import Thread

print("What do you want to listen to?")
print("1:\tRynos Theme")
print("2:\tFinal Battle of the Dark Wizards")
print("3:\tFloating Cities")

x = 0
try:
	x = int(input('hi: '))
except(ValueError):
	x = 3

if x == 1:
	print("Playing Rynos Theme")
	Music.Music.playRyno()
elif x == 2:
	print("Playing Final Battle of the Dark Wizards")
	Music.Music.playWizards()
else:
	print("Playing Floating Cities")
	Music.Music.playCity()
	
name = input("What is your name? ")
print("Nice to meet you, ", name, "!")

inv = [('Dog', 1), ('Cat', 1), ('Rat', 0)]
PythonGameLib.Inventory.inventoryTable(inv)
