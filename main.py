#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y 
#entregue como resultado el tiempo total de viaje en formato horas:minutos.

totalViajes = 0

while True:
    viajes = int(input("Duración del tramo: "))
    if viajes == 0:
        break

    totalViajes += viajes

horas = totalViajes // 60
minutos = totalViajes % 60

print(f"Tiempo total de viaje: {horas} horas con {minutos} minutos")