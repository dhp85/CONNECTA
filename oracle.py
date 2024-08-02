from enum import Enum, auto
from list_utils import *
from linear_board import *

class ColumnClassification(Enum):
    MAYBE = auto()
    FULL = auto()


class BaseOracle:

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
        if board._columns[indice].is_full():
            clasificacion = ColumnClassification.FULL
        return ColumnRecommendation(indice, clasificacion)    
        

class ColumnRecommendation:
    def __init__(self, indice, clasification):
        self.indice = indice
        self.clasificacion = clasification
           
