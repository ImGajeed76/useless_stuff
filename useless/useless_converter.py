import math


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9


def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9 / 5 - 459.67


def degree_to_radian(degree):
    return degree * math.pi / 180


def radian_to_degree(radian):
    return radian * 180 / math.pi
