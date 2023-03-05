# Comentarios

Comentario de una se utiliza el carácter #

```py
# esto es un ejemplo de comentario
```
Para poner comentarios de lineas múltiples se utiliza el caracter """

```py
""" esto es un ejemplo de comentario
de lineas multiples para comentar código
"""
```
# Definición de variable

Python es un lenguaje no tipado, por lo que no es necesario indicar el tipo de variable en el momento que se crea. PAra poder declarar una variable se realiza mediante el nombre de la referencia y su valor:

```py
nombre_variable = valor
operandoUno = 2
```

Una vez se quiera utilizar la variable tan solo es necesario nombrarla

```py
print(operandoUno)
```

## Tipos de variable

- Numéricos: se trata de los números reales, enteros y complejos

```py
numero = 8
numeroDecimal = 4.23
numeroComplejo = 4.21j
```

- Cadenas de texto: A diferencia de otros lenguajes de programación, en este caso no se diferencia entre mayúsculas y caracteres, por lo que una palabra va guardada entre el simbolo de '

```py
saludo = 'Hola esto es un ejemplo'
```

- Booleanos: elementos utilizados para poder realizar comprobaciones. Los únicos valores que pueden guardar este tipo de variables son True / False

```py
acierto = False
```

Además de poder asignar las variables de la forma que hemos visto, tambien es posible hacer una asignación múltiple, para ello primero se declarar un luego se les daá el valor de forma conjunta como en el siguiente ejemplo

```py
name, lastName, adress = 'Borja', 'Martin', 'Madrid'
print(name)
```


## Tratamiento de strings

Como hemos visto en la definición de variables, los strings son las palabras. Este tipo de variable tiene un tratamiento muy especial ya que cuenta con multitud de métodos que pueden ser ejecutados. 

```py
letra = 'a'
palabra = 'introducción a python'
palabraMultiple = """ Esto es la escritura de una variable
donde están escritas varias lineas, pero asignadas a la misma variable
"""

print(letra)
print(palabra)
print(palabraMultiple)
```

### Formateo

En el caso de querer concatenar strings, al igual que en el resto de lenguajes de programación, se realiza mediante el operador +. Esta concatención en muchos de los casos es un poco tediosa, siendo mucho mejor utilizar el formateo de string. Para ello se utilizan las banderas %s para string %d para enteros %f para decimales

```py
apellido = 'Martin'
asignatura = 'SGE'
anio = 2023

print('Este repositorio ha sido realizado por %s %s para la asignautar de %s en el año %d' %
      (nombre, apellido, asignatura, anio))
```

A partir de la versión 3 de Pyhton, existe otras formas de formateo mediante la siguiente sintaxis. La primera es mediante el método format

```py
print('Este repositorio ha sido realizado por {} {} para la asignautara de {} en el año {}'.format(nombre, apellido, asignatura, anio))
```

En este caso no es necesario indicar ningún tipo de bandera, sin tener en cuenta los tipos de las variables

Otro de los nuevos métodos de formateo es con la interpolación. Esto se realiza mediante la función f

```py
print(f'Este repositorio ha sido realizado por {nombre} {apellido} para la asignatura de {asignatura} en el año {anio}')
```

### Métodos string

Alguno de los métodos destacados de string son los siguientes: 

- leng(): obtiene la longitud de la palabra indicada

```py
print(f'La longitud de {nombre} es {len(nombre)}')
```

- CharAt: No existe un método como tal, sino que simplemente se trata de un acceso por posición, como si fuese un array.

```py
print(f'La longitura de {nombre} es {len(nombre)}')
letra = nombre[0]  # B
letra = nombre[len(nombre)-1]  # a
```

- Slice: permite obtener un substring de una palabra, indicando el punto de inicio y el punto de final

```py
correo = 'developandsystem@gmail.com'
dominio = correo[correo.index('@'):len(correo)]
```

Como se ha podido ver, todos los elementos indicados no son en realidad método, sino funciones que se pueden aplicar a los elementos de tipo string. Los principales métodos de los elementos de tipo string son los siguientes: 

- capitalize(): Permite pasar la primera letra de un string a mayúsculas

```py
palabraInicial = 'esto es un ejemplo'
print(palabraMultiple.capitalize())  # 'Esto es un Ejemplo'
```

- count(): Obtiene el número de elementos que se indican en el método

```py
frase = 'esta frase está echa para poder buscar todos los elementos de la misma'
print(frase.count('a')) # 8
print(frase.count('es')) # 2
```

- endswith(): Devuelve True o False dependiendo si el string indicado termina con la palabra que se dice

```py
frase = 'esta frase está echa para poder buscar todos los elementos de la misma'
print(frase.endswith("mos")) # false
print(frase.endswith("isma")) # true
```

- find(): Retorna el index de la primera coincidencia encontrada. En caso de no encontrar nada devolverá -1

```py
frase = 'esta frase está echa para poder buscar todos los elementos de la misma'
print(frase.find("f"))  # 5
```

Existen otros métodos como isDigit, isDecimal, isNumeric que pueden ser muy útiles a la hora de evaluar datos. Todos ellos retornan un booleano, indicando si cumple o no la condición de búsqueda

## Operadores

Los operadores en python son

- Asignación: aquellos que permiten asignar valores a variables. Cabe destacar los siguientes
  - =, +=, -=, *=, /=, %=
- Aritméticos: Aquellos que permiten realizar operaciones de suma (+), resta (-), multiplicación (*), división(/), modulo (%) y exponente (**)
- Comparación Aquellos que permiten realizar comprobaciones sobre algun tipo de condición. La salida de estos operadores siempre será un operador booleano. Se pueden destacar las siguientes: igual (==), diferente (!=), mayor (>), mayor igual (>=), menor (<), menor igual (<=)
- Lógicos: Aquellos que permiten juntar el resultado de más de una condición de comparación. Entre estos operadores podemos destacar sobre todo tres: y (and), ó (or)

# Colecciones

Las colecciones son tipos de datos que permiten guardar elementos de forma conjunta en una misma estructura de datos. En Pyhton existen principalmente 4 tipos de colecciones:

- List:se trata de una colección ordenada y de tamaño mutable
- Tupla: se trata de una colección ordenada y de tamaño no mutable 
- Set: se trata de una colección no ordenada, sin indice.
- Diccionario: se trata de una colección no ordenada, modificable e indexada

## Listas

Una lista es un conjunto de datos que se guarda en una variable que representa la estructura de almacenamiento. Para poder definirla se puede hacer de dos formas: 

```py
numeros = [1, 2, 3, 4, 5, 6, 7]
print(numeros)

palabras = list()
```

Una vez creada una lista las operaciones que se pueden hacer son las siguientes

### Acceso a elementos

El acceso a los elementos de una lista se realiza mediante posiciones, sabiendo que la posición del primer elemento siempre será la 0.

```py
numeros = [1, 2, 3, 4, 5, 6, 7]
print(numeros[0])  # 1
print(numeros[len(numeros)-1])  # 7
```
De la misma forma, en python está disponible acceder a los elementos mediante indices negativos, siendo -1 el último elemento

```py
numeros = [1, 2, 3, 4, 5, 6, 7]
print(numeros[-1])  # 7
print(numeros[-len(numeros)])  # 1
```

En el caso de querer hacer un acceso a un subconjunto, tal y como hemos visto con los strings, se podría hacer indicando la posicion inicial y final

```py
numeros = [1, 2, 3, 4, 5, 6, 7]
subconjunto = numeros[2:4]
print(subconjunto) # [3,4]
```

### Modificar elementos a una lista

Para poder modificar elementos en una lista, basta con indicar la posición del elemento que se quiere modificar y asignar el nuevo valor

```py
numeros = [1, 2, 3, 4, 5, 6, 7]
numeros[0] = -1
print(numeros) # [-1, 2, 3, 4, 5, 6, 7]
```

En el caso de querer modificar un subconjunto se podría, indicando el acceso de la misma forma que se ha explicado antes

```py
numeros = [1, 2, 3, 4, 5, 6, 7]
numeros[0:3] = [9, 8, 7]
print(numeros) # [9, 8, 7, 4, 5, 6, 7]
```

### Añadir elementos de una lista

Tal y como se ha dicho al principio, un objeto de tipo list es una colección que tiene un tamaño mutable, por lo que se pueden tanto agregar como eliminar elementos nuevos. Para poder agregarlos se utilizan los métodos append y/o extends, dependiendo de cual sea el número de elementos que se quieran añadir

```py
palabras = list()
palabras.append("Ejemplo")
palabras.append("de")
palabras.append("añadir")
palabras.append("elementos")
print(palabras)
```
ó

```py
palabras = list()
palabras.extend(["Ejemplo", "de", "como", "añadir", "elementos"])
print(palabras)
```
Por último, existe la posibilidad de agregar elementos en posiciones determinadas. Para ello es necesario utilizar el método insert, indicando el elemento a añadir y la posición donde se quiere poner

```py
numeros = [1, 2, 3, 4, 5, 6, 7]
numeros.insert(1, 10)
print(numeros) # [1, 10, 2, 3, 4, 5, 6, 7]
```

Además de estos tres métodos, también se pueden realizar operaciones aritméticas sobre las list. En el caso de utilizar el operados +, las dos list indicadas se sumarán, obteniendo una completa

```py
lista1 = ["primero","segundo","tercero"]
lista2 = ["cuarto","quinto","sexto"]

listaResultante = lista1 + lista2
print(listaResultante) #['primero', 'segundo', 'tercero', 'cuarto', 'quinto', 'sexto']
```

En el caso de utilizar el operados *, el resultado será la repeticion tantas veces come se indique de la lista

```py
lista1 = ["primero", "segundo", "tercero"]
listaResultante = lista1 * 2
print(listaResultante) # ['primero', 'segundo', 'tercero', 'primero', 'segundo', 'tercero']
```

### Borrar elementos de una lista

Para poder borrar los elementos de una lista, existen diferentes posibilidades: 

- la sentencia del, indicando la colección de donde se quiere eliminar y el indice del elemento que se quiere quitar
```py
listaElementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
del listaElementos[2]
print(listaElementos) #['Elemento 1', 'Elemento 2', 'Elemento 4']
```
Una vez borrado el elemento, el resto se movilizan una posición
  
-  Además de la sentencia del, se pueden utilizar los métodos remove y pop. El método remove se basa en eliminar elementos concretos, quitando de la lista el primer elemento que coincidan con la búsqueda. En el caso del método pop, tienen un funcionamiento muy similar a la sentencia del, con la diferencia que ademas de eliminar el elemento, lo devuelve. Además, también se puede 

```py
listaElementos = ["Elemento 1", "Elemento 2",
                  "Elemento 3", "Elemento 4", "Elemento 1"]
listaElementos.remove('Elemento 1')
print(listaElementos) # ['Elemento 2', 'Elemento 3', 'Elemento 4', 'Elemento 1']
```
en el caso del método pop su uso sería el siguiente

```py
listaElementos = ["Elemento 1", "Elemento 2",
                  "Elemento 3", "Elemento 4", "Elemento 1"]
print(f'Elemento {listaElementos.pop(0)} eliminado con éxito') # Elemento Elemento 1 eliminado con éxito
print(listaElementos) # ['Elemento 2', 'Elemento 3', 'Elemento 4', 'Elemento 1']
```

Es importante saber que en el método pop, si no se indica un indice, el elemento que se elimina es el último

### Otras accione elementos en una lista (recorrer, buscar, ordenar)

Para poder recorrer elementos dentro de una lista, se utiliza el bucle for 

```py
for item in listaElementos:
    print(item)
```

Para poder comprobar si un elemento está dentro de la lista, se utiliza la sentencia if in

```py
if 'Elemento 1' in listaElementos:
    print('El elemento está en la lista')
```
Para poder ordenar una lista se utiliza el método sort

```py
listaElementos = ["Elemento 4", "Elemento 2",
                  "Elemento 1", "Elemento 3"]
listaElementos.sort()
print(listaElementos) # ['Elemento 1', 'Elemento 2', 'Elemento 3', 'Elemento 4']
```

# Funciones

Para poder crear una función en Python se utiliza la palabra reservada def, seguida del nombre de la función, los parámetros que necesita y por último :. Esto indica que la función empezará a definir el cuerpo

```py
def funcionImprimir(mensaje):
    print(f'el {mensaje} se ha impreso correctamente')
```

En el caso de que se quiera que la función devuelva algo, la última sentencia de la función será un return

```py
def suma(op1, op2):
    resultado = op1+op2
    print('Suma realizada con éxito')
    return resultado

resultado = suma(4, 9)
print(resultado)  # 13
```
Una cosa importante que hay que tener en cuenta, es que a diferencia de otros lenguajes como por ejemplo javascript, si en la definición de la función se indica que en número de parámetros a pasar es de 2, esta no podrá ser llamada sin menos parámetros

```py
def suma(op1, op2):
    resultado = op1+op2
    print('Suma realizada con éxito')
    return resultado


resultado = suma(4)
# TypeError: suma() missing 1 required positional argument: 'op2'
```

Si se quiere tener la posibilidad de pasar un solo parámetro y que el resto no se pasen, se pueden utilizar los parámetros por defecto, los cuales son utilizados cuando se define la función

```py
multiplicacion(9, 2)  # 18
multiplicacion(9)  # 9
```

En el caso de querer pasar un número de argumentos indeterminado, se utiliza el caracter * para indicar que el número de parámetros será entre 0 y n

```py
def sumarTodos(*elementos):
    sumatorio = 0
    for item in elementos:
        sumatorio += item
    print(
        f'El resultado de sumar todos los elementos pasados es de {sumatorio}')

sumarTodos(1, 4, 5, 6, 7, 3, 1, 0)
```

# Módulos

Los módulos, ayudan a que el código sea mucho más comprensible y escalable, ya que permite independizar en ficheros funciones y/o elementos para que sean reutilizados en diferentes sitos. Para poder crear un módulo basta con crear un archivo py, el cual puede contener variables, funciones, clases y/o ejecutables

Imaginemos el siguiente fichero con tres funciones declaradas

```py
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
```

En el caso de que estas funciones se quieran utilizar en diferentes sitios, deben ser llamadas desde el módulo, por lo que lo primero será importarlo

```py
import modfunciones
```

Una vez hecho esto, todas las funciones y elementos que están declarados dentro del módulo serán accesible a través del nombre del mismo.

```py
import modfunciones
modfunciones.funcionImprimir('Importacion correcta')
lista = modfunciones.obtenerSubconjuntoList([1, 2, 3, 4, 5, 6, 7], 2, 4)
print(lista)
lista = modfunciones.sumarElementosList([], 1, 2, 3)
print(lista)
```

Esta es la importación clásica, pero también podemos renombrar el módulo para que sea más fácil de manejar con la siguiente sintaxis

```py
import modulo as m
```

o también importar solo parte del módulo

```py
from modulo import funcion_general as fun1, funcion_especifica as fun2
```

# Clases

Para poder definir una clase se utiliza la palabra reservada class. En el caso de querer tener un constructor, es necesario utilizar la funcion __init__, la cual actual como constructor. Dentro de ella, existirán tantos parámetros como se consideren necesarios, siendo uno de ellos el parámetro self, el cual ayudará a igualar los elementos a variables de clase

```py
class Producto:
    def __init__(self, nombre, descripcion, precio):

        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio


producto = Producto("Ordenador", "Ordenador personal para trabajar", 1000)

print(producto.nombre)
print(producto.descripcion)
print(producto.precio)

```