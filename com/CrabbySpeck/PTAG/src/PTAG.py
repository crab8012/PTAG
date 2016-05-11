#Custom made modules
import PythonGameLib as pgl	#This is where we can see a formatted list of all of the player's statistics. We import it as pgl so we dont have to keep typing 'PythonGameLib._()'
from PythonGameLib import *
#Built-in Libraries
import time	#Allows us to add pauses between events.
import sys
#Game Libraries
import pyglet	#This is the general game library
#Extra Functions/Classes from Game Library
from pyglet.window import key	#Allows us to have keyboard input
from pyglet.window import mouse		#Allows us to have mouse input
def storyNarration():
	print('You begin awaking in a room.')
	print('It is not your room.')
	print('The room is stone cold.')
	print('There are no lights.')
	print('You have to escape.')
def pressToStart():
	if not PTAGVars.started:
		LabelsGeneral.StartLabel.text=''
		moveTitleUp()
		PTAGVars.started = True
		if PTAGVars.DeBuG:
			print("DEBUG: PTAGVars.started = ", PTAGVars.started)
		storyNarration()

	else:
		PTAGVars.started = True
def LeButtonOne(x, y):
	if x >= 197 and x <= 440 and y >= 351 and y <= 384:
		#Basic Button Code
		print('', end='')
def moveTitleUp():
	GameTitle = LabelsGeneral.GameTitle
	GameTitle.font_size=10
	GameTitle.y=window.height
	GameTitle.anchor_y='top'
def endRoom():
	#Code goes here to switch to the next level
	print('You have escaped 1-1')
	LabelsGeneral.storyLabel.text='You have escaped 1-1'
class PTAGVars():
	
	#Tells Whether or not to print the Debug Information to the console or the screen
	DeBuG = True	#	True means that the debug stuff is shown and false means that it isn't.
	
	#Global Variables
	playerInventory = []
	player = ['player', 10, False, 10, (1, 1)]
	started = False
	playerHealth = 'Player Health: ' + str(player[1])
	playerResistance = 'Resistance: ' + str(player[2])
	playerArmour = 'Player Armour: ' + str(player[3])
	playerLocation = 'Location: ' + str(player[4])
	missionObjective = 'Escape The Room'
	mouseCoords = (0, 0)
	fs = False
	level=0

	found_Stone=False
	doorUnlocked=False
	found_Key=False
	
	ButtonFont = ['Times New Roman', 10]
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
	
	song = [wizardsBattleSong, floatingCitiesSong, rynosThemeSong, clashDefiantSong, edmDetectionModeSong, furiousFreakSong, overworldSong, professorUmlautSong]
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
def inBounds(bounds, pointer):
		if pointer[0] <= bounds[2] and pointer[0] >= bounds[0] and pointer[1] <= bounds[1] and pointer[1] >= bounds[3]:
			return(True)
		else:
			return(False)
#Setup the game and music stuffs
newGame.selectDLL()
newGame.setupPlayer()
#Play the music
sound = pyglet.media.load(PTAGVars.song[0])
sound.play()
#Define the main window
window = pyglet.window.Window(caption='Python Text Adventure Game - Room 1.1 - Rv1')
class RoomOne():
	font = PTAGVars.ButtonFont[0]
	size = PTAGVars.ButtonFont[1]
	
	#Buttons
	#Look Around Button
	LookAroundButtonLabel = pyglet.text.Label('Look Around', font_name=font, font_size=10, x=10, y=300, anchor_x='left', anchor_y='center')
	def lookAround():
		pointer = PTAGVars.mouseCoords
		#Button Bounds:
		bounds = (10, 305, 89, 295)#Top Left, Bottom Right
		if inBounds(bounds, pointer):
			LabelsGeneral.storyLabel.text='There is not much to see here'
			print("There is not much to see here")
		
	#Listen Closely Button
	ListenCloselyLabel = pyglet.text.Label('Listen Closely', font_name=font, font_size=10, x=10, y=285, anchor_x='left', anchor_y='center')
	def listenClosely():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (9, 290, 89, 280)
		if inBounds(bounds, pointer):
			print("You hear muffled noises that could be voices or music.")
			LabelsGeneral.storyLabel.text='You hear muffled noises that could be voices or music'
	
	#Feel Around Button
	FeelAroundLabel = pyglet.text.Label('Feel Around', font_name=font, font_size=10, x=10, y=270, anchor_x='left', anchor_y='center')
	def feelAround():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (9, 275, 89, 265)
		if inBounds(bounds, pointer):
			LabelsGeneral.storyLabel.text='You find a door and a loose stone.'
			PTAGVars.found_Stone=True
			print('You find a door and a loose stone.')
	
	#Try Door Button
	TryDoorLabel = pyglet.text.Label('Try the door', font_name=font, font_size=10, x=10, y=270, anchor_x='left', anchor_y='center')
	def tryDoor():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (10, 275, 78, 266)
		if inBounds(bounds, pointer):
			if PTAGVars.found_Key:
				print("The door opens smoothly and quietly.")
				LabelsGeneral.storyLabel.text='The door opens smoothly and quietly.'
				endRoom()
			else:
				print("The door is locked. You must find a key before it will open.")
				LabelsGeneral.storyLabel.text='The door is locked. You must find a key before it will open.'
	
	#Try Stone Button
	TryStoneLabel = pyglet.text.Label('Look under the stone', font_name=font, font_size=size, x=100, y=270, anchor_x='left', anchor_y='center')
	def tryStone():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (97, 275, 218, 266)
		if inBounds(bounds, pointer):
			print('Y1ou find a key underneath the stone. It might go to a door')
			LabelsGeneral.storyLabel.text='You find a key underneath the stone. It might go to a door.'
			PTAGVars.found_Key = True	
	
	def ButtonRoomOne():
		RoomOne.listenClosely()
		RoomOne.lookAround()
				
		if not PTAGVars.found_Stone:
			RoomOne.feelAround()
		if PTAGVars.found_Stone:
			RoomOne.tryDoor()
			RoomOne.tryStone()
		
	def DrawRoomOne():
		RoomOne.LookAroundButtonLabel.draw()
		RoomOne.ListenCloselyLabel.draw()
		
		if not PTAGVars.found_Stone:
			RoomOne.FeelAroundLabel.draw()
		if PTAGVars.found_Stone:
			RoomOne.TryDoorLabel.draw()
			RoomOne.TryStoneLabel.draw()
