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
from pyglet import font
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
	level = PTAGVars.level
	#Code goes here to switch to the next level
	if level == 0:
		print('You have escaped 1-1')
		LabelsGeneral.storyLabel.text='You have escaped 1-1'
	
	level = level + 10	
class PTAGVars():
	
	#Tells Whether or not to print the Debug Information to the console or the screen
	DeBuG = True	#	True means that the debug stuff is shown and false means that it isn't.
	
	#Name Creation Variables
	NaMe = []
	NAME = ''
	
	#Global Variables
	playerInventory = []
	player = ['player', 10, False, 10, (1, 1), 1]
	started = False
	playerHealth = 'Player Health: ' + str(player[1])
	playerResistance = 'Resistance: ' + str(player[2])
	playerArmour = 'Player Armour: ' + str(player[3])
	playerLocation = 'Location: ' + str(player[4])
	playerLevel = 'Player Level: ' + str(player[5])
	missionObjective = 'Escape The Room'
	mouseCoords = (0, 0)
	fs = False
	level=0

	found_Stone=False
	doorUnlocked=False
	found_Key=False
	
	#Hidden Variables
	keyPressCount = 0
	
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
	killersSong = '../assets/music/Killers.mp3'
	sandStormRemixSong = '../assets/music/Daude - Sandstorm Jorxelvin Napalm Remix.mp3'
	funLOTRSong = '../assets/music/taking the hobbits to isengard.mp3'
	
	song = [wizardsBattleSong, floatingCitiesSong, rynosThemeSong, clashDefiantSong, edmDetectionModeSong, funLOTRSong, furiousFreakSong, overworldSong, professorUmlautSong, killersSong, sandStormRemixSong]
class newGame():
	def selectDLL():		
		try:
			pyglet.lib.load_library('avbin64')
			pyglet.have_avbin=True
			print("Using avbin64")
		except:#OSError
			pyglet.lib.load_library('avbin')
			pyglet.have_avbin=True
			print('Using avbin')
		
	def setupPlayer():
		player = PTAGVars.player
		playerHealth = PTAGVars.playerHealth
		#This bit is commented out because of a new, on-screen method for creating he character's username.
		#playerName = str(input("What is your player's Name?\n"))
		health = 10
		resistance = False
		armour = 10
		player[0] = ''#playerName
		player[1] = health
		player[2] = resistance
		player[3] = armour
		player[4] = (0, 0, 0)#Location. Change to fit the stating location and the location system
		player[5] =	1
		playerHealth = playerHealth + str(player[1])
		PTAGVars.level=3807
def inBounds(bounds, pointer):
		if pointer[0] <= bounds[2] and pointer[0] >= bounds[0] and pointer[1] <= bounds[1] and pointer[1] >= bounds[3]:
			return(True)
		else:
			return(False)
