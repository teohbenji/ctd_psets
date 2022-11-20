import math

def compound_interest(amount, rate, periods, time):
    future_value = amount * pow((1 + rate / periods), periods * time)
    
    return round(future_value, 3) 

def area_vol_cylinder(radius, length):
    area = math.pi * pow(radius, 2)
    volume = area * length

    return round(area, 2), round(volume, 2)

def seconds_to_hours(seconds):
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    hours = int(seconds / SECONDS_PER_HOUR)
    seconds -= hours * SECONDS_PER_HOUR
    mins = int(seconds / SECONDS_PER_MINUTE)
    seconds -= mins * SECONDS_PER_MINUTE
    return hours, mins, seconds

def fahrenheit_to_celsius(f):
    c = round((f - 32) * 5 / 9, 2)

    if (c < -273.15):
        return None

    return c


