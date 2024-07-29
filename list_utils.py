
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
       
