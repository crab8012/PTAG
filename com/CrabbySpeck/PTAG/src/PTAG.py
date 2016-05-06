#Custom made modules
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
	player = ['player', 10, False, 10, (1, 1)]
	started = False
	playerHealth = 'Player Health: ' + str(player[1])
	playerResistance = 'Resistance: ' + str(player[2])
	playerArmour = 'Player Armour: ' + str(player[3])
	playerLocation = 'Location: ' + str(player[4])
	missionObjective = 'Play the Game!'
	mouseCoords = (0, 0)

	stringPlayerStatisticsList = [player[0], playerHealth, playerResistance, playerArmour, playerLocation]
	#Fonts
	hemiHead = '../assets/fonts/hemi head bd it.ttf'
	#Music
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
sound = pyglet.media.load(PTAGVars.professorUmlautSong)
sound.play()
#Define the main window
window = pyglet.window.Window()

class LabelsAndButtons():
	#Game Name and Start Button Labels
	GameTitle = pyglet.text.Label("Python Text Adventure Game", font_name='Times New Roman', font_size=25, x=window.width//2, y=window.width//2, anchor_x='center', anchor_y='center', color=(255,0,0,255))
	StartLabel = pyglet.text.Label("Click to Start", font_name='Times New Roman', font_size=15, x=(window.width//2)-20, y=(window.width//2)-100, anchor_x='center', anchor_y='center')
	
	#Player Statistics
	playerNameLabel = pyglet.text.Label(PTAGVars.player[0], font_name='Times New Roman', font_size=10, x=window.width, y=window.height, anchor_x='right', anchor_y='top')
	playerHealthLabel = pyglet.text.Label(PTAGVars.playerHealth, font_name='Times New Roman', font_size=10, x=window.width, y=(window.height-15), anchor_x='right', anchor_y='top')
	playerResistanceLabel = pyglet.text.Label(PTAGVars.playerResistance, font_name='Times New Roman', font_size=10, x=window.width, y=(window.height-30), anchor_x='right', anchor_y='top')
	playerArmourLabel = pyglet.text.Label(PTAGVars.playerArmour, font_name='Times New Roman', font_size=10, x=window.width, y=(window.height-45), anchor_x='right', anchor_y='top')
	playerLocationLabel = pyglet.text.Label(PTAGVars.playerLocation, font_name='Times New Roman', font_size=10, x=window.width, y=(window.height-60), anchor_x='right', anchor_y='top')
	
	#General Game Information Labels
	missionObjectiveLabel = pyglet.text.Label(PTAGVars.missionObjective, font_name='Arial Rounded MT Bold', font_size=10, x=window.width//2 ,y=0, anchor_x='center', anchor_y='bottom')
	storyLabel = pyglet.text.Label('The story here gets updated, like subtitles, with the voice.', font_name='Arial', font_size=10, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
	speaker = pyglet.image.load('../assets/images/Speaker.png')
	
	#Debug Labels
	pointerClickLocation = pyglet.text.Label('0, 0', font_name='Arial', font_size=10, x=window.width, y=0, anchor_x='right', anchor_y='bottom')
	fps = pyglet.clock.ClockDisplay()
	
	def inBounds(bounds, pointer):
		if pointer[0] <= bounds[2] and pointer[0] >= bounds[0] and pointer[1] <= bounds[1] and pointer[1] >= bounds[3]:
			return(True)
	
	#Buttons
	#Look Around Button
	LookAroundButtonLabel = pyglet.text.Label('Look Around', font_name='Times New Roman', font_size=10, x=10, y=300, anchor_x='left', anchor_y='center')
	def lookAround():
		pointer = PTAGVars.mouseCoords
		#Button Bounds:
		bounds = (10, 305, 89, 295)#Top Left, Bottom Right
		if LabelsAndButtons.inBounds(bounds, pointer):
			print("There is not much to see here")
		
	#Listen Closely Button
	ListenCloselyLabel = pyglet.text.Label('Listen Closely', font_name='Times New Roman', font_size=10, x=10, y=285, anchor_x='left', anchor_y='center')
	def listenClosely():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (9, 290, 89, 280)
		if LabelsAndButtons.inBounds(bounds, pointer):
			print("You hear muffled noises that could be voices or music.")
	
	#Feel Around Button
	FeelAroundLabel = pyglet.text.Label('Feel Around', font_name='Times New Roman', font_size=10, x=10, y=270, anchor_x='left', anchor_y='center')
	def feelAround():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (9, 275, 89, 265)
		if LabelsAndButtons.inBounds(bounds, pointer):
			print('hi')
		 
	
def storyNarration():
	print('You begin awaking in a room.')
	print('It is not your room.')
	print('The room is stone cold.')
	print('There are no lights.')
	print('You have to escape.')



@window.event
def on_key_press(symbol, modifiers):
	print('')

@window.event
def on_mouse_press(x, y, button, modifiers):
	pressToStart()
	PTAGVars.mouseCoords = (x, y)
	LabelsAndButtons.lookAround()
	LabelsAndButtons.listenClosely()
	LabelsAndButtons.feelAround()
	loc = [str(x), str(y)]
	pointerLoc = ','.join(loc)
	LabelsAndButtons.pointerClickLocation.text=pointerLoc
def pressToStart():
	if not PTAGVars.started:
		LabelsAndButtons.StartLabel.text=''
		moveTitleUp()
		PTAGVars.started = True
		print("DEBUG: PTAGVars.started = ", PTAGVars.started)
		storyNarration()

	else:
		PTAGVars.started = True

def LeButtonOne(x, y):
	if x >= 197 and x <= 440 and y >= 351 and y <= 384:
		#Basic Button Code
		print('', end='')

def moveTitleUp():
	GameTitle = LabelsAndButtons.GameTitle
	GameTitle.font_size=10
	GameTitle.y=480
	GameTitle.anchor_y='top'
	
@window.event
def on_draw():
	b = LabelsAndButtons()
	window.clear()#	Clear the display
	
	#	Draw the Game Infomation Labels
	b.GameTitle.draw()
	b.missionObjectiveLabel.draw()
	b.storyLabel.draw()
	
	#	Draw the Game Button Labels
	b.StartLabel.draw()
	b.LookAroundButtonLabel.draw()
	b.ListenCloselyLabel.draw()
	b.FeelAroundLabel.draw()
	
	#	Draw the Player Statistics Labels
	b.playerNameLabel.draw()
	b.playerHealthLabel.draw()
	b.playerResistanceLabel.draw()
	b.playerArmourLabel.draw()
	b.playerLocationLabel.draw()
	
	#	Draw the Game Debugging Labels
	b.pointerClickLocation.draw()
	b.fps.draw()
	
	
pyglet.app.run()
sys.exit(0)

#Run code that is supposed to happen after the main game window is closed. 
