'''
Version 1.0

By Payton J.

'''
from random import seed
from random import randint
import time

floor0 = ['empty', 'sword', 'stairs up', 'monster', 'empty']
floor1 = ['magic stones', 'monster', 'stairs down', 'empty', 'stairs up']
floor2 = ['prize', 'boss monster', 'sword', 'sword', 'stairs down']
inventory = []
currentFloor = 0
currentRoom = 0

gameState = 'ongoing'

while gameState == 'ongoing':
  
  if currentFloor == 0:
    
    floor = floor0
    room = floor[currentRoom]
  
  elif currentFloor == 1:
    floor = floor1
    room = floor[currentRoom]
 
  else:
    floor = floor2
  room = floor[currentRoom]
  
  
  if room == 'empty':
    print('You are in an empty room.')
    
    
  elif room == 'prize':
    print("Wowww you made it to the treasure")
    print("ʕつ ͡◔ ᴥ ͡◔ʔつ")
    time.sleep(1)
    print("You win the game!")
    gameState = 'won'
    exit()
     
    
  elif room == 'boss monster':
    print("☉_☉")
    time.sleep(1)
    print("IDK bout this one man he is an absolute unit")
    
    
  elif room == 'sword':
    print("nice a weapon, this will be useful")
    
    
  elif room == 'stairs down':
    print("I can go down these stairs")
    
    
  elif room == 'stairs up':
    print("I can go up these stairs")
    
    
  elif room == 'monster':
    print("thats a spooky boi")
    
    
  elif room == 'magic stones':
    print("Nice, glowing rocks")
  
  choice = input('Command? ')

  
  if choice == 'help':
   
    pass 
  
  
  elif choice == 'left':
  
    if currentRoom <= 0:
      print("thats a wall dummy")
    
    elif currentRoom == ('monster') or ('boss monster'):
      print("YOUUUUU DIEEEDDDDDDDDDDDD")
      print("game over")
      exit()
    else:
      currentRoom = (currentRoom - 1)
       
   
    
  elif choice == 'right':
    if currentRoom > 3:
      print("thats a wall dummy")
    else:
      currentRoom = (currentRoom + 1)
    

   
    
  elif choice == 'up':
    if room == ('stairs up'):
      currentFloor + 1
      currentFloor = (currentFloor + 1)
    else:
      print("you cant go through a ceiling dummy")
    
    
    
    
    
    
  elif choice == 'down':
    if room == ('stairs down'):
      currentFloor - 1
      currentFloor = (currentFloor - 1)
    else:
      print("There are no stairs to go down!")
    
    
    
    
    
    
  elif choice == 'grab':
    if room == 'sword':
      inventory.append ('sword')
      floor[currentRoom] = ('empty')
      print("your man bag contains", inventory)
    elif room == 'magic stones':
      inventory.append ('magic stones')
      print("your man bag contains", inventory)
    
  elif choice == 'fight':
    if ('sword') in inventory and room == ('monster'):
      print("(¬_¬)")
      time.sleep(1)
      print("you have slain a monster")
      inventory.remove ('sword')
      floor[currentRoom] = ('empty')
    elif 'magic stones' in inventory and 'sword' in inventory and room == ('boss monster'):
      print("ヾ( ･`⌓´･)ﾉﾞ")
      time.sleep(1)
      print("ヽ(#`Д´)ﾉ")
      time.sleep(1)
      print("୧༼ಠ益ಠ༽୨")
      time.sleep(1)
      print("ᕙ( ︡’︡益’︠)ง")
      time.sleep(1)
      print("YOU HAVE DEFEATED THE BOSS")
      inventory.remove ('magic stones')
      floor[currentRoom] = ('empty')
    else:
      print("YOUUUUU DIEEDDDD")
      time.sleep(.5)
      print("game over")
      exit() 
    
    pass
  else:
    print('Command not recognized. Type "help" to see all commands.')
    
    
  

if gameState == 'won':
  print('You won the game! :)')
else:
  print('You lost the game. :( Maybe next time.')
