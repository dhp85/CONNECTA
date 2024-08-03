from oracle import *

class Player:

    def __init__(self, name, char, oracle = BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle

    def play(self, board):
        """
        Elige mejor columna de aquellas que recomienda el oráculo.
        """    

        # obten las recomendaciones.
        # selecciona la mejor de todas.
        # juega en ella.
        pass

    def _chose(self, recommendations):
        # selecciona la mejor opcion de la lista de recomendaciones.
        pass