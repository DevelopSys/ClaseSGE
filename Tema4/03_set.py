elementos = {"elemento 1", "elemento 2", "elemento 3"}
elementos.add("elemento adicional")
elementos.remove("elemento 1")
for i in elementos:
    print(i)

conjunto1 = {1, 2, 3, 4, 5, 6, 7, 8}
conjunto2 = {4, 5, 9, 10, 11, 12}

conjuntoResultante = conjunto1.symmetric_difference(conjunto2)
print(conjuntoResultante)
