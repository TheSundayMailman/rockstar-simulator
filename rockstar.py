import random

class Rockstar():
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
    self.pronoun = ("she", "he")[self.gender == "male"]
    self.posessive = ("her", "his")[self.gender == "male"]
    self.alive = True
    self.popularity = 100
    self.money = 1000
    self.energy = 100
    self.cost = 500

  def update_cost(self):
    self.cost = int(self.popularity * random.randint(4, 5))

  def show_status(self):
    # status = ("dead", "alive")[self.alive]
    print(" > Popularity: " + str(self.popularity) + "%")
    print(" > Cash: $" + str(self.money))
    print(" > Party cost: $" + str(self.cost))
    print(" > Energy: " + str(self.energy) + "%\n")

  def tour(self):
    if self.energy == 0:
      print("\nOh no! {} has no energy to perform...so {} takes a rest instead...".format(self.name, self.pronoun))
      self.energy = 10
      self.popularity -= random.randint(25, 45)
      self.money += random.randint(1, 3) * self.popularity
    else:
      print("\n{} tours around the country to perform!!!".format(self.name))
      if self.popularity < 100:
        print("Oh no...{} seems to be losing it with {} fans...".format(self.pronoun, self.posessive))
        self.energy -= random.randint(30, 50)
        self.popularity += random.randint(0, 10)
        self.money += random.randint(1, 5) * self.popularity
      else:
        self.energy -= random.randint(25, 45)
        self.popularity += random.randint(30, 50)
        self.money += random.randint(5, 10) * self.popularity
    if self.energy < 0:
      self.energy = 0
    if self.popularity < 0:
      self.popularity = 0
    self.update_cost()
    self.show_status()

  def party(self):
    if self.money < self.cost:
      print("\n{} is too broke to party...".format(self.name))
      print("So {} just sits and mopes around for awhile...".format(self.pronoun))
      self.energy += random.randint(1, 5)
      self.popularity -= int(random.randint(30, 50) * self.popularity / 100)
    elif self.energy < 15:
      print("\n{} does not have enough energy to party...".format(self.name))
      print("So {} just sits and mopes around for awhile...".format(self.pronoun))
      self.energy += random.randint(1, 5)
      self.popularity -= int(random.randint(30, 50) * self.popularity / 100)
    else:
      print("\n{} parties like a rockstar!!!".format(self.name))
      self.energy -= random.randint(12, 18)
      self.popularity += random.randint(20, 40)
      self.money -= self.cost
    if self.popularity < 0:
      self.popularity = 0
    if self.energy < 0:
      self.energy = 0
    self.update_cost()
    self.show_status()

  def rest(self):
    print("\n{} goes on a haitus...".format(self.name))
    self.energy += random.randint(25, 40)
    self.popularity -= random.randint(25, 45)
    self.money += random.randint(0, 10)
    if self.popularity < 0:
      self.popularity = 0
    self.update_cost()
    self.show_status()
