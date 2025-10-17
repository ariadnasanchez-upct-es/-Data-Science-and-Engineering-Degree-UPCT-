print("Ejercicio 3: Número perfecto.")

# Pedir un número positivo al usuario
N = -1
while N <= 0:
    N = int(input("Introduce un número positivo N: "))
    if N <= 0:
        print("El número debe ser positivo. Inténtalo de nuevo.")

# Mostrar los números perfectos entre 1 y N
print(f"Números perfectos entre 1 y {N}:")

for numero in range(1, N + 1):
    suma_divisores = 0
    # Calcular la suma de divisores
    for i in range(1, numero):
        if numero % i == 0:  # Si i es un divisor de numero
            suma_divisores += i
    # Verificar si la suma de divisores es igual al número
    if suma_divisores == numero:
        print(numero)