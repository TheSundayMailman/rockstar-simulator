from rockstar import Rockstar

divider = "\n==========================================================================="

# prints player status
def show_status(player):
  print(" > Popularity: " + str(player.popularity) + "%")
  print(" > Cash: $" + str(player.money))
  print(" > Party cost: $" + str(player.cost))
  print(" > Energy: " + str(player.energy) + "%\n")

# handles all tour logics
def handle_tour(player):
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

# handles all party logics
def handle_party(player):
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

# handles all rest logics
def handle_rest(player):
  print(divider)
  print("\n{} goes on a haitus...".format(player.name))
  player.rest()

# handles all ending scenarios
def handle_ending(player):
  if player.popularity <= 50:
    print("{} is not very popular...".format(player.name))
  elif player.popularity > 50 and player.popularity <= 120:
    print("{} is somewhat popular...".format(player.name))
  else:
    print("{} is very popular!".format(player.name))