from typing import Optional


# Product
class Car:
    def __init__(self, make: str, model: str, year: int, color: Optional[str] = None, engine: Optional[str] = None):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine

    def __str__(self):
        return f"Car - Make: {self.make}, Model: {self.model}, Year: {self.year}, " \
               f"Color: {self.color or 'N/A'}, Engine: {self.engine or 'N/A'}"


# Builder
class CarBuilder:
    def __init__(self, make: str, model: str, year: int):
        self.car = Car(make, model, year)

    def add_color(self, color: str):
        self.car.color = color
        return self

    def add_engine(self, engine: str):
        self.car.engine = engine
        return self

    def build(self):
        return self.car


# Director
class Director:
    @staticmethod
    def construct_sports_car():
        return CarBuilder('Ferrari', '488 GTB', 2022).add_color('Red').add_engine('V8').build()

    @staticmethod
    def construct_standard_car():
        return CarBuilder('Toyota', 'Camry', 2022).build()


# Creating a sports car
sports_car = Director.construct_sports_car()
print(sports_car)
# Outputs: Car - Make: Ferrari, Model: 488 GTB, Year: 2022, Color: Red, Engine: V8


# Creating a standard car
standard_car = Director.construct_standard_car()
print(standard_car)
# Outputs: Car - Make: Toyota, Model: Camry, Year: 2022, Color: N/A, Engine: N/A
