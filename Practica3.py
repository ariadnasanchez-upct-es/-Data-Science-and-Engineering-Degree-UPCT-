print("Práctica 3: Estructuras de control condicionales.")

print("Ejercicio 1: Ecuación avanzada.")
import math
a=int(input("Introduzca un número entero\n"))
b=int(input("Introduzca un número entero\n"))
c=int(input("Introduzca un número entero\n"))

𝑥1=(-b+(math.sqrt(b**2)-(4*a*c)))/(2*a)
𝑥2=(-b-(math.sqrt(b**2)-(4*a*c)))/(2*a)

if ((b**2)-(4*a*c)/(2*a)) > 0:
    print("La solución x1 es: ", x1)
    print("La solución x2 es: ", x2)

if ((b**2)-(4*a*c)/(2*a)) < 0:
    print("La ecuación tiene raíces complejas")

print("Ejercicio 2: Calculadora avanzada.")
x = int(input("Introduzca un número entero\n"))
y = int(input("Introduzca un número entero\n"))

operación = int(input("Pulse: (1) para sumar, (2) para restar, (3) para multiplicar, (4) para dividir, y (5) para residuo."))

if operación == 1:
    print("La suma de x + y es: ", x+y)
if operación == 2:
    print("La resta de x - y es: ", x-y)
if operación == 3:
    print("La multiplicación de x * y es: ", x*y)
if operación == 4:
    print("La división de x / y es: ", x/y)
if operación == 5:
    print("El resto de la división es: ", x%y)

print("Ejercicio 3: Desglose billetes y monedas.")

x=int(input("Introduce la cantidad:\n"))

if x>=500:
    dinero = x // 500
    print(dinero, "billetes de 500")
    x = x % 500
if x>=200:
    dinero = x // 200
    print(dinero, "billetes de 200")
    x = x % 200
if x>=100:
    dinero = x // 100
    print(dinero, "billetes de 100")
    x = x % 100
if x>=50:
    dinero = x // 50
    print(dinero, "billetes de 50")
    x = x % 50
if x>=20:
    dinero = x // 20
    print(dinero, "billetes de 20")
    x = x % 20
if x>=10:
    dinero = x // 10
    print(dinero, "billetes de 10")
    x = x % 10
if x>=5:
    dinero = x // 5
    print(dinero, "billetes de 5")
    x = x % 5
if x>=2:
    dinero = x // 2
    print(dinero, "monedas de 2")
    x = x % 2
if x>=1:
    dinero = x // 1
    print(dinero, "monedas de 1")
    x = x % 1

print("Ejercicio 4: condiciones")

dia = int(input("¿Qué día es hoy (número de mes)? \n"))
if 0< dia <=15:
    print("Le corresponde el lado izquierdo de la calle")
elif 0< dia <32:
    print("Le corresponde el lado derecho de la calle")
else:
    print("dia incorrecto")

print("Ejercicio 5: fechas")
dia = int(input("Hoy es el dia: \n"))
mes = int(input("Del mes: \n"))
año = int(input("Del año:\n"))


print(dia, mes, año, sep="/")

if dia == 31:
    if mes == 12:
        dia = 1
        mes = 1
        año = año + 1
    elif mes == 1 or 3 or 5 or 7 or 8 or 10:
        dia = 1
        mes = mes + 1
        año = año
    else:
        print("No esxiste el día 31 en", mes)
elif dia == 30:
    if mes == 2 or 4 or 6 or 9:
        dia = 1
        mes = mes + 1
        año = año
    else:
        dia = dia + 1
        mes = mes
        año = año
else:
    dia = dia + 1

print("Ejercicio 6")

# Leer un carácter de la entrada
caracter = input("Introduce un carácter: ")

# Verificar si el carácter es una letra mayúscula
if 'A' <= caracter <= 'Z':
    if caracter == 'Z':
        caracter_codificado = 'A'  # Z se convierte en A
    else:
        caracter_codificado = chr(ord(caracter) + 1)  # Siguiente letra

# Verificar si el carácter es una letra minúscula
elif 'a' <= caracter <= 'z':
    if caracter == 'z':
        caracter_codificado = 'a'  # z se convierte en a
    else:
        caracter_codificado = chr(ord(caracter) + 1)  # Siguiente letra

# Verificar si el carácter es un dígito
elif '0' <= caracter <= '9':
    if caracter == '9':
        caracter_codificado = '0'  # 9 se convierte en 0
    else:
        caracter_codificado = chr(ord(caracter) + 1)  # Siguiente número

# Si no es letra ni dígito, devolver *
else:
    caracter_codificado = '*'

# Mostrar el resultado
print("El carácter codificado es:", caracter_codificado)
