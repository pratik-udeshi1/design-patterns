# Adaptee 1: Gasoline (Petrol) Car
class GasolineCar:
    def refuel(self):
        print("Refueling a gasoline car")


# Adaptee 2: Electric Car
class ElectricCar:
    def charge(self):
        print("Charging an electric car")


# Target: Common refueling or charging station
class ChargingStation:
    def refuel(self, car):
        if hasattr(car, 'charge') and callable(car.charge):
            car.charge()
        else:
            print("Unsupported car type")


class GasolineCarAdapter:
    def __init__(self, car):
        self.car = car

    def charge(self):
        self.car.refuel()


# Example usage
gasoline_car = GasolineCar()
electric_car = ElectricCar()

charging_station = ChargingStation()

# Plug in the gasoline car into the charging station using an adapter
adapter = GasolineCarAdapter(gasoline_car)
charging_station.refuel(adapter)
# Outputs: Refueling a gasoline car

# Plug in the electric car directly into the charging station
charging_station.refuel(electric_car)
# Outputs: Charging an electric car
