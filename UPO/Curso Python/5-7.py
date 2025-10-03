horas = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

# Calculamos la duración desglosada
horas_duracion = duracion // 60
minutos_duracion = duracion % 60

# Sumamos duración a la hora inicial
horas_total = horas + horas_duracion
minutos_total = minutos + minutos_duracion

# Ajustamos los minutos y horas
minutos_final = minutos_total % 60
horas_final = (horas_total + minutos_total // 60) % 24

# Mostramos el resultado en formato HH:MM
print("Hora final:", horas_final, ":" , minutos_final, sep="")
