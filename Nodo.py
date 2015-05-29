__author__ = 'sideth'
class Nodo:

    def __init__(self, info):
        self._info = info
        self._derecha = None
        self._izquierda = None

    @property
    def info(self):
        return self._info

    @property
    def derecha(self):
        return self._derecha

    @property
    def izquierda(self):
        return self._izquierda