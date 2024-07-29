from settings import *

class LinearBoard:
    """
    Clase que representa un tablero de una sola columna.
    x un jugador
    o otro jugador
    None un espacio vacio
    """

    def __init__(self):
        """
        Una lista de None
        """
        self._column = [None for i in range(BOARD_LENGHT)]

    def add(self, char):
        """
        Juega en la primera posicion disponible
        """
    # buscamos la primera posicion libre.
        if not self.is_full():
            i = self._column.index(None)
            # lo sustituimos por char.
            self._column[i] = char 
    
    
    def is_full(self):
        return self._column[-1] != None

    
    def is_victory(self, char):
        result = False
        for i in range(VICTORY_STRIKE):
            if self._column[i] == char:
              result = True
            else:
                return result  
    
    def is_tie(self, char1, char2):
        """
        no hay victoria de char1 ni de char2
        """

        return (self.is_victory(char1) == False) and (self.is_victory(char2) == False)


        
    
 
