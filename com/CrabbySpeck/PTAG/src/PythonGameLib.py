import random
import winsound
import pyglet
import PTAG

class Weapons():
	def weaponFist(enemy):
		#enemy[name, damage, health, resistance buff, armour]
		name = enemy[0]
		damage = enemy[1]
		health = enemy[2]
		resistance = enemy[3]
		armour = enemy[4]
		print("You hit ", name, "with your fist")
		enemy[2] = entityDamage(health, armour, resistance, givenDamage)
		
		return(enemy)
	
	def weaponBottle(enemy, inventory):
		givenDamage = RandomDamage(2,3)
		name = enemy[0]
		damage = enemy[1]
		health = enemy[2]
		resistance = enemy[3]
		armour = enemy[4]
		print("You hit ", name, "with your fist")
		enemy[2] = entityDamage(health, amour, resistance, givenDamage)
		durability = durability - 1
		if durability == 0:
			print("The Bottle Broke")
		return(enemy, inventory)
	
	def weaponBrokenBottle(enemy, inventory):
		name = enemy[0]
		damage = enemy[1]
		health = enemy[2]
		esistance = enemy[3]
		armour = enemy[4]
		durability = name
		
class Inventory():
	def findInInventory(inventory, searchItem):
		itemIndex = inventory.index(searchItem)
	
	def inventoryFull(inventory):
		if len(inventory) == 3:
			print('You cannot pick that item up. Your inventory is full.')
			print('0: ', inventory[0])
			print('1: ', inventory[1])
			print('2: ', inventory[2])
			return(True)
		else:
			return(False)
	
	def dropInventory(inv):
		if Inventory.inventoryFull(inv):
				try:
					print("-1: Cancel")
					x = int(input("Your inventory is full. What do you want to drop? "))
					if x != (-1):
						inv.pop(x)
						inv.append(('----', 0))
				except (ValueError, IndexError):
					print("You did not enter a proper value. Try again.")
					Inventory.dropInventory(inv)
				return(inv)
					
	def inventoryTable(inv):
		
		#Header
		print('Item', end='\t')
		print('#', end='\n')
		#Item One
		print(inv[0][0], end='\t')
		print(inv[0][1], end='\n')
		#Item Two
		print(inv[1][0], end='\t')
		print(inv[1][1], end='\n')
		#Item Three
		print(inv[2][0], end='\t')
		print(inv[2][1], end='\n')

class Damages():	
	def entityDamage(health, armour, resistance, takenDamage):
		newHealth = 0
		health = health + armour
		if resistance:
			damage = takenDamage/2
			newHealth = health - damage
		else:
			newHealth = health - takenDamage
					
		return(newHealth)
	
	def RandomDamage(a, b):
		random.randrange(a, b)

	def isDead(health):
		if health <=0:
			return(True)
		else:
			return(False)
			
class SaveLoadGame():
	print()
			
class PythonGameAudio():
	def winsoundPlayMusic(song):
		winsound.PlaySound(song, winsound.SND_FILENAME)
		print("Playing Music")		

class Player():
	def listStats(player):
		strStats = PTAGVars.stringPlayerStatisticsList
		health = PTAG.playerHealthLabel
		resistance = PTAG.playerResistanceLabel
		armour = PTAG.playerArmourLabel
		location = PTAG.playerLocationLabel
		name = PTAG.playerNameLabel
		
		health.text=strStats[1]
		resistance.text=strStats[2]
		armour.text=strStats[3]
		location.text=strStats[4]
