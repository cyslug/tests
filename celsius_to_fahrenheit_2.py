def celsius_to_fahrenheit(dcelsius):
    dfahrenheit = dcelsius * 1.8 + 32
    return dfahrenheit

dcelsius = [10,-20,-289,100]

for degree in dcelsius:
    if degree <= 40 and degree >= -273.15:
        print (
            "A temperatura é: " +
            str(celsius_to_fahrenheit(degree)) +
            "º fahrenheit"
        )

    elif degree < -273.15:
        print (
            "Tá brincando, né?"
        )

    else:
        print (
            str(celsius_to_fahrenheit(degree)) +
            "º fahrenheit" +
            ": " +
            "Quente pra caralho"
        )
