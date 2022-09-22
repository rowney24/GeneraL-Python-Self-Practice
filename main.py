

#*Problem Statement
#Create a Car class with two instance attributes:

#.color, which stores the name of the car’s color as a string
#.mileage, which stores the number of miles on the car as an integer
#Then instantiate two Car objects—a blue car with 20,000 miles and a red car with 30,000 miles—and print out their colors and mileage.


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def descrip(self):
        return f"color is, {self.color}, and it has a mileage of", {self.mileage}


FirstCar = Car(color="blue", mileage=20000)
SecondCar = Car(color="red", mileage=30000)

print(FirstCar.descrip())
print(SecondCar.descrip())

