__author__ = 'sideth'

import unittest


def existe(raiz, grafo):
    if raiz is not None:

        for k in range(len(grafo.keys())):
            if grafo.keys()[k] is raiz:
                return True
    return False


def num_hojas(raiz, grafo):
    if existe(raiz, grafo):
        if raiz is not None:
            derecha = num_hojas(grafo[raiz]["apuntador_der"], grafo)
            izquierda = num_hojas(grafo[raiz]["apuntador_izq"], grafo)
            if derecha is 0 and izquierda is 0:
                return derecha + izquierda + 1
            else:
                return derecha + izquierda
        else:
            return 0
    else:
        return 0


def add_nodo(raiz, arbol, nodo):
    if arbol.existe(raiz, arbol):
        if raiz is None:
            arbol[raiz] = {"apuntador_izq" : None, "apuntador_der" : None}
        else:
            nodo["apuntador_izq"] = None
            nodo["apuntador_der"] = None
            for k, v in arbol.items():
                if k["apuntador_izq"] is None:
                    if nodo < k:
                        k["apuntador_izq"] = nodo
                    else:
                        if k["apuntador_der"] is None:
                            if nodo > k:
                                k["apuntador_der"] = nodo


def eliminar(arbol={}, nodo={}):
    if arbol.existe(nodo, arbol):
        for k, v in arbol.items():
            if k == nodo:
                arbol.pop(k)
            if arbol[k]["apuntador_izq"] == nodo:
                arbol[k]["apuntador_izq"] = None
            else:
                if arbol[k]["apuntador_der"] == nodo:
                    arbol[k]["apuntador_der"] = None


def es_completo(n):
    if n is not None:
        if n["apuntador_izq"] is not None and n["apuntador_der"] is not None:
            aux1 = es_completo(n["apuntador_izq"])
            aux2 = es_completo(n["apuntador_der"])
            resultado = 0 + aux1 + aux2
            return resultado
        if n["apuntador_izq"] is not None and n["apuntador_der"] is None:
            aux = es_completo(n["apuntador_izq"])
            return aux + 1
        if n["apuntador_izq"] is None and n["apuntador_der"] is not None:
            aux = es_completo(n["apuntador_der"])
            return aux + 1


def recorrido(raiz, default = "pos"):
    if raiz is not None:
        if default == "pre":
            print(raiz)
        recorrido(raiz["apuntador_izq"])
        if default == "in":
            print(raiz)
        recorrido(raiz["apuntador_der"])
        if default == "pos":
            print(raiz)


def espejo(arbol):
    aux1 = arbol
    for k, v in aux1.items():
        aux = v["apuntador_der"]
        v["apuntador_der"] = v["apuntador_izq"]
        v["apuntador_izq"] = aux
    return aux1


arbol = {8: {"apuntador_izq": 3, "apuntador_der": 10}, 3: {"apuntador_izq": 1, "apuntador_der": 6},
             1: {"apuntador_izq": None, "apuntador_der": None}, 6: {"apuntador_izq": 4, "apuntador_der": 7},
             4: {"apuntador_izq": None, "apuntador_der": None}, 7: {"apuntador_izq": None, "apuntador_der": None},
             10: {"apuntador_izq": None, "apuntador_der": 14}, 14: {"apuntador_izq": 13, "apuntador_der": None},
             13: {"apuntador_izq": None, "apuntador_der": None}}

espejoo = {8: {"apuntador_der": 3, "apuntador_izq": 10}, 3: {"apuntador_der": 1, "apuntador_izq": 6},
             1: {"apuntador_der": None, "apuntador_izq": None}, 6: {"apuntador_der": 4, "apuntador_izq": 7},
             4: {"apuntador_der": None, "apuntador_izq": None}, 7: {"apuntador_der": None, "apuntador_izq": None},
             10: {"apuntador_der": None, "apuntador_izq": 14}, 14: {"apuntador_der": 13, "apuntador_izq": None},
             13: {"apuntador_der": None, "apuntador_izq": None}}


class MiPrueba(unittest.TestCase):

    def test_caso1(self):
        self.assertEqual(4, num_hojas(8, arbol))
    def test_caso2(self):
        self.assertEqual(espejoo, espejo(arbol))
    def test_caso3(self):
        self.assertEqual(None, es_completo(arbol[1]))

if __name__=='__main__':
    unittest.main()
