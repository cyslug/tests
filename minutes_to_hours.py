def minutes_to_hours(minutes):
    hours = int(minutes) / 60
    return hours

minutes = input("Digite os minutos: ")
print(minutes_to_hours(minutes))
