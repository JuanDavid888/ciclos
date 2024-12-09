#Escriba un programa que muestre la tabla de multiplicar del
#1 al 10 del número ingresado por el usuario:


number = int(input("Ingrese un número: "))

i = 1
while True:
    
    print(f"{number} x {i} = {number * i}")
    i += 1
    if i > 10:
        break
