class Producto:
    def __init__(self, nombre, descripcion, precio):

        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def mostrarDatos(self):
        print(f'El nombre del producto es {self.nombre}')
        print(f"f La descripción del producto es {self.descripcion}")
        print(f"f El precio del producto es {self.precio}")


# producto = Producto("Ordenador", "Ordenador personal para trabajar", 1000)

# producto.mostrarDatos()


class Informe:
    def __init__(self, titulo, categoria, elementos, nombre):
        self.titulo = titulo
        self.categoria = categoria
        self.elementos = elementos
        self.__nombre = nombre

    def imprimirInforme(self):
        print(f'{self.__nombre}')
        print(f'{self.titulo}')
        print(f'{self.categoria}')
        for item in self.elementos:
            print(f'{item}')


informe = Informe("Titulo", "Categoria", [
                  "elemento1", "elemento2", "elemento3"], "nombre")

print(informe.__nombre)
informe.imprimirInforme()
