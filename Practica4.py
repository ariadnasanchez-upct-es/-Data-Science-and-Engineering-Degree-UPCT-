print("Práctica 4: Estructuras de control iterativas.")

print("Ejercicio 1: Calculadora avanzada 2.")
# Variable de control para terminar el programa
salir = False

while not salir:
    # Solicitar al usuario que introduzca dos enteros
    x = int(input("Introduzca el primer número entero: "))
    y = int(input("Introduzca el segundo número entero: "))
    
    # Mostrar el menú de operaciones
    print("\nSeleccione la operación a realizar:")
    print("(1) Sumar")
    print("(2) Restar")
    print("(3) Multiplicar")
    print("(4) Dividir")
    print("(5) Residuo (resto de la división)")
    print("(0) Salir")
    
    # Leer la operación elegida por el usuario
    operacion = int(input("\nElija la operación (0-5): "))

    # Opción para salir
    if operacion == 0:
        print("Saliendo del programa...")
        salir = True  # Cambia la variable de control para salir del bucle
    
    # Operaciones aritméticas
    elif operacion == 1:
        print(f"La suma de {x} + {y} es: {x + y}")
    
    elif operacion == 2:
        print(f"La resta de {x} - {y} es: {x - y}")
    
    elif operacion == 3:
        print(f"La multiplicación de {x} * {y} es: {x * y}")
    
    elif operacion == 4:
        if y != 0:
            print(f"La división de {x} / {y} es: {x / y}")
        else:
            print("Imposible dividir por cero")
    
    elif operacion == 5:
        if y != 0:
            print(f"El residuo de {x} % {y} es: {x % y}")
        else:
            print("Imposible dividir por cero")
    
    else:
        print("Operación no válida. Elija un número entre 0 y 5.")
    
    # Espacio para hacer la salida más clara
    print("\n----------------------------------\n")

print("Ejercicio 2: Sensor de ruido.")

import random

# Solicitar el valor de N
N = int(input("Introduce el valor máximo del rango [0, N]: "))

# Inicializar variables
suma_pares = 0
numero_generado = -1  # Inicializarlo con un valor distinto de 0 para entrar en el bucle

# Simular la generación de números aleatorios
print("\nValores generados por el sensor:")
while numero_generado != 0:
    # Generar un número aleatorio en el rango [0, N]
    numero_generado = random.randint(0, N)
    
    # Mostrar el número generado
    print(numero_generado, end=" ")
    
    # Si el número es par y distinto de 0, sumamos
    if numero_generado % 2 == 0 and numero_generado != 0:
        suma_pares += numero_generado

# Mostrar la suma de los valores pares
print(f"\n\nLa suma de los valores pares generados es: {suma_pares}")

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

print("Ejercicio 4. Número primo.")
N = 0
# Pedir un número positivo al usuario
N = -1
while N <= 0:
    N = int(input("Introduce un número positivo N: "))
    if N <= 0:
        print("El número debe ser positivo. Inténtalo de nuevo.")

# Mostrar los números primos entre 1 y N
print(f"Números primos entre 1 y {N}:")

for numero in range(2, N + 1):  # Comenzar desde 2, el primer número primo
    es_primo = True  # Suponemos que el número es primo
    for i in range(2, int(numero ** 0.5) + 1):  # Comprobar divisores hasta la raíz cuadrada de 'numero'
        if numero % i == 0:  # Si es divisible por i
            es_primo = False  # No es primo
            break  # No necesitamos seguir verificando más
    if es_primo:  # Si sigue siendo primo, lo imprimimos
        print(numero)

print("Ejercicio 5. Adivina el número.")
import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0
jugando = True  # Variable para controlar el bucle

print("¡Bienvenido al juego 'Adivina el número'!")
print("He generado un número entre 1 y 100. Intenta adivinarlo.")

while jugando:
    # Solicitar al usuario que adivine el número
    adivinanza = int(input("Introduce tu adivinanza: "))
    intentos += 1

    # Comprobar si la adivinanza es correcta
    if adivinanza == numero_secreto:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        if adivinanza == numero_secreto:
            numero_secreto = random.randint(1, 100)
            intentos = 0
            jugando = True  # Variable para controlar el bucle
    else:
        # Dar pistas al usuario
        if adivinanza < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")

    # Preguntar si el usuario quiere continuar o rendirse
    continuar = input("¿Quieres seguir jugando? (s/n): ").lower()
    if continuar == 'n':
        if adivinanza != numero_secreto:
            print(f"Te has rendido. El número secreto era {numero_secreto}.")
            print(f"Total de intentos realizados: {intentos}.")
        jugando = False  # Cambiar el estado para salir del bucle

print("Ejercicio 6. Triangulo de *.")
# Pedir un número positivo al usuario
# Solicitar un número entero positivo N
N = int(input("Introduce un número entero positivo para la altura del triángulo: "))

# Asegurarse de que N sea positivo
while N <= 0:
    N = int(input("Por favor, introduce un número entero positivo: "))

# Dibujar el triángulo de asteriscos
for i in range(N):
    # Calcular la cantidad de asteriscos en la fila actual
    num_asteriscos = 1 + 2 * i
    # Imprimir la fila de asteriscos
    print('*' * num_asteriscos)

