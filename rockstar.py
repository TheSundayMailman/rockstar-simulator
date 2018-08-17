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
    self.cars = 0
    self.incidents = 0
  
  # makes sure stats are not negative; called after every method
  def balancer(self):
    if self.energy < 0:
      self.energy = 0
    if self.popularity < 0:
      self.popularity = 0
    if self.money < 0:
      self.money = 0
    # update cost of next party
    self.cost = int(self.popularity * random.randint(4, 5))

  # all tour methods
  def tour(self):
    self.energy -= random.randint(25, 45)
    self.popularity += random.randint(30, 50)
    self.money += random.randint(5, 10) * self.popularity
    self.balancer()

  def unpopular_tour(self):
    self.energy -= random.randint(25, 45)
    self.popularity += random.randint(0, 10)
    self.money += random.randint(1, 5) * self.popularity
    self.balancer()

  def fail_tour(self):
    self.energy += random.randint(6, 12)
    self.popularity -= random.randint(25, 45)
    self.money += random.randint(1, 3) * self.popularity
    self.balancer()

  # all party methods
  def party(self):
    self.energy -= random.randint(12, 18)
    self.popularity += random.randint(30, 50)
    self.money -= self.cost
    self.balancer()

  def broke_party(self):
    self.energy += random.randint(1, 5)
    self.popularity -= int(random.randint(30, 50) * self.popularity / 100)
    self.balancer()

  def fail_party(self):
    self.energy += random.randint(1, 5)
    self.popularity -= int(random.randint(30, 50) * self.popularity / 100)
    self.balancer()

  # all rest methods
  def rest(self):
    self.energy += random.randint(25, 40)
    self.popularity -= random.randint(20, 30)
    self.money += random.randint(0, 10)
    self.balancer()

  # all event encounter methods
  def buy_car(self):
    self.cars += 1
    self.money = int(self.money * random.randint(25, 40) / 100)
    self.popularity += random.randint(10, 20)
    self.balancer()

  def punch_producer(self):
    self.money = int(self.money * random.randint(20, 35) / 100)
    self.popularity += random.randint(15, 20)
    self.energy -= random.randint(5, 10)
    self.balancer()
  
  def engage_producer(self):
    self.money = int(self.money * random.randint(110, 135) / 100)
    self.popularity -= random.randint(45, 55)
    self.balancer()

  def disengage_producer(self):
    self.popularity = int(self.popularity * random.randint(15, 20) / 100)
    self.balancer()

  def punch_fan(self):
    self.incidents += 1
    self.money = int(self.money * random.randint(20, 25) / 100)
    self.popularity += random.randint(5, 10)
    self.energy -= random.randint(5, 10)
    self.balancer()
  
  def run_from_fan(self):
    self.energy += random.randint(5, 10)
    self.popularity -= random.randint(15, 20)
    self.balancer()

  def call_security(self):
    self.energy += random.randint(0, 5)
    self.popularity += random.randint(5, 10)
    self.balancer()
  
  def game_over(self):
    self.alive = False
    self.balancer()
