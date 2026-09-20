"""Using map and lambda to transform a list."""

temperatures_celsius = [0, 10, 20, 30]

# Here is map with lambda to convert Celsius to Fahrenheit.
temperatures_fahrenheit = list(map(lambda temperature: temperature * 9 / 5 + 32, temperatures_celsius))

print(temperatures_fahrenheit)
