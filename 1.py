# un entrenador quiere analizar el rendimiento de su equipo en los últimos 5 partidos de la temporada. Para cada partido, se registran los goles anotados por cada uno de los 11 jugadores del equipo. Se debe calcular:
# El promedio de goles por partido.
# Cuántos jugadores marcaron más de 2 goles en al menos un partido.

goles = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(2):
    print(f"""Dia {i+1}
    """)
    if i == 0:
        for i in range(1,12):
            a = int(input(f"Goles del jugador {i}: "))
            goles[i-1][0] = a
    
    if i == 1:
        for i in range(1,12):
            a = int(input(f"Goles del jugador {i}: "))
            goles[i-1][1] = a

    if i == 2:
        for i in range(1,12):
            a = int(input(f"Goles del jugador {i}: "))
            goles[i-1][2] = a

    if i == 3:
        for i in range(1,12):
            a = int(input(f"Goles del jugador {i}: "))
            goles[i-1][3] = a

    if i == 4:
        for i in range(1,12):
            a = int(input(f"Goles del jugador {i}: "))
            goles[i-1][4] = a

suma = 0
a = 0
print("""
Promedio de goles por partido""")
for _ in range(11):
    for gol in goles:
        b=0
        suma += gol[b]
        promedio = suma / 5
        b+=1
    print(f"Jugador {_+1}: {promedio} por partido")

print("""
Jugadores destacados""")
for _ in range(11):
    for dia in range(5):
        if goles[_][dia] > 2:
            print(f"Jugador {_ + 1} marcó más de 2 goles en el día {dia + 1}")


