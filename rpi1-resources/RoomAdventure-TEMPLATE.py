###########################################################################################
# Name: Aiden Thomas and Deion Davis
# Date:  4/19/2024
# Description: This program is a text-based adventure game that allows the player to move through 5 rooms.(make sure you find that snake)
###########################################################################################
from tkinter import *

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room:
	# the constructor
	def __init__(self, name, image, unlocked = False):
		# rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
		# (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
		# and grabbables (things that can be taken into inventory)
		self.name = name
		self.image = image
		self.exits = {}
		self.items = {}
		self.grabbables = []
		self.unlocked = unlocked
		self.itemGrabPairs = {
			"key": "table",
			"book-lever": "bookshelf",
			"lock": "desk",
			"snake": "painting"

		}
		self.itemLocks = {}

	# getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, value):
		self._image = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	@property
	def unlocked(self):
		return self._unlocked
	
	@unlocked.setter
	def unlocked(self, value):
		self._unlocked = value

	@property
	def itemGrabPairs(self):
		return self._itemGrabPairs
	
	@itemGrabPairs.setter
	def itemGrabPairs(self, value):
		self._itemGrabPairs = value	
	
	@property
	def itemLocks(self):
		return self._itemLocks
	
	@itemLocks.setter
	def itemLocks(self, value):
		self._itemLocks = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate dictionary
		self._exits[exit] = room

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc, state):
		# append the item and description to the appropriate dictionary
		self._items[item] = desc
		self._itemLocks[item] = state

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item):
		# append the item to the list
		self._grabbables.append(item)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):
		# remove the item from the list
		self._grabbables.remove(item)

	# returns a string description of the room
	def __str__(self):
		# first, the room name
		s = "You are in {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items.keys():
			s += item + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits.keys():
			s += exit + " "

		return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
	# the constructor
	def __init__(self, parent):
		# call the constructor in the superclass
		Frame.__init__(self, parent)

	# creates the rooms
	def createRooms(self):
		# r1 through r4 are the four rooms in the mansion
		# currentRoom is the room the player is currently in (which can be one of r1 through r4)
		# since it needs to be changed in the main part of the program, it must be global
		global currentRoom

		r1 = Room("Room 1", "images/room1.gif")
		r2 = Room("Room 2", "images/room2.gif")
		r3 = Room("Room 3", "images/room3.gif")
		r4 = Room("Room 4", "images/room4.gif",)
		r5 = Room("Trapdoor", "images/skull.gif")
		r6 = Room("Room 5", "images/room7.gif")
		r7 = Room("Room", "images/room7.gif")

		# add exits to rooms 1
		r1.addExit("east", r2)
		r1.addExit("south", r3)

		# add items to room 1
		r1.addItem("table", "It is made of oak. A golden key rests on it.", True)
		r1.addItem("chair", "It is made of wicker.", True)
		r1.addItem("fireplace", "It is made of brick.", False)

		# add grabbables to room 1
		r1.addGrabbable("key")

		# add exits to room 2
		r2.addExit("west", r1)
		r2.addExit("south", r4)

		# add items to room 2
		r2.addItem("rug", "It is woven and quite large.", False)
		r2.addItem("fireplace", "It is made of marble.", False)
		r2.addItem("bookshelf", "The shelves are filled with dusty books.", True)

		# add grabbables to room 2
		r2.addGrabbable("book-lever")

		# add exits to room 3
		r3.addExit("north", r1)
		r3.addExit("east", r4)
		r3.addExit("down", r5)  # add exit for trapdoor


		# add items to room 3
		r3.addItem("desk", "It is made of oak.", True)
		r3.addItem("papers", "Written on hurredly, these texts speak of a path for the worthy serpents.", True)
		r3.addItem("Trapdoor", "It is locked with a golden lock.", False)


		# add grabbables to room 3
		r3.addGrabbable("lock")

		# add exits to room 4
		r4.addExit("north", r2)
		r4.addExit("west", r3)

		# add items to room 4
		r4.addItem("bed", "It is made with gold.", True)
		r4.addItem("painting", "It depicts a giant snake", False)
		r4.addItem("dresser", "It is made of marble.", True)

		# add grabbables to room 4
		r4.addGrabbable("snake")

		# add exits to room 6 (this room is south of room 4, so there's only 1 exit for now)
		r6.addExit("north", r4)

		# add items to room 6
		r6.addItem("table", "It's a fancy looking table filled with empty plates and expensive looking utensils.", True)
		r6.addItem("rug", "The rug is red and filled with random patterns", True)
		r6.addItem("plate", "This looks expensive, you might be able to sell this for a lot of money..", False)

		# add grabbables to room 6
		r6.addGrabbable("plate")

		# add exits to room 7 (only one exit because this room is directly south of room 6)
		r7.addExit("north", r6)

		# add items to room 7
		r7.addItem("book", "There's nothing in it besides one page but it's ripped in half, it says 'WATCH OUT FOR TRA...", False)
		r7.addItem("sculpture", "Sculpture of an angel, there's two others like this in the room.", True)
		r7.addItem("bookshelves", "This bookshelf is filled with books and it stretches up to the ceiling of the room.", True)

		# add grabbables to room 7
		r7.addGrabbable("book")
		
		# set room 1 as the current room at the beginning of the game
		Game.currentRoom = r1

		# initialize the player's inventory
		Game.inventory = []


		# usable and usable pairs
		Game.usables = {}
		Game.usablePairs = {
			"key": "lock",
			"book-lever": "bookshelf",
			"snake": "painting"
		}


		# item grab pairs
		
		Game.itemGrabPairs = {
			"key": "table",
			"book-lever": "bookshelf",
			"lock": "desk",
			"snake": "painting"
		}

		#Score
		Game.score = 0

			 

		


	# sets up the GUI
	def setupGUI(self):
		# organize the GUI
		self.pack(fill=BOTH, expand=1)

		# setup the player input at the bottom of the GUI
		# the widget is a Tkinter Entry
		# set its background to white and bind the return key to the function process in the class
		# push it to the bottom of the GUI and let it fill horizontally
		self.entry = Entry(self, bg="white")
		self.entry.bind("<Return>", self.process)
		self.entry.pack(side=BOTTOM, fill=X)

		# setup the image to the left of the GUI
		# the widget is a Tkinter Label
		# don't let the image control the widget's size
		img = None
		self.image = Label(self, width=WIDTH // 2, image=img)
		self.image.image = img
		self.image.pack(side=LEFT, fill=Y)
		self.image.pack_propagate(False)

		# setup the text to the right of the GUI
		# first, the frame in which the text will be placed
		text_frame = Frame(self, width=WIDTH // 2)
		# the widget is a Tkinter Text
		# disable it by default
		# don't let the widget control the frame's size
		self.text = Text(text_frame, bg="lightgrey", state=DISABLED)
		self.text.pack(fill=Y, expand=1)
		text_frame.pack(side=RIGHT, fill=Y)
		text_frame.pack_propagate(False)


	# sets the current room image
	def setRoomImage(self):
		if (Game.currentRoom.name == "Trapdoor"):
			# Check if the snake is in the player's inventory
			if "snake" in Game.inventory:
            	# Display the "Win.gif" image
				img = PhotoImage(file="images/Win.gif")
			else:	
				# Display the "skull.gif" image
				img = PhotoImage(file="images/skull.gif")
		else:
			img = PhotoImage(file=Game.currentRoom.image)
		self.image.config(image=img)
		self.image.image = img


	# sets the status displayed on the right of the GUI
	def setStatus(self, status):
		# enable the text widget, clear it, set it, and disable it
		self.text.config(state=NORMAL)
		self.text.delete("1.0", END)

		if (self.currentRoom == "Trapdoor"):
			self.text.insert(END, "You have fallen into the trapdoor! You have died!")
			self.text.config(state=DISABLED)
			return
		elif (self.currentRoom == "Room 4" and "snake" in Game.inventory):
			self.text.insert(END, "You have successfully escaped the mansion with the snake!")
			self.text.config(state=DISABLED)
			return	
		else:
			self.text.insert(END, str(Game.currentRoom) + "\nYou are carrying: "+ str(self.inventory) + "\n" + status)
		self.text.config(state=DISABLED)

	# plays the game
	def play(self):
		
		# add the rooms to the game
		self.createRooms()
		# configure the GUI
		self.setupGUI()
		# set the current room
		self.setRoomImage()
		# set the current status
		self.setStatus("")

		# processes the player's input
	def process(self, event):
		# grab the player's input from the input at the bottom of the GUI
		action = self.entry.get()
		# set the user's input to lowercase to make it easier to compare the verb and noun to known values
		action = action.lower()
		# set a default response
		response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
		# exit the game if the player wants to leave (supports quit, exit, and bye)
		if (action == "quit" or action == "exit" or action == "bye"):
			exit(0)
		# if the player is dead
		if (Game.currentRoom.name == "Trapdoor"):
			self.setStatus(response)
			return
		# split the user input into words (words are separated by spaces)
		words = action.split()
		# the game only understands two word inputs
		if(len(words) == 2):
			# isolate the verb and noun
			verb = words[0]
			noun = words[1]
			# the verb is go
			if (verb == "go"):
				# set a default response
				response = "Invalid exit."
				# check for valid exits in the current room
				if (noun in Game.currentRoom.exits):
					if noun == "down" and Game.currentRoom.name == "Room 3":
						# If the player is trying to go to the trapdoor room
						if "key" not in Game.inventory:
							response = "You can't enter the trapdoor room without the key in your inventory."
						else:
							# Allow the player to move to the trapdoor room
							Game.currentRoom = Game.currentRoom.exits[noun]
							response = "Room changed."
							if "snake" in Game.inventory:
								response = "Congratulations! You have successfully escaped the mansion with the snake! You win!"
					# if one is found, change the current room to the one that is associated with the specified exit
					else:
						Game.currentRoom = Game.currentRoom.exits[noun]
						# set the response (success)
						response = "Room changed."
				# set the room image
				self.setRoomImage()
				# set the status
				self.setStatus(response)
				return
			# the verb is look
			if (verb == "look"):
				# set a default response
				response = "I don't see that item."
				# check for valid items in the current room
				if (noun in Game.currentRoom.items):
					# if one is found, set the response to the item's description
					response = Game.currentRoom.items[noun]
				# set the status
				self.setStatus(response)
				return
			# the verb is take
			if (verb == "take"):
				# set a default response
				response = "I don't see that item."
				# check for valid grabbable items in the current room
				if (noun in Game.currentRoom.grabbables):
					# if one is found, move it to the player's inventory
					Game.inventory.append(noun)
					# set the response (success)
					response = "Item grabbed."
					# remove the item from the room
					Game.currentRoom.delGrabbable(noun)
				# set the status
				self.setStatus(response)
				return
			# the verb is use
			if (verb == "use"):
				# set a default response
				response = "I don't see that item."
				# check for valid items in the player's inventory
				if (noun in Game.inventory):
					# if one is found, set the response to the item's description
					response = Game.currentRoom.items[noun]
				# set the status
				self.setStatus(response)
				return

'''
	# processes the player's input
	def process(self, event):
		# grab the player's input from the input at the bottom of the GUI
		action = self.entry.get()
		# set the user's input to lowercase to make it easier to compare the verb and noun to known values
		action = action.lower()
		# set a default response
		response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
		# exit the game if the player wants to leave (supports quit, exit, and bye)
		if (action == "quit" or action == "exit" or action == "bye"):
			exit(0)
		# if the player is dead
		if (Game.currentRoom == "Trapdoor"):
			self.setStatus(response)
			return
		# split the user input into words (words are separated by spaces)
		words = action.split()
		# the game only understands two word inputs
		if(len(words) == 2):
			# isolate the verb and noun
			verb = words[0]
			noun = words[1]
			# the verb is go
			if (verb == "go"):
				# set a default response
				response = "Invalid exit."
				# check for valid exits in the current room
				if (noun in Game.currentRoom.exits):
					if noun == "down" and Game.currentRoom == "Room 3":
						# If the player is trying to go to the trapdoor room
						if "key" not in Game.inventory:
							response = "You can't enter the trapdoor room without the key in your inventory."
						else:
                        	# Allow the player to move to the trapdoor room
							Game.currentRoom = Game.currentRoom.exits[noun]
							response = "Room changed."
							if "snake" in Game.inventory:
								response = "Congratulations! You have successfully escaped the mansion with the snake! You win!"
					# if one is found, change the current room to the one that is associated with the specified exit
					else:
						Game.currentRoom = Game.currentRoom.exits[noun]
						# set the response (success)
						response = "Room changed."
				# set the room image
				self.setRoomImage()
				# set the status
				self.setStatus(response)
				return
			# the verb is look
			if (verb == "look"):
				# set a default response
				response = "I don't see that item."
				# check for valid items in the current room
				if (noun in Game.currentRoom.items):
					# if one is found, set the response to the item's description
					response = Game.currentRoom.items[noun]
				# set the status
				self.setStatus(response)
				return
			# the verb is take
			if (verb == "take"):
				# set a default response
				response = "I don't see that item."
				# check for valid grabbable items in the current room
				if (noun in Game.currentRoom.grabbables):
					# if one is found, move it to the player's inventory
					Game.inventory.append(noun)
					# set the response (success)
					response = "Item grabbed."
					# remove the item from the room
					Game.currentRoom.delGrabbable(noun)
				# set the status
				self.setStatus(response)
				return
			# the verb is use
			if (verb == "use"):
				# set a default response
				response = "I don't see that item."
				# check for valid items in the player's inventory
				if (noun in Game.inventory):
					# if one is found, set the response to the item's description
					response = Game.currentRoom.items[noun]
				# set the status
				self.setStatus(response)
				return

'''
##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
