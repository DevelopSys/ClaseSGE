letra = 'a'
palabra = 'introduccion a python'
palabraMultiple = """ Esto es la escritura de una variable
donde están escritas varias lineas, pero asignadas a la misma variable
"""

print(letra)
print(palabra)
print(palabraMultiple)

nombre = 'Borja'
apellido = 'Martin'
asignatura = 'SGE'
anio = 2023

print('Este repositorio ha sido realizado por {} {} para la asignautara de {} en el año {}'.format(
    nombre, apellido, asignatura, anio))

""" print('Este repositorio ha sido realizado por %s %s para la asignautar de %s en el año %d' %
      (nombre, apellido, asignatura, anio)) """

print(
    f'Este repositorio ha sido realizado por {nombre} {apellido} para la asignatura de {asignatura} en el año {anio}')


print(f'La longitura de {nombre} es {len(nombre)}')

letra = nombre[0]  # B
letra = nombre[len(nombre)-1]  # a

print(letra)

correo = 'developandsystem@gmail.com'

dominio = correo[correo.index('@'):len(correo)]
print(dominio)

palabraInicial = 'esto es un ejemplo'
print(palabraMultiple.capitalize())  # 'Esto es un Ejemplo'

frase = 'esta frase está echa para poder buscar todos los elementos de la misma'
print(frase.count('a'))
print(frase.count('es'))

print(frase.endswith("mos"))  # false
print(frase.endswith("isma"))  # true
print(frase.find("f"))  # 5
