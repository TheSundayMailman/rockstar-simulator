from rockstar import Rockstar

def rockstar_sim():
  # print("{} has ran.".format(rockstar_sim.__name__))
  print("""
 (       )           ) (                 (      (   (      *    
 )\ ) ( /(   (    ( /( )\ ) *   )  (     )\ )   )\ ))\ ) (  `   
(()/( )\())  )\   )\()(()/` )  /(  )\   (()/(  (()/(()/( )\))(  
 /(_)((_)\ (((_)|((_)\ /(_)( )(_)(((_)(  /(_))  /(_)/(_)((_)()\ 
(_))   ((_))\___|_ ((_(_))(_(_()))\ _ )\(_))   (_))(_)) (_()((_)
| _ \ / _ ((/ __| |/ // __|_   _|(_)_\(_| _ \  / __|_ _||  \/  |
|   /| (_) | (__  ' < \__ \ | |   / _ \ |   /  \__ \| | | |\/| |
|_|_\ \___/ \___|_|\_\|___/ |_|  /_/ \_\|_|_\  |___|___||_|  |_|

Welcome to Rockstar Simulator 1.0!
Play as a rockstar! Manage your career for a few years!
Be remembered as a rock legend! Or party too hard and die...
  """)

  name = input("Start by giving your rockstar a name!\n")
  while len(name) < 4 or len(name) > 30:
    name = input("\nPlease enter a name between 4 to 30 letters long...\n")
  
  gender = input("\nIs your rockstart a male or female?\n").lower()
  while gender != "male" and gender != "female":
    gender = input("\nPlease enter either 'male' or 'female'...\n").lower()
  
  print("\nYour {} rockstar will named {}!\n".format(gender, name))

  running = True
  alive = True
  months = 1

  while running and alive and months < 12:
    cmd = input("{} month(s) have passed. Type 'help' for help, or 'quit' to exit.\n".format(months)).lower()
    if cmd == "help":
      print("""
In this coming month, your rockstar can either 'tour', 'rest', or 'party'.
> Touring will use energy but you can earn some cash based on popularity.
> Resting will lower popularity, but you can regain more energy for tours
> Partying uses cash, but can boost popularity and energy.

Rockstars beware!
Partying too hard while you are too popular might have devasting effects...
      """)
    elif cmd == "quit":
      running = False
    elif cmd == "tour":
      print("\nYou typed: {}, but nothing happened.\n".format(cmd))
      months += 1
    elif cmd == "rest":
      print("\nYou typed: {}, but nothing happened.\n".format(cmd))
      months += 1
    elif cmd == "party":
      print("\nYou typed: {}, but nothing happened.\n".format(cmd))
      months += 1
    else:
      print("\nPlease type in a valid command...\n")



rockstar_sim()

print("\nThanks for playing!\n")
