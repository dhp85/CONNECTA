from enum import Enum, auto
from list_utils import *
from linear_board import *

class ColumnClassification(Enum):
    MAYBE = auto()
    FULL = auto()

class ColumnRecommendation():
    def __init__(self, indice, clasification):
        self.indice = indice
        self.clasificacion = clasification
    
    def __eq__(self, other):
        # si son de clases distintas, pues distintos.
        if not isinstance(other, self.__class__):
            return False
        # si son de la misma clase, pues comparo las propiedades de uno y otro.
        else:
            return (self.indice, self.clasificacion) == (other.indice, other.clasificacion)
        
    def __hash__(self) -> int:
        return hash((self.indice, self.clasificacion))  
        
class BaseOracle():

    def get_recommendation(self, board, player):
        """
        Devuelve un lista de instancias de ColumnRecomendation:
        """

        rc = []
        for i in range(len(board)):
            rc.append(self._get_column_recommendation(board, i, player))
        return rc    
    
    def _get_column_recommendation(self, board, indice, player):
        
        """
        Clasifica una columna ya sea como FULL o MAYBE y devuelve
        una ColumnRecomendation 
        """

        clasificacion = ColumnClassification.MAYBE
        if board._column[indice].is_full():
            clasificacion = ColumnClassification.FULL
        return ColumnRecommendation(indice, clasificacion)    
        


           
