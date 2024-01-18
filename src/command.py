from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


# Client code
light = Light()
turn_on_command = TurnOnLightCommand(light)
turn_off_command = TurnOffLightCommand(light)

remote = RemoteControl()
remote.set_command(turn_on_command)
remote.press_button()  # Output: Light is on

remote.set_command(turn_off_command)
remote.press_button()  # Output: Light is off
