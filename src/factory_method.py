from abc import ABC, abstractmethod


# Define the Pizza Factory Interface
class PizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self):
        pass


# Create Concrete Pizza Factories
class MargheritaPizzaFactory(PizzaFactory):
    def create_pizza(self):
        return MargheritaPizza()


class PepperoniPizzaFactory(PizzaFactory):
    def create_pizza(self):
        return PepperoniPizza()


class VeggiePizzaFactory(PizzaFactory):
    def create_pizza(self):
        return VeggiePizza()


# Define Pizza Classes
class Pizza:
    def prepare(self):
        pass


class MargheritaPizza(Pizza):
    def prepare(self):
        print("Preparing Margherita Pizza")


class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza")


class VeggiePizza(Pizza):
    def prepare(self):
        print("Preparing Veggie Pizza")


# Client Code
def order_pizza(factory):
    pizza = factory.create_pizza()
    pizza.prepare()
    return pizza


margherita_factory = MargheritaPizzaFactory()
margherita = order_pizza(margherita_factory)  # Preparing Margherita Pizza

pepperoni_factory = PepperoniPizzaFactory()
pepperoni = order_pizza(pepperoni_factory)  # Preparing Pepperoni Pizza
