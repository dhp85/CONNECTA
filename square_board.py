from linear_board import *
from list_utils import transpose, displace, displace_board

class SquareBoard():
    """
    Representa un tablero cuadrado
    """
    @classmethod
    def fromList(cls, list_of_lists):
        """
        Transforma una lista de listas en una list de LinearBoard
        """

        board = cls()
        board._column = list(map(lambda element: LinearBoard.fromList(element), list_of_lists))
        return board
    
    def __init__(self):
        self._column = [LinearBoard() for i in range(BOARD_LENGHT)]

    def is_full(self):
        """
        True si todos los LinearBoards estan llenos
        """

        result = True
        for lb in self._column:
            result = result and lb.is_full()
        return result    
    
    def as_matriz(self):
        """
        Devuelve una representacion en formato de matriz, es decir, lista de listas
        """
        matriz = []
        for lb in self._column:
            matriz.append(lb._column)
        return matriz

    # Detectar victorias
    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)
    
    def _any_vertical_victory(self,char):
        
        result = False
        for lb in self._column:
            result = result or lb.is_victory(char)
        return result

    def _any_horizontal_victory(self, char):
        # Transponemos _columns.
        transp = transpose(self.as_matriz())
        # Creamos un talbeero temporal con esa matriz transpuesta.
        tmp = SquareBoard.fromList(transp)
        # comprobamos si tiene una victoria temporal.
        return tmp._any_vertical_victory(char)
    
    def _any_rising_victory(self, char):
        pass
    
    def _any_sinking_victory(self, char):
        # obtenemos las columnas como una matriz.
        matriz = self.as_matriz()
        # la desplazamos.
        matriz_desplazada = displace_board(matriz, filler=None)
        # creamos un tablero temporal con esa matriz.
        tmp = SquareBoard.fromList(matriz_desplazada)
        # averiguamos si tiene una victoria horizontal.
        return tmp._any_horizontal_victory(char)

        
    
    # dunders

    def __repr__(self):
        return f"{self.__class__}:{self._column}"

