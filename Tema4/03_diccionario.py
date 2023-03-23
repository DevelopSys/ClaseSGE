informe = {'nombre': "informe ventas", 'prioridad': 'alta',
           'elementos': ['cabecera', 'contenido', 'totales']}

informe["cliente"] = "Universidad Europea"
del (informe["prioridad"])

print(f'eliminado el elemento {informe.pop("elementos")}')

for i in informe.values():
    print(i)


informe.get("nombree")

print(informe["nombre"])

lista = ["ventas", "finanzas", "marketing", ""]
listaDict = dict(["a1", "b2", "c3", "d4"])


print(type(informe))
print(type(lista))
print(type(listaDict))

print(informe)
print(lista)
print(listaDict)
