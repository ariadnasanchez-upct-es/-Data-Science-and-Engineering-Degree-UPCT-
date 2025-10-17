#aqui escribo el código python
print("uno","dos","tres", sep="-")
print("Hola grado de CID")
print("¿Cómo te llamas?")
nombre=input()
resultado=20+10
print("El resultado es, ",resultado)

def pintar_triangulo(altura):
    num_ast =7
    for f in range (altura+1, 1):
        print(""*1-f)
        print("*"*num_ast)
        num_ast-=5