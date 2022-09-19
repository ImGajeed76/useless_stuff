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


def rgb_to_hvs(rgb):
    r, g, b = rgb
    h = 0

    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min

    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * (((b - r) / delta) + 2)
    elif c_max == b:
        h = 60 * (((r - g) / delta) + 4)

    if c_max == 0:
        s = 0
    else:
        s = delta / c_max

    v = c_max

    return h, s, v


def hsv_to_rgb(hsv):
    h, s, v = hsv
    r = 0
    g = 0
    b = 0

    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        r = c
        g = x
        b = 0
    elif 60 <= h < 120:
        r = x
        g = c
        b = 0
    elif 120 <= h < 180:
        r = 0
        g = c
        b = x
    elif 180 <= h < 240:
        r = 0
        g = x
        b = c
    elif 240 <= h < 300:
        r = x
        g = 0
        b = c
    elif 300 <= h < 360:
        r = c
        g = 0
        b = x

    r = (r + m) * 255
    g = (g + m) * 255
    b = (b + m) * 255

    return r, g, b