class RoomOne_ReturnOne():
	LeaveRoomButton = pyglet.text.Label('Leave Room', font_name='Times New Roman', font_size=10, x=10, y=100, anchor_x='left', anchor_y='center')
	def LeaveRoom():
		PTAGVars.level=10
	def DrawRoomOne():
		RoomOne_ReturnOne.LeaveRoomButton()
class HallOne():
	font = PTAGVars.ButtonFont[0]
	size = PTAGVars.ButtonFont[1]
	
	#Buttons
	#Look Around Button
	GoBackButtonLabel = pyglet.text.Label('Go back inside the room', font_name=font, font_size=10, x=10, y=300, anchor_x='left', anchor_y='center')
	def lookAround():
		pointer = PTAGVars.mouseCoords
		#Button Bounds:
		bounds = (10, 305, 89, 295)#Top Left, Bottom Right
		if inBounds(bounds, pointer):
			LabelsGeneral.storyLabel.text='You have been here before. There is nothing to see here'
			print("You have been here before. There is nothing to see here")
			PTAGVars.level=1
			
		
	#Listen Closely Button
	ListenCloselyLabel = pyglet.text.Label('Listen Closely', font_name=font, font_size=10, x=10, y=285, anchor_x='left', anchor_y='center')
	def listenClosely():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (9, 290, 89, 280)
		if inBounds(bounds, pointer):
			print("You hear muffled noises that could be voices or music.")
			LabelsGeneral.storyLabel.text='You hear muffled noises that could be voices or music'
	
	#Feel Around Button
	FeelAroundLabel = pyglet.text.Label('Feel Around', font_name=font, font_size=10, x=10, y=270, anchor_x='left', anchor_y='center')
	def feelAround():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (9, 275, 89, 265)
		if inBounds(bounds, pointer):
			LabelsGeneral.storyLabel.text='You find a door and a loose stone.'
			PTAGVars.found_Stone=True
			print('You find a door and a loose stone.')
	
	#Try Door Button
	TryDoorLabel = pyglet.text.Label('Try the door', font_name=font, font_size=10, x=10, y=270, anchor_x='left', anchor_y='center')
	def tryDoor():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (10, 275, 78, 266)
		if inBounds(bounds, pointer):
			if PTAGVars.found_Key:
				print("The door opens smoothly and quietly.")
				LabelsGeneral.storyLabel.text='The door opens smoothly and quietly.'
				endRoom()
			else:
				print("The door is locked. You must find a key before it will open.")
				LabelsGeneral.storyLabel.text='The door is locked. You must find a key before it will open.'
	
	#Try Stone Button
	TryStoneLabel = pyglet.text.Label('Look under the stone', font_name=font, font_size=size, x=100, y=270, anchor_x='left', anchor_y='center')
	def tryStone():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (97, 275, 218, 266)
		if inBounds(bounds, pointer):
			print('Y1ou find a key underneath the stone. It might go to a door')
			LabelsGeneral.storyLabel.text='You find a key underneath the stone. It might go to a door.'
			PTAGVars.found_Key = True	
	
	def ButtonRoomOne():
		RoomOne.listenClosely()
		RoomOne.lookAround()
				
		if not PTAGVars.found_Stone:
			RoomOne.feelAround()
		if PTAGVars.found_Stone:
			RoomOne.tryDoor()
			RoomOne.tryStone()
		
	def DrawRoomOne():
		RoomOne.LookAroundButtonLabel.draw()
		RoomOne.ListenCloselyLabel.draw()
		
		if not PTAGVars.found_Stone:
			RoomOne.FeelAroundLabel.draw()
		if PTAGVars.found_Stone:
			RoomOne.TryDoorLabel.draw()
			RoomOne.TryStoneLabel.draw()

