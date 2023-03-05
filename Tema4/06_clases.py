class Producto:
    def __init__(self, nombre, descripcion, precio):

        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio


producto = Producto("Ordenador", "Ordenador personal para trabajar", 1000)

print(producto.nombre)
print(producto.descripcion)
print(producto.precio)
