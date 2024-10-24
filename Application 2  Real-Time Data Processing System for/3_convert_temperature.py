def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(kelvin, unit="C"):
    if unit == "C":
        return kelvin_to_celsius(kelvin)
    elif unit == "F":
        return kelvin_to_fahrenheit(kelvin)
    else:
        return kelvin  # return Kelvin by default
