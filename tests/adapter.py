import unittest
from io import StringIO
from unittest.mock import patch


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


class TestChargingStation(unittest.TestCase):
    def setUp(self):
        self.gasoline_car = GasolineCar()
        self.electric_car = ElectricCar()
        self.charging_station = ChargingStation()

    def test_gasoline_car_adapter(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            adapter = GasolineCarAdapter(self.gasoline_car)
            self.charging_station.refuel(adapter)
            expected_output = "Refueling a gasoline car\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_electric_car_directly(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.charging_station.refuel(self.electric_car)
            expected_output = "Charging an electric car\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_unsupported_car_type(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            unsupported_car = GasolineCar()  # GasolineCar without adapter
            self.charging_station.refuel(unsupported_car)
            expected_output = "Unsupported car type\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_charging_station_with_invalid_adapter(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            invalid_adapter = GasolineCar()  # ElectricCar used as an adapter
            self.charging_station.refuel(invalid_adapter)
            expected_output = "Unsupported car type\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_charging_station_with_no_refuel_method(self):
        class CarWithoutRefuelMethod:
            pass

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            unsupported_car = CarWithoutRefuelMethod()
            self.charging_station.refuel(unsupported_car)
            expected_output = "Unsupported car type\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
