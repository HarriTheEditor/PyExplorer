CurrentArea = ''
Inventory = []

def Ask(Areas):
    print('Available areas to go:')
    for i in Areas:
        print(i)
        
    Destination = input('Where do you go?: ')
    Destination = Destination.lower()
    if Destination == 'inventory':
        if len(Inventory) == 0:
            print('There is nothing in your inventory.')
        else:
            print('Your inventory:')
            for i in Inventory:
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
    
    Areas = []
    Areas.append('go into room')
    Areas.append('go back')

    CurrentArea = Go(Areas)

    if CurrentArea == 'go into room':
        print('The room has a broken chair. Take one of the legs of the chair?')

        Areas = []
        Areas.append('take a leg')
        Areas.append('go back.')

        CurrentArea = Go(Areas)

        if CurrentArea == 'take a leg':
            Inventory.append('chair leg')
            print('Gained chair leg. You leave the room.')
            Hallway()
        elif CurrentArea == 'go back':
            Hallway()
    elif CurrentArea == 'go back':
            Start()
    
def Basement():
    print('You enter the basement. The door slowly opens.')

    Areas = []
    Areas.append('further down')
    Areas.append('go back')

    CurrentArea = Go(Areas)

    if CurrentArea == 'go back':
        Start()
    elif CurrentArea == 'further down':
        Areas = []

        if 'key' in Inventory:
            Areas.append('use key on chest')
        Areas.append('go back')
        print('You are now in the basement. You see a chest. It requires a key.')

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
                print('You take the note.')
                print('Note was added to inventory. Type inventory anytime to check.')
        else:
            Basement()
                
            

def Start():
    Areas = []
    Areas.append('upstairs')
    Areas.append('hallway')
    Areas.append('basement')

    print('You are in an entrance of a building. The stairway to the basement is on your left, the stairs on your right and a hallway entrance in front of you. Where do you go?')
    CurrentArea = Go(Areas)
    if CurrentArea == 'basement':
        Basement()
    elif CurrentArea == 'hallway':
        Hallway()
    elif CurrentArea == 'upstairs':
        print('You slowly go up the stairs. You arrive on the first floor of this building. There is a table with a key up here.')

        Areas = []
        Areas.append('take key')
        Areas.append('go downstairs')

        CurrentArea = Go(Areas)

        if CurrentArea == 'take key':
            print('You take the key and go downstairs.')
            Inventory.append('key')

            Start()
        elif CurrentArea == 'go downstairs':
            Start()

Start()

