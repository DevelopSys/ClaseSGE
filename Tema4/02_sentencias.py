numero = 7
match numero:
    case 1:
        print("valor 1")
    case 2:
        print("valor 2")
    case 3:
        print("valor 3")
    case _:
        print("valor no contemplado")

if numero == 0:
    print("numero es 0")
elif numero < 5:
    print("numero entre 1 y 4")
elif numero < 9:
    print("numero entre 5 y 8")
else:
    print("numero 9 o 10")
