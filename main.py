from rockstar import Rockstar



def get_player_status(player):
  print(" > Popularity: " + str(player.popularity) + "%")
  print(" > Cash: $" + str(player.money))
  print(" > Party cost: $" + str(player.cost))
  print(" > Energy: " + str(player.energy) + "%\n")



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
Be remembered as a rock legend! Or party too hard and die..."""

  hint = """
Every month, your rockstar can either 'tour', 'rest', or 'party'.
> Touring will use energy but you can earn some cash based on popularity.
> Resting will lower popularity, but you can regain more energy for tours.
> Partying uses cash, but can boost popularity and energy.

Rockstars beware!
Partying too hard while you are too popular might have devasting effects..."""

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
  print("\nYour rockstar will named {}! May {} career be legendary...".format(player.name, player.posessive))
  get_player_status(player)

  # start of game loop
  running = True
  months = 0
  while running and player.alive and months < 12:
    cmd = input("{} of 12 months have passed. What will {} do next?\nType 'help' for help, or 'quit' to exit.\n".format(months, player.name)).lower()
    if cmd == "quit" or cmd == "exit":
      running = False
    elif cmd == "tour":
      if player.energy < 20:
        print(divider)
        print("\nOh no! {} has no energy to perform...so {} takes a rest instead...".format(player.name, player.pronoun))
        player.fail_tour()
      elif player.popularity < 100:
        print(divider)
        print("\n{} tours around the country to perform!!!".format(player.name))
        print("Oh no...{} seems to be losing it with {} fans...".format(player.pronoun, player.posessive))
        player.unpopular_tour()
      else:
        print(divider)
        print("\n{} tours around the country to perform!!!".format(player.name))
        player.tour()
      get_player_status(player)
      months += 1
    elif cmd == "party":
      if player.money < player.cost:
        print(divider)
        print("\n{} is too broke to party...".format(player.name))
        print("So {} just sits and mopes around for awhile...".format(player.pronoun))
        player.broke_party()
      elif player.energy < 15:
        print(divider)
        print("\n{} does not have enough energy to party...".format(player.name))
        print("So {} just sits and mopes around for awhile...".format(player.pronoun))
        player.fail_party()
      else:
        print(divider)
        print("\n{} parties like a rockstar!!!".format(player.name))
        player.party()
      get_player_status(player)
      months += 1
    elif cmd == "rest":
      print(divider)
      print("\n{} goes on a haitus...".format(player.name))
      player.rest()
      get_player_status(player)
      months += 1
    elif cmd == "help":
      print(divider)
      print(hint)
    else:
      print(divider)
      print("\nPlease type in a valid command...\n")

  # check reason for loop exit
  if player.alive == False:
    print("{} has died from partying too hard...".format(player.name))
    if player.popularity < 50:
      print("And {} died with little fans to remember {}, sad...".format(player.pronoun, player.posessive))
  
  # evaluate result
  print(divider)
  print("After one year of being a rockstar,")
  if player.popularity <= 50:
    print("{} is not very popular...".format(player.name))
  elif player.popularity > 50 and player.popularity <= 120:
    print("{} is somewhat popular...".format(player.name))
  else:
    print("{} is very popular!".format(player.name))



# main function call
rockstar_sim()


# exit greeting
print("\nThanks for playing!\n")
