
def find_one(list, needle):
    """
    Devuelve True si encuentra una o mas ocurrencias de needle en list
    """
    return find_n(list, needle, 1)     



"""
def find_n(list, needle, n):

    
    Devuelve True si en list hay n o mas ocurrencias de needle,
    False si hay menos o si n < 0.
    

    result = False
    count = 0

    if n >= 0:
        result = False
        
    
        for element in list:
            if element == needle:
                count += 1
               if count >= n:
                    result = True
                else:
                    result = False          
    return result
    """


def find_n(list, needle, n):

    """
    Devuelve True si en list hay n o mas ocurrencias de needle,
    False si hay menos o si n < 0.
    """
    result = False
    # si n < 0 devolvemos False.
    if n >= 0:
        result = False
    # Iniciamos el indice y el contador.
        indice = 0
        count = 0
      # Mientras no hayamos encontrado el elemento n veces o no hayamos terminado la lista.
        while count < n and indice < len(list):  
     # Si lo encontramos, actualizamos el contador.
            if list[indice] == needle:
                count += 1
                 
    # Avanzamos al siguiente elemento.
            indice += 1  
    # devolvemos el resultado de comparar contador con n.
        return count >= n
    else:
        return False
       
def find_streak(list, needle, nstrike):  
    """
    Devuelve True si en lista hay n o mas needles seguidos False, para todos los demas.
    """
    # si n >= 0.
    if nstrike >= 0:
    # inicializo el indice el contador y el indicador de racha.
        indice = 0
        count_strike = 0
    # mientras no haya encontrado n seguidos y la lista no se haya acabado.
        while count_strike < nstrike and indice < len(list):
    # si lo encuentro, activo el indicador de rachas y actualizo el contador.
            if needle == list[indice]:
                count_strike += 1
    # si no lo encuentro, desactivo indicador de racha y pongo a cero el contador.
            else:
                count_strike = 0
    # avanzo al siguiente elemento.
            indice += 1
    # devolvemos el resultado de comparar el contador con n SIEMPRE Y CUANDO estemos en racha.        
        return count_strike == nstrike     
    else:
        return False
    
def first_elements(matriz):
    """
    Recibe una lista de listas y devuelve
    una lista con los primeros elementos de la original
    """

    return nth_elements(matriz, 0)  

def nth_elements(lol, n):

    """
    Recibe una lista de listas y devuelve
    una lista con los enésimos elementos de la original.
    """

    acumm = []

    for lista in lol:
        acumm.append(lista[n])
    return acumm    


def transpose(matriz): 
    """
    Recibe una matriz y devuelve su transpuesta
    """       
    """
    ac = []
    
    for lista in matriz:
        i = 0
        while i < len(lista):
            ac.append(nth_elements(matriz, i))
            i += 1 
    return ac
    """
    ac = []
    for i in range(len(matriz[0])):
        ac.append(nth_elements(matriz, i))
    return ac    

def displace(l, distance, filler=None):
    if distance == 0:
        return l
    elif distance > 0:
        filling = [filler] * distance
        res = filling + l
        res = res[:-distance]
        return res
    else:
        distance = distance * -1
        filling = [filler] * distance
        res = l + filling
        res = res[distance:]
        return res
        
def displace_board(matriz, filler=None):

    # Ceamos una matriz vacia.
    m = []
    i = 0
    # por cada columna de la matriz original la desplazamos su indice -1.
    while i < len(matriz):
    # añadimos la columna desplazada a m
        m.append(displace(matriz[i], i - 1, filler))
        i += 1
    # devolvemos m
    return m


        