class LabelsGeneral():	
	font = PTAGVars.ButtonFont[0]
	size = PTAGVars.ButtonFont[1]
	#Game Name and Start Button Labels
	GameTitle = pyglet.text.Label("Python Text Adventure Game", font_name=font, font_size=size, x=window.width//2, y=window.width//2, anchor_x='center', anchor_y='top', color=(255,0,0,255))
	StartLabel = pyglet.text.Label("Click to Start", font_name=font, font_size=size, x=(window.width//2)-20, y=(window.width//2)-100, anchor_x='center', anchor_y='center')
	
	#General Game Information Labels
	missionObjectiveLabel = pyglet.text.Label(PTAGVars.missionObjective, font_name='Arial Rounded MT Bold', font_size=10, x=window.width//2 ,y=0, anchor_x='center', anchor_y='bottom')
	storyLabel = pyglet.text.Label('', font_name='Arial', font_size=10, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
	speaker = pyglet.image.load('../assets/images/Speaker.png')
	
	def DrawGeneralLabels():
		LabelsGeneral.GameTitle.draw()
		LabelsGeneral.missionObjectiveLabel.draw()
		LabelsGeneral.storyLabel.draw()
		LabelsGeneral.StartLabel.draw()
class PlayerStats():
	font = PTAGVars.ButtonFont[0]
	size = PTAGVars.ButtonFont[1]
	
	#Player Statistics
	playerNameLabel = pyglet.text.Label(PTAGVars.player[0], font_name=font, font_size=size, x=window.width, y=window.height, anchor_x='right', anchor_y='top')
	playerHealthLabel = pyglet.text.Label(PTAGVars.playerHealth, font_name=font, font_size=size, x=window.width, y=(window.height-15), anchor_x='right', anchor_y='top')
	playerResistanceLabel = pyglet.text.Label(PTAGVars.playerResistance, font_name=font, font_size=10, x=window.width, y=(window.height-30), anchor_x='right', anchor_y='top')
	playerArmourLabel = pyglet.text.Label(PTAGVars.playerArmour, font_name=font, font_size=10, x=window.width, y=(window.height-45), anchor_x='right', anchor_y='top')
	playerLocationLabel = pyglet.text.Label(PTAGVars.playerLocation, font_name=font, font_size=10, x=window.width, y=(window.height-60), anchor_x='right', anchor_y='top')
	
	def DrawPlayerStats():
		PlayerStats.playerNameLabel.draw()
		PlayerStats.playerHealthLabel.draw()
		PlayerStats.playerResistanceLabel.draw()
		PlayerStats.playerArmourLabel.draw()
		PlayerStats.playerLocationLabel.draw()		
class DebugStuffs():
	#Debug Labels
	pointerClickLocation = pyglet.text.Label('0, 0', font_name='Arial', font_size=10, x=window.width, y=0, anchor_x='right', anchor_y='bottom')
	fps = pyglet.clock.ClockDisplay()
	
	def DrawDebugStuff():
		DebugStuffs.pointerClickLocation.draw()
		DebugStuffs.fps.draw()
@window.event
def on_key_press(symbol, modifiers):
	print('')
@window.event
def on_mouse_press(x, y, button, modifiers):
	pressToStart()
	PTAGVars.mouseCoords = (x, y)
	Level=PTAGVars.level
	
	if Level==0:
		RoomOne.listenClosely()
		RoomOne.lookAround()
		if not PTAGVars.found_Stone:
			RoomOne.feelAround()
		if PTAGVars.found_Stone:
			RoomOne.tryDoor()
			RoomOne.tryStone()
	elif Level==1:
		RoomOne_ReturnOne.LeaveRoom()
		
	loc = [str(x), str(y)]
	pointerLoc = ','.join(loc)
	DebugStuffs.pointerClickLocation.text=pointerLoc	
@window.event
def on_draw():
	level = PTAGVars.level
	window.clear()#	Clear the display
	#	Draw the Game Infomation Labels
	LabelsGeneral.DrawGeneralLabels()
	#	Draw the Player Statistics Labels
	PlayerStats.DrawPlayerStats()
	#	Draw the Game Debugging Labels
	if PTAGVars.DeBuG:
		DebugStuffs.DrawDebugStuff()
	
	if level==0:
		#	Draw The Stuff for Room One
		RoomOne.DrawRoomOne()
	elif level==1:
		RoomOne_ReturnOne.DrawRoomOne
pyglet.app.run()
sys.exit(0)
