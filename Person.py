class Person:
    def __init__(self, name, money, mood ="Happy",healthRate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate
   
    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"
        print(f"{self.name} is now {self.mood}")

    def eat(self, meals):
        if meals ==3:
            self.helthRate = 100
        elif meals ==2:
            self.helthRate = 75
        else:
            self.helthRate = 50
        print(f"{self.name}'s healthRate is {self.healthRate}%")


    def buy(self, items):
        if items == 1:
          self.money-=10 * items
          print(f"{self.name} spent {10*items} L.E, remaining money: {self.money} L.E")


 
