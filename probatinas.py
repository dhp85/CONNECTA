

matriz = [[0, 1, 2, 3], [0, 1, 2, 3]]

def reverse_list(l):
    """
    Funcion que recibe una lista y la invierte
    """
    rev = list(reversed(l))
    return rev


def reverse_matriz(lol):
    """
    Funcion que invierte lista de listas.
    """

    """mv= []
    for l in lol:
        mv.append(reverse_list(l))
    return mv
    """

    return list(map(reverse_list, lol))    

print(reverse_matriz(matriz))    