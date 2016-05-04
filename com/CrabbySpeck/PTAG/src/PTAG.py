#Custom made modules
import Music	#This is where all of the multi-threaded music is.
import PythonGameLib	#This is where we can see a formatted list of all of the player's statistics.

#Built-in Libraries
import time	#Allows us to add pauses between events.
import sys

#Game Libraries
import pyglet	#This is the general game library
#Extra Functions/Classes from Game Library
from pyglet.window import key	#Allows us to have keyboard input
from pyglet.window import mouse		#Allows us to have mouse input

class PTAGVars():
	
	#Global Variables
	playerInventory = []
	player = ['player', 10, False, 10, (0, 0)]
	started = False
	playerHealth = 'Player Health: ' + str(player[1])
	playerResistance = 'Resistance: ' + str(player[2])
	playerArmour = 'Player Armour: ' + str(player[3])
	playerLocation = 'Location: ' + str(player[4])
	missionObjective = 'Play the Game!'
	story = 'Hello. \n Spencer Said Hello. \n So does Jordan'

	stringPlayerStatisticsList = [player[0], playerHealth, playerResistance, playerArmour, playerLocation]
	
	wizardsBattleSong = '../assets/music/Final Battle of the Dark Wizards.mp3'
	floatingCitiesSong = '../assets/music/Floating Cities.mp3'
	rynosThemeSong = '../assets/music/Rynos_Theme.mp3'
	clashDefiantSong = '../assets/music/Clash Defiant.mp3'
	edmDetectionModeSong = '../assets/music/EDM Detection Mode.mp3'
	furiousFreakSong = '../assets/music/Furious Freak.mp3'
	overworldSong = '../assets/music/Overworld.mp3'
	professorUmlautSong = '../assets/music/Professor Umlaut.mp3'

	
class newGame():
	def selectDLL():		
		try:
			pyglet.lib.load_library('avbin64')
			pyglet.have_avbin=True
			print("Using avbin64")
		except OSError:
			pyglet.lib.load_library('avbin')
			pyglet.have_avbin=True
			print('Using avbin')
		
	def setupPlayer():
		player = PTAGVars.player
		playerHealth = PTAGVars.playerHealth
		playerName = str(input("What is your player's Name?\n"))
		health = 10
		resistance = False
		armour = 10
		player[0] = playerName
		player[1] = health
		player[2] = resistance
		player[3] = armour
		player[4] = (0, 0, 0)#Location. Change to fit the stating location and the location system
		playerHealth = playerHealth + str(player[1])

	
	
#Setup the game annd music stuffs
newGame.selectDLL()
newGame.setupPlayer()
#Play the music
sound = pyglet.media.load(PTAGVars.clashDefiantSong)
sound.play()
#Define the main window
window = pyglet.window.Window()

#Game Name and Start Button Labels
GameTitle = pyglet.text.Label("Python Text Adventure Game", font_name='Times New Roman', font_size=25, x=window.width//2, y=window.width//2, anchor_x='center', anchor_y='center', color=(255,0,0,255))
StartLabel = pyglet.text.Label("Click to Start", font_name='Times New Roman', font_size=15, x=(window.width//2)-20, y=(window.width//2)-100, anchor_x='center', anchor_y='center')

#Player Statistics Labels
playerNameLabel = pyglet.text.Label(PTAGVars.player[0], font_name='Times New Roman', font_size=10, x=window.width, y=window.height, anchor_x='right', anchor_y='top')
playerHealthLabel = pyglet.text.Label(PTAGVars.playerHealth, font_name='Times New Roman', font_size=10, x=window.width, y=(window.height-15), anchor_x='right', anchor_y='top')
playerResistanceLabel = pyglet.text.Label(PTAGVars.playerResistance, font_name='Times New Roman', font_size=10, x=window.width, y=(window.height-30), anchor_x='right', anchor_y='top')
playerArmourLabel = pyglet.text.Label(PTAGVars.playerArmour, font_name='Times New Roman', font_size=10, x=window.width, y=(window.height-45), anchor_x='right', anchor_y='top')
playerLocationLabel = pyglet.text.Label(PTAGVars.playerLocation, font_name='Times New Roman', font_size=10, x=window.width, y=(window.height-60), anchor_x='right', anchor_y='top')
missionObjectiveLabel = pyglet.text.Label(PTAGVars.missionObjective, font_name='Arial Rounded MT Bold', font_size=20, x=window.width//2 ,y=460, anchor_x='center', anchor_y='top')
storyLabel = pyglet.text.Label(PTAGVars.story, font_name='Arial', font_size=15, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

#Buttons
#Look Around Button
LookAroundButtonLabel = pyglet.text.Label('Look Around', font_name='Times New Roman', font_size=10, x=10, y=30, anchor_x='left', anchor_y='center')
def lookAround():
	if True:
		print()


@window.event
def on_key_press(symbol, modifiers):
	print('')

@window.event
def on_mouse_press(x, y, button, modifiers):
	print(x, y)
	pressToStart()
	LeButtonOne(x, y)

def pressToStart():
	if not PTAGVars.started:
		StartLabel.text=''
		moveTitleUp()
		PTAGVars.started = True
		print("DEBUG: PTAGVars.started = ", PTAGVars.started)
		
		#StoryLine()
	else:
		PTAGVars.started = True

def LeButtonOne(x, y):
	if x >= 197 and x <= 440 and y >= 351 and y <= 384:
		#Basic Button Code
		print('', end='')

def moveTitleUp():
	GameTitle.font_size=10
	GameTitle.y=480
	GameTitle.anchor_y='top'
	    
def playerStatistics():
	print('')

@window.event
def on_draw():
	window.clear()
	GameTitle.draw()
	StartLabel.draw()
	playerNameLabel.draw()
	playerHealthLabel.draw()
	playerResistanceLabel.draw()
	playerArmourLabel.draw()
	playerLocationLabel.draw()
	LookAroundButtonLabel.draw()
	missionObjectiveLabel.draw()
	storyLabel.draw()
	
	
pyglet.app.run()
sys.exit(0)

#Run code that is supposed to happen after the main game window is closed. 
