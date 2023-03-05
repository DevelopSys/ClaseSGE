numeros = [1, 2, 3, 4, 5, 6, 7]
numeros.insert(1, 10)
print(numeros)


numeros[0:3] = [9, 8, 7]

numeros[0] = -1

subconjunto = numeros[2:4]
print(subconjunto)

print(numeros[-1])  # 7
print(numeros[-len(numeros)])  # 1

print(numeros[0])  # 1
print(numeros[len(numeros)-1])  # 7

palabras = list()
palabras.extend(["Ejemplo", "de", "como", "añadir", "elementos"])
print(palabras)

lista1 = ["primero", "segundo", "tercero"]
listaResultante = lista1 * 2
print(listaResultante)

lista2 = ["cuarto", "quinto", "sexto"]

listaResultante = lista1 + lista2
print(listaResultante)

listaElementos = ["Elemento 4", "Elemento 2",
                  "Elemento 1", "Elemento 3"]

listaElementos.sort()

print(listaElementos)

if 'Elemento 1' in listaElementos:
    print('El elemento está en la lista')

for item in listaElementos:
    print(item)


print(f'Elemento {listaElementos.pop(0)} eliminado con éxito')
# listaElementos.remove('Elemento 1')
print(listaElementos)

del listaElementos[2]
