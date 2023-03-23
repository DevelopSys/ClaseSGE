def funcionImprimir(mensaje):
    print(
        f'El mensaje que se ha mandado a imprimir es el siguiente: {mensaje}')


def sumarElementosList(lista, *elementos):
    lista.extend(elementos)
    return lista


def obtenerSubconjuntoList(lista, pos1, pos2):
    listaResultado = lista[pos1:pos2]
    print('La operacion se ha llevado a cabo con éxito')
    print(f'Se ha obtenido una lista de {len(listaResultado)} elementos')
    return listaResultado
