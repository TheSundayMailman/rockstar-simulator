import random
from rockstar import Rockstar



# graphics
car = """
               __       .          
    __       ~( @\      |\         
 __/__\________]_[______| \_       
|   ___   |         ,|   ___`-.    
|  /   \  | _________/  /   \  `-. 
|_| (O) |______________| (O) |____|
   \___/                \___/
"""

deranged = """
      .........
   .::::::::::::::.  
 .::'   ''''''   '::. 
 :::              ::: 
 ::'              ':: 
: : /~~~~'  '~~~~\ : :
:(:   |       |    :):
'.:      /  \      :.'
 ':     (.  .)     :' 
  '.  .::::::::.  .'
   :   <------>   :   
   '.  ~::::::~  .'
     '.   ''   .'     
       ''''''''"""

shady = """
   .------\ /------.
   |       -       |
   |               |
   |               |
   |               |
_______________________
===========.===========
  / ~~~~~     ~~~~~ \ 
 /|     |     |\    |\ 
 W   ---  / \  ---   W
 \.      |o o|      ./
  |                 |
  \    #########    /
   \  ## ----- ##  /
    \##         ##/
     \_____v_____/"""



# handles all encounters that can happen to player
def encounter_death(player):
  encount = random.randint(1, 100)
  if encount < int(player.popularity / 5):
    player.game_over()

def encounter_impulse(player):
  encount = random.randint(1, 100)
  if encount < int(player.popularity / 5):
    print("\n{} impulsively bought a fancy sports car because {} was bored and\nhad too much cash...Not the wisest move, but it made for some good PR news.".format(player.name, player.pronoun))
    print(car)
    player.buy_car()



# handles all fan events
def encounter_fan(player, running):
  encount = random.randint(1, 100)
  if encount < int(player.popularity / 5):
    unresolved = True
    while running and unresolved:
      print("\nDuring a concert, a crazy deranged fan approaches {} and causes a scene!".format(player.name))
      print(deranged)
      cmd = input("What should {} do? Options: 'punch', 'run', or 'call security'\n".format(player.pronoun)).lower()
      if cmd == "quit":
        running = False
      elif cmd == "punch":
        print("\nBOOOOM! {} surpressed the deranged fan as {} other fans cheered on. It\ncosts some money to repair {} image but it was worth it.".format(player.name, player.posessive, player.posessive))
        player.punch_fan()
        unresolved = False
      elif cmd == "run":
        print("\n{} found some cover! But {} fans are disappointed...".format(player.name, player.posessive))
        player.run_from_fan()
        unresolved = False
      elif cmd == "call security":
        print("\nNicely handled! Concert continued as normal!")
        player.call_security()
        unresolved = False
      else:
        print("Please type in a valid command...\n")
  return running



# handles all producer events
def encounter_producer(player, running):
  encount = random.randint(1, 100)
  if encount < int(player.popularity / 5):
    unresolved = True
    while running and unresolved:
      print("\nSome creepy producer pitches a shady-sounding record deal to {}...".format(player.name))
      print(shady)
      cmd = input("What should {} do? Options: 'punch', 'deal', or 'no deal'\n".format(player.pronoun)).lower()
      if cmd == "quit":
        running = False
      elif cmd == "punch":
        print("\nBOOOOM! The producer sued {} a sizable sum of money,\nbut {} won the heart of your fans!".format(player.name, player.pronoun))
        player.punch_producer()
        unresolved = False
      elif cmd == "deal":
        print("\n{} made some good money from this deal, but {} left some fans\nconcerned over {} dubious motives...".format(player.name, player.pronoun, player.posessive))
        player.engage_producer()
        unresolved = False
      elif cmd == "no deal":
        print("\nGreat choice! But the shady producer spread some nasty\nrumors about {} out of spite...".format(player.name))
        player.disengage_producer()
        unresolved = False
      else:
        print("Please type in a valid command...\n")
  return running
