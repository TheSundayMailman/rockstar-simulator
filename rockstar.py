import random

class Rockstar():
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
    self.pronoun = ("she", "he")[self.gender == "male"]
    self.posessive = ("her", "his")[self.gender == "male"]
    self.alive = True
    self.popularity = 100
    self.money = 100
    self.energy = 100

  def show_status(self):
    status = ("dead", "alive")[self.alive]
    print(" > Popularity: " + str(self.popularity) + "%")
    print(" > Cash: $" + str(self.money))
    print(" > Energy: " + str(self.energy) + "%")
    print(" > Status: " + status)

  def party(self):
    if self.money <= 45:
      print("{} does not have enough cash to party...".format(self.name))
      print("So {} just sits and mopes around for awhile...".format(self.pronoun))
      self.popularity -= random.randint(30, 50)
    else:
      print("{} parties like a rockstar!!!".format(self.name))
      self.energy += random.randint(5, 15)
      self.popularity += random.randint(20, 40)
      self.money -= random.randint(45, 55)
      if self.money < 0:
        self.money = 0
    self.show_status()

  def tour(self):
    print("{} tours around the country to perform!!!".format(self.name))
    if self.popularity < 100:
      print("Oh no...{} seems to be losing it with {} fans...".format(self.pronoun, self.posessive))
      self.money += random.randint(0, 15)
      self.popularity += random.randint(0, 10)
      self.energy -= random.randint(25, 45)
    else:
      self.money += random.randint(35, 35)
      self.popularity += random.randint(30, 50)
      self.energy -= random.randint(25, 45)
    if self.energy < 0:
      self.energy = 0
    self.show_status()

  def rest(self):
    print("{} goes on a haitus...".format(self.name))
    self.energy += random.randint(25, 40)
    self.popularity -= random.randint(25, 45)
    self.money += random.randint(0, 10)
    if self.popularity < 0:
      self.popularity = 0
    self.show_status()



player_char = Rockstar("Nathan Explosion", "male")

player_char.tour()
player_char.party()
player_char.party()
player_char.party()
player_char.party()
player_char.party()
player_char.tour()
player_char.rest()