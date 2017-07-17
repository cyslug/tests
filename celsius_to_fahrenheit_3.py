def celsius_to_fahrenheit(dcelsius):
    dfahrenheit = float(dcelsius) * 1.8 + 32
    return dfahrenheit

dcelsius = [10,-20,100]

with open("example2.txt", "w") as file:
    for degree in dcelsius:
        file.write("\n"+str(celsius_to_fahrenheit(degree)))
