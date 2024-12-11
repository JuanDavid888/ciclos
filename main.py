#Escriba un programa que pida al usuario ingresar la altura
#y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

altura = int(input("Ingrese la altura: "))
ancho = int(input("Ingrese el ancho: "))

print(f"Altura: {altura}")
print(f"Ancho: {ancho}")

for altura in range(1, altura +1):
    for ancho in range(1, ancho +1):
        print("*", end = " ")
    print()


#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario:

altura2  = int(input("Ingrese la altura del triángulo: "))

print(f"Altura: {altura2}")

for ancho2 in range(1, altura2 +1):
        print("*" * ancho2)