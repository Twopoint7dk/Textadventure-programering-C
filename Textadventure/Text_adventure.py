from Rooms import *

inventory={}

def show_room(room_num):
    """Display the contents of the given room.
    Input:
    - room_num : int, the number of the room to show.
    """
    rooms = {
        0: show_room_0,
        1: show_room_1,
        2: show_room_2,
        3: show_room_3,
        4: show_room_4,
        5: show_room_5
    }
    if room_num in rooms:
        rooms[room_num]()
    else:
        print("You are out of bounds. Room", room_num, "does not exist.")

def loot_form_room_2(current_room, user_input):
    global inventory
    while current_room == 2:
        if user_input == "take the torch":
            inventory.append("torch")
            

def move_from_room_0(direction):
    if direction == "west":
        return 1

def move_from_room_1(direction):
    if direction == "north":
        return 2
    if direction == "west":
        return 3
    if direction == "east":
        return 0

def move_from_room_2(direction):
    if direction == "south":
        return 1

def move_from_room_3(direction):
    if direction == "south":
        return 4
    if direction == "east":
        return 1

def move_from_room_4(direction):
    if direction == "north":
        return 3

def move_from_room(current_room, direction):
    new_room = current_room
    if current_room == 0:
         new_room = move_from_room_0(direction)
    if current_room == 1:
         new_room = move_from_room_1(direction)
    if current_room == 2:
         new_room = move_from_room_2(direction)
    if current_room == 3:
         new_room = move_from_room_3(direction)
    if current_room == 4:
         new_room = move_from_room_4(direction)
    return new_room

def game_loop():
    """Main loop of the game - this is where the fun happens."""

    # We start in room 0
    current_room = 0

    # Display the room that we start in
    show_room(current_room)

    # Enter the main loop, where the user can input commands.
    while True:
        user_inp = input("> ")
        move_command_strip = user_inp[5:]

        if user_inp == "quit":
            break
        elif user_inp[:4] == "move":
            current_room = move_from_room(current_room,user_inp[5:])
        elif user_inp[:11] == "look around":
            show_room(current_room)
        elif user_inp[:9] =="inventory":
            print(inventory)
        else:
            print("I do not understand the command:", user_inp)
       

game_loop()