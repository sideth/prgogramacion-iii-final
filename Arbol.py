__author__ = 'sideth'

import unittest

class Arbol:
    def __init__(self, raiz):
        self._raiz = raiz

    def existe(self, raiz, grafo):
        if raiz is not None:

            for k in range(len(grafo.keys())):
                if grafo.keys()[k] is raiz:
                    return True
        return False

    def num_hojas(self, raiz, grafo):
        if self.existe(raiz, grafo):
            if raiz is not None:
                derecha = self.num_hojas(grafo[raiz]["apuntador_der"], grafo)
                izquierda = self.num_hojas(grafo[raiz]["apuntador_izq"], grafo)
                if derecha is 0 and izquierda is 0:
                    return derecha + izquierda + 1
                else:
                    return derecha + izquierda
            else:
                return 0
        else:
            return 0

class MiPrueba():
    mArbol = Arbol(8)

    arbol = {8: {"apuntador_izq": 3, "apuntador_der": 10}, 3: {"apuntador_izq": 1, "apuntador_der": 6},
             1: {"apuntador_izq": None, "apuntador_der": None}, 6: {"apuntador_izq": 4, "apuntador_der": 7},
             4: {"apuntador_izq": None, "apuntador_der": None}, 7: {"apuntador_izq": None, "apuntador_der": None},
             10: {"apuntador_izq": None, "apuntador_der": 14}, 14: {"apuntador_izq": 13, "apuntador_der": None},
             13: {"apuntador_izq": None, "apuntador_der": None}}

    print "numero de hojas: ", mArbol.num_hojas(8, arbol)