from datetime import date, datetime


dia = date.today()
print("dia " + str(dia))

now = datetime.now()
print("tiempo " + str(now))

day = datetime.today().weekday()
print("day " + str(day))


diaSemana = datetime.today().strftime('%A')
print("day " + str(diaSemana))
