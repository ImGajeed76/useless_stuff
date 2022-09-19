from useless.useless_string import *
from useless.useless_converter import *

if __name__ == '__main__':
    celsius = 30
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)

    print(f"{celsius}°C = {fahrenheit}°F = {kelvin}K")

    print(f"{celsius == fahrenheit_to_celsius(fahrenheit)}")
    print(f"{celsius == kelvin_to_celsius(kelvin)}")

    fahrenheit = kelvin_to_fahrenheit(kelvin)
    print(f"{kelvin == fahrenheit_to_kelvin(fahrenheit)}")
