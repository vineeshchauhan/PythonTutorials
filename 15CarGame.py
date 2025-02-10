state = False
while True:
    entered = input('>')
    if entered == 'help':
        print(''''start - to start the car'
'stop - to stop the car'
'quit - to exit' ''')
    elif entered == 'start':
          if state is not True:
            state = True
            print('Car Started...Ready to go!')
          elif state is True:
            print('Car already started')
    elif entered == 'stop':
        if state is not False:
            state = False
            print('Car Stopped!')
        elif state is False:
            print('Car is already stopped')
    elif entered == 'quit':
        print('Exit the game')
        break
    else:
        print('Unexpected Input')