#Setup the game and music stuffs
newGame.selectDLL()
newGame.setupPlayer()
#Play the music
lastIndex = len(PTAGVars.song)-1
sound = pyglet.media.load(PTAGVars.song[random.randrange(0, lastIndex)])
sound.play()
#Define a folder for the custom fonts
pyglet.font.add_directory('../assets/fonts/')
#Define the main window
window = pyglet.window.Window(caption='Python Text Adventure Game - Room 1.1 - Rv1')
#The different Levels
#This is not quite a level to the game, but it is a level in the way that it has to be set up.
class getUserName():
	instructionLabel = pyglet.text.Label('Please enter your name and then hit enter', font_name='Times New Roman', font_size=10, x=window.width//2, y=(window.height//2)+20, anchor_x='center', anchor_y='center')
	nameLabel = pyglet.text.Label('', font_name='Times New Roman', font_size=20, x=window.width//2, y=(window.width//2)-20, anchor_x='center', anchor_y='center')
	
	def drawNameGet():
		getUserName.instructionLabel.draw()
		getUserName.nameLabel.draw()
#Room One
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
				print('You have escaped 1-1.')
				PTAGVars.level=10
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
		pointer = PTAGVars.mouseCoords
		#Button Bounds:
		bounds = (8, 107, 79, 96)#Top Left, Bottom Right
		if inBounds(bounds, pointer):
			PTAGVars.level=10
	def DrawRoomOne():
		RoomOne_ReturnOne.LeaveRoomButton.draw()
#Hallway One
class HallOne():
	font = PTAGVars.ButtonFont[0]
	size = PTAGVars.ButtonFont[1]
	
	#Buttons
	#Look Around Button
	GoBackButtonLabel = pyglet.text.Label('Go back inside the room', font_name=font, font_size=10, x=10, y=300, anchor_x='left', anchor_y='center')
	def goBack():
		pointer = PTAGVars.mouseCoords
		#Button Bounds:
		bounds = (10, 305, 89, 295)#Top Left, Bottom Right
		if inBounds(bounds, pointer):
			PTAGVars.level = 1
			LabelsGeneral.storyLabel.text='You have been here before. There is nothing to see here'
			print("You have been here before. There is nothing to see here")
			PTAGVars.level=1
	#Try Door Button
	GoToIntersectionButton = pyglet.text.Label('Go to the intersection', font_name=font, font_size=10, x=10, y=270, anchor_x='left', anchor_y='center')
	def goToIntersection():
		pointer = PTAGVars.mouseCoords
		#Button Bounds
		bounds = (10, 275, 131, 265)
		if inBounds(bounds, pointer):
			print("You walk towads the intersection cautiously.")
			LabelsGeneral.storyLabel.text='You walk towads the intersection cautiously.'
			level=20
	def DrawHallOne():
		HallOne.GoBackButtonLabel.draw()
		HallOne.GoToIntersectionButton.draw()
class HallTwo():
	font = PTAGVars.ButtonFont[0]
	size = PTAGVars.ButtonFont[1]
	
	RunLeftLabel = pyglet.text.Label('Run into the office to your left', font_name=font, font_size=size, x=10, y=270, anchor_x='left', anchor_y='center')
	RunRightLabel = pyglet.text.Label('Run into the office to your right', font_name=font, font_size=size, x=10, y=285, anchor_x='left', anchor_y='center')
	FightLabel = pyglet.text.Label('Defend yourself from the soldier', font_name=font, font_size=size, x=10, y=300, anchor_x='left', anchor_y='center')
	
	def fight():
		Level=21
	def runLeft():
		print('You run into the office to your left.')
	def runRight():
		print('You run into the office to your right.')
	def DrawHallTwo():
		HallTwo.RunLeftLabel.draw()
		HallTwo.RunRightLabel.draw()
		HallTwo.FightLabel.draw()		
class LabelsGeneral():
	font = PTAGVars.ButtonFont[0]
	size = PTAGVars.ButtonFont[1]
	#Game Name and Start Button Labels
	GameTitle = pyglet.text.Label("Python Text Adventure Game", font_name=font, font_size=14, x=window.width//2, y=window.width//2, anchor_x='center', anchor_y='top', color=(255,0,0,255))
	StartLabel = pyglet.text.Label("Click to Start", font_name=font, font_size=size, x=(window.width//2)-20, y=(window.width//2)-100, anchor_x='center', anchor_y='center')
	
	#General Game Information Labels
	missionObjectiveLabel = pyglet.text.Label(PTAGVars.missionObjective, font_name='Arial Rounded MT Bold', font_size=10, x=window.width//2 ,y=0, anchor_x='center', anchor_y='bottom')
	storyLabel = pyglet.text.Label('', font_name='Arial', font_size=10, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
	
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
	playerLevelLabel = pyglet.text.Label(PTAGVars.playerLevel, font_name=font, font_size=10, x=window.width, y=(window.height-75), anchor_x='right', anchor_y='top')
	
	def DrawPlayerStats():
		PlayerStats.playerNameLabel.draw()
		PlayerStats.playerHealthLabel.draw()
		PlayerStats.playerResistanceLabel.draw()
		PlayerStats.playerArmourLabel.draw()
		PlayerStats.playerLocationLabel.draw()
		PlayerStats.playerLevelLabel.draw()		
class DebugStuffs():
	#Debug Labels
	pointerClickLocation = pyglet.text.Label('0, 0', font_name='Arial', font_size=10, x=window.width, y=0, anchor_x='right', anchor_y='bottom')
	fps = pyglet.clock.ClockDisplay()
	
	def DrawDebugStuff():
		DebugStuffs.pointerClickLocation.draw()
		DebugStuffs.fps.draw()
def typedName(symbol, modifiers):
	#This is for letters and numbers
	keyCodes = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,32,48,49,50,51,52,53,54,55,56,57,58]
	keyString = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','0','1','2','3','4','5','6','7','8','9']
	enter = 65293
	backspace = 65288
	if not symbol==enter:
		if not symbol==backspace:
			try:
				i = keyCodes.index(symbol)
				if modifiers==17:
					preChar = keyString[i]
					char = preChar.upper()
				else:
					char = keyString[i]
				PTAGVars.NaMe.append(char)
			except ValueError:
				print('', end='')
		if symbol==backspace:
			try:
				last=len(PTAGVars.NaMe)-1
				del(PTAGVars.NaMe[last])
			except IndexError:
				print('', end='')
	if symbol==enter:
		PTAGVars.NAME=''.join(PTAGVars.NaMe)
		if PTAGVars.NaMe[0]=='M' and PTAGVars.NaMe[1]=='c' and PTAGVars.NaMe[2]=='D':
			PTAGVars.player[1] = 3807
			PTAGVars.player[3] = 3807
			PTAGVars.player[5] = 3807
			PlayerStats.playerHealthLabel.draw()
			PlayerStats.playerArmourLabel.draw()
			PlayerStats.playerLevelLabel.draw()
		elif PTAGVars.NAME == "McD":
			PTAGVars.player[1] = 3807
			PTAGVars.player[3] = 3807
			PTAGVars.player[5] = 3807
			PlayerStats.playerHealthLabel.draw()
			PlayerStats.playerArmourLabel.draw()
			PlayerStats.playerLevelLabel.draw()
			
		PTAGVars.player[0] = PTAGVars.NAME
		PlayerStats.playerNameLabel.text=PTAGVars.player[0]
		PTAGVars.level=0
	getUserName.nameLabel.text=''.join(PTAGVars.NaMe)
@window.event
def on_key_press(symbol, modifiers):
	if PTAGVars.level==3807:
		typedName(symbol, modifiers)
	if not PTAGVars.level==3807:
		if not PTAGVars.keyPressCount==100:
			print('Nice! You pressed a button on the keyboard!')
			PTAGVars.keyPressCount = PTAGVars.keyPressCount + 1
			print(symbol)
			print(modifiers)
		else:
			print('Stop Pressing Buttons!!!')
@window.event
def on_mouse_press(x, y, button, modifiers):
	PTAGVars.mouseCoords = (x, y)
	Level=PTAGVars.level
	if not Level==3807:
		pressToStart()
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
	elif Level==10:
		HallOne.goToIntersection()
		HallOne.goBack()
	elif Level==20:
		HallTwo.null
		
	loc = [str(x), str(y)]
	pointerLoc = ','.join(loc)
	DebugStuffs.pointerClickLocation.text=pointerLoc	
@window.event
def on_draw():
	level = PTAGVars.level
	window.clear()#	Clear the display
	if not level==3807:
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
		RoomOne_ReturnOne.DrawRoomOne()
	elif level==10:
		HallOne.DrawHallOne()
	elif level==20:
		HallTwo.DrawHallTwo()
	elif level==3807:
		getUserName.drawNameGet()
	
pyglet.app.run()
sys.exit(0)
