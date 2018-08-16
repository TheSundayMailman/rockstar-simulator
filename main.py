from rockstar import Rockstar

def rockstar_sim():
  # print("{} has ran.".format(rockstar_sim.__name__))

  intro = """
 (       )           ) (                 (      (   (      *    
 )\ ) ( /(   (    ( /( )\ ) *   )  (     )\ )   )\ ))\ ) (  `   
(()/( )\())  )\   )\()(()/` )  /(  )\   (()/(  (()/(()/( )\))(  
 /(_)((_)\ (((_)|((_)\ /(_)( )(_)(((_)(  /(_))  /(_)/(_)((_)()\ 
(_))   ((_))\___|_ ((_(_))(_(_()))\ _ )\(_))   (_))(_)) (_()((_)
| _ \ / _ ((/ __| |/ // __|_   _|(_)_\(_| _ \  / __|_ _||  \/  |
|   /| (_) | (__  ' < \__ \ | |   / _ \ |   /  \__ \| | | |\/| |
|_|_\ \___/ \___|_|\_\|___/ |_|  /_/ \_\|_|_\  |___|___||_|  |_|

Welcome to Rockstar Simulator 1.0!
Play as a rockstar! Manage your career for 12 months!
Be remembered as a rock legend! Or party too hard and die...
  """

  hint = """
Every month, your rockstar can either 'tour', 'rest', or 'party'.
> Touring will use energy but you can earn some cash based on popularity.
> Resting will lower popularity, but you can regain more energy for tours.
> Partying uses cash, but can boost popularity and energy.

Rockstars beware!
Partying too hard while you are too popular might have devasting effects...
  """

  divider = "\n==========================================================================="

  print(intro)
  print(divider)

  name = input("Start by giving your rockstar a name!\n")
  while len(name) < 4 or len(name) > 30:
    name = input("\nPlease enter a name between 4 to 30 letters long...\n")
  
  gender = input("\nIs your rockstar a male or female?\n").lower()
  while gender != "male" and gender != "female":
    gender = input("\nPlease enter either 'male' or 'female'...\n").lower()

  # initialize player character
  player = Rockstar(name, gender)

  print(hint)
  print(divider)
  print("\nYour rockstar will named {}! May {} career be successful...".format(player.name, player.posessive))
  player.show_status()

  # start of game loop
  running = True
  months = 0

  while running and player.alive and months < 12:
    cmd = input("{} of 12 months have passed. What will {} do next?\nType 'help' for help, or 'quit' to exit.\n".format(months, player.name)).lower()
    if cmd == "quit" or cmd == "exit":
      running = False
    elif cmd == "tour":
      print(divider)
      player.tour()
      months += 1
    elif cmd == "rest":
      print(divider)
      player.rest()
      months += 1
    elif cmd == "party":
      print(divider)
      player.party()
      months += 1
    elif cmd == "help":
      print(divider)
      print(hint)
    else:
      print(divider)
      print("\nPlease type in a valid command...\n")



rockstar_sim()

print("\nThanks for playing!\n")
