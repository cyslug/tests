def celsius_to_fahrenheit(dcelsius):
    dfahrenheit = dcelsius * 1.8 + 32
    return dfahrenheit

dcelsius = float(input("Digite a temperatura em ºC: "))

if dcelsius <= 40 and dcelsius >= -273.15:
    print (
        "A temperatura é: " +
        str(celsius_to_fahrenheit(dcelsius)) +
        "º fahrenheit"
    )

elif dcelsius < -273.15:
    print (
        "Tá brincando, né?"
    )

else:
    print (
        str(celsius_to_fahrenheit(dcelsius)) +
        "º fahrenheit" +
        ": " +
        "Quente pra caralho"
    )
