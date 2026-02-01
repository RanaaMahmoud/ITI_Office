class Car:
    def __init__(self,name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity


    def run(self, velocity, distance):
        self.velocity = velocity
        fuel_needed = (distance // 10) * 10

        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            remaining_distance = distance - (self.fuelRate / 10) * 10
            self.fuelRate = 0
            self.stop(remaining_distance)
        


    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance == 0:
            print("Arrived at destination ")
        else:
            print(f"Car stopped, remaining distance: {remaining_distance} km")



