def generarInforme(contenido, titulo, elementos):
    print(titulo)
    for i in contenido:
        print(i)
    print(f'los elementos pasados para el informe son {elementos}')


generarInforme(["Esto es un ejemplo de contenido", "para mostrar en un informe"],
               "Informe posicional", [1, 2, 3, 4])

generarInforme(elementos=["Esto es un ejemplo de contenido", "para mostrar en un informe"],
               titulo="Informe posicional", contenido=[1, 2, 3, 4])


def funcionImprimir(mensaje: str):
    print(f'el {mensaje} se ha impreso correctamente')





def suma(op1, op2):
    resultado = op1+op2
    print('Suma realizada con éxito')
    return resultado


resultado = suma(4, 4)
print(resultado)  # 13


def multiplicacion(op1, op2=1):
    resultado = op1*op2
    print(f'La multiplicación de {op1} y {op2} es {resultado}')


multiplicacion(9, 2)  # 18
multiplicacion(9)  # 9


def sumarTodos(*elementos):
    sumatorio = 0
    for item in elementos:
        sumatorio += item
    print(
        f'El resultado de sumar todos los elementos pasados es de {sumatorio}')


sumarTodos(1, 4, 5, 6, 7, 3, 1, 0)
