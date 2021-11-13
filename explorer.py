import time
from os import system, name
CurrentArea = ''
Inventory = []
TakenKey = False

def Ask(Areas):
    print('Available areas to go:')
    for i in Areas:
        time.sleep(0.1)
        print(i)

    Destination = input('Where do you go?: ')
    Destination = Destination.lower()
    if Destination == 'inventory':
        if len(Inventory) == 0:
            print('There is nothing in your inventory.')
        else:
            print('Your inventory:')
            for i in Inventory:
                time.sleep(0.1)
                print(i)

        Destination = Ask(Areas)

    return Destination

def Go(Areas):
    Destination = Ask(Areas)

    if Destination in Areas:
        Destination = Areas.index(Destination)
    else:
        Destination = Go(Areas)
        Destination = Areas.index(Destination)

    return Areas[Destination]

def Hallway():
    print('You walk into the hallway, there is nothing here except a door.')
    time.sleep(1)

    Areas = []
    Areas.append('go into room')
    Areas.append('go back')

    CurrentArea = Go(Areas)

    if CurrentArea == 'go into room':
        print('The room has a broken chair.')

        Areas = []
        if 'chair leg' not in Inventory:
            print('Take a chair leg?')
            Areas.append('take a leg')
        Areas.append('go back.')

        CurrentArea = Go(Areas)

        if CurrentArea == 'take a leg':
            Inventory.append('chair leg')
            print('Gained chair leg. You leave the room.')
            print('Type inventory anytime to check your inventory.')
            Hallway()
        elif CurrentArea == 'go back':
            Hallway()
    elif CurrentArea == 'go back':
            Start()

def Basement():
    print('You enter the basement. The door slowly opens.')

    time.sleep(1)
    Areas = []
    Areas.append('further down')
    Areas.append('go back')

    CurrentArea = Go(Areas)

    if CurrentArea == 'go back':
        Start()
    elif CurrentArea == 'further down':
        Areas = []


        Areas.append('go back')
        print('You are now in the basement. You see a chest.')
        if not 'note' in Inventory:
            if 'key' in Inventory:
                Areas.append('use key on chest')
                print('The chest requires a key.')

        CurrentArea = Go(Areas)

        if CurrentArea == 'go back':
            Basement()
        elif CurrentArea == 'use key on chest':
            Inventory.remove('key')
            print('Key was used on chest.')
            print('The chest opens. There is a note inside. Take note?')

            Areas = []
            Areas.append('take note')
            Areas.append('leave note')
            CurrentArea = Go(Areas)

            if CurrentArea == 'take note':
                print('You take the note and go back upstairs.')
                Inventory.append('note')

                print('Type inventory anytime to check your inventory.')
                Basement()
        else:
            Basement()

def Forwards():
    Thought = False
    print('You walk forwards. Time starts to slow down. You feel like you are falling, but nothing has fell.')

    time.sleep(3)
    print('You walk for several hours. You finally reach a point where you can see light.')

    time.sleep(1)
    Areas = []
    Areas.append('keep walking')
    Areas.append('stop to think')
    Areas.append('rest')

    CurrentArea = Go(Areas)

    if CurrentArea == 'rest':
        print('You rest for a sec.')
        time.sleep(10)
        print('Okay lets continue.')
        time.sleep(.5)
        Forwards()
    elif CurrentArea == 'stop to think':
        if Thought == False:
            Thought = True
            print('You stop to think.')
            time.sleep(1)
            print("'Why am I even here in the first place?' you said to yourself.")
            time.sleep(1)
            print("'What's stopping me fron leaving right now?'")
            time.sleep(3)
            print('...')
            time.sleep(1)
            print('You decide its best to see for yourself.')
            time.sleep(2)
            Forwards()
        else:
            print('But you have already thought.')
            time.sleep(2)
            Forwards()
    elif CurrentArea == 'keep walking':
        print('You walk forwards into the light.')
        time.sleep(2)
        print('Everything turns to white. You close your eyes and wake up in a hospital')
        time.sleep(4)
        print('...there is a broken chair.')
        time.sleep(5)
        if name == 'nt':
            system('cls')
        else:
            system('clear')


def HiddenArea():
    print('You slowly walk in and the hidden wall slams down. There is no backing now.')

    time.sleep(1)
    Areas = []
    Areas.append('tap wall to activate button')
    Areas.append('forwards')
    Areas.append('sit for a bit')

    CurrentArea = Go(Areas)

    if CurrentArea == 'tap wall to activate button':
        print('You tap the wall. Nothing happens.')

        time.sleep(2)
        HiddenArea()
    elif CurrentArea == 'sit for a bit':
        print('You sit down and rest for a sec.')

        time.sleep(10)
        print('Okay lets continue.')
        time.sleep(.5)
        HiddenArea()
    elif CurrentArea == 'forwards':
        Forwards()

def Start():
    Areas = []
    Areas.append('upstairs')
    Areas.append('hallway')
    Areas.append('basement')

    print('You are in an entrance of a building. The stairway to the basement is on your left, the stairs on your right and a hallway entrance in front of you. Where do you go?')

    time.sleep(1)
    if 'note' in Inventory:
        print('A hidden wall suddenly lifts.')
        Areas.append('hidden area')
    CurrentArea = Go(Areas)
    if CurrentArea == 'basement':
        Basement()
    elif CurrentArea == 'hidden area':
        HiddenArea()
    elif CurrentArea == 'hallway':
        Hallway()
    elif CurrentArea == 'upstairs':
        print('You slowly go up the stairs. You arrive on the first floor of this building.')

        Areas = []
        print('There is a table with a key up here.')
        Areas.append('take key')
        Areas.append('go downstairs')

        CurrentArea = Go(Areas)

        if CurrentArea == 'take key':
            print('You take the key and go downstairs.')
            print('Type inventory anytime to check your inventory.')
            if 'key' in Inventory:
                print('wait you already have a key')
            else:
                TakenKey = True
                Inventory.append('key')

            Start()
        elif CurrentArea == 'go downstairs':
            Start()

Start()

