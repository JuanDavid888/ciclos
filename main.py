#Escriba un programa que entregue todos los divisores del número entero ingresado:

dividiendo = (int(input("Ingrese un número: ")))

divisores = []

for valor in range(1, dividiendo + 1):
    if dividiendo % valor == 0:
        divisores.append(valor)

print(f"{divisores}")
