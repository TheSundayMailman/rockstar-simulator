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

  # update cost of next party, called after every method
  def update_cost(self):
    self.cost = int(self.popularity * random.randint(4, 5))

  # all tour methods
  def tour(self):
    self.energy -= random.randint(25, 45)
    self.popularity += random.randint(30, 50)
    self.money += random.randint(5, 10) * self.popularity
    if self.energy < 0:
      self.energy = 0
    self.update_cost()

  def unpopular_tour(self):
    self.energy -= random.randint(25, 45)
    self.popularity += random.randint(0, 10)
    self.money += random.randint(1, 5) * self.popularity
    if self.energy < 0:
      self.energy = 0
    self.update_cost()

  def fail_tour(self):
    self.energy += random.randint(6, 12)
    self.popularity -= random.randint(25, 45)
    self.money += random.randint(1, 3) * self.popularity
    if self.popularity < 0:
      self.popularity = 0
    self.update_cost()

  # all party methods
  def party(self):
    self.energy -= random.randint(12, 18)
    self.popularity += random.randint(30, 50)
    self.money -= self.cost
    if self.energy < 0:
      self.energy = 0
    self.update_cost()

  def broke_party(self):
    self.energy += random.randint(1, 5)
    self.popularity -= int(random.randint(30, 50) * self.popularity / 100)
    if self.popularity < 0:
      self.popularity = 0
    self.update_cost()

  def fail_party(self):
    self.energy += random.randint(1, 5)
    self.popularity -= int(random.randint(30, 50) * self.popularity / 100)
    if self.popularity < 0:
      self.popularity = 0
    self.update_cost()

  # all rest methods
  def rest(self):
    self.energy += random.randint(25, 40)
    self.popularity -= random.randint(20, 30)
    self.money += random.randint(0, 10)
    if self.popularity < 0:
      self.popularity = 0
    self.update_cost()
