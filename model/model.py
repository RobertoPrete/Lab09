import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._nodi = None
        self._archi = None
        self._idMap = {}

    def build_graph(self, soglia):
        self._grafo.clear()
        self._nodi = DAO.getAllAirports()
        self.fillIDMap()
        self._grafo.add_nodes_from(self._nodi)
        self._archi = DAO.getRotte()

        for arco in self._archi:
            w = arco.avgDistance
            a1Object = self._idMap[arco.a1]
            a2Object = self._idMap[arco.a2]
            if w > soglia:
                self._grafo.add_edge(a1Object, a2Object, weight=w)
                print("arco aggiunto", arco)

    def getNumEdges(self):
        return self._grafo.number_of_edges()

    def getNumNodes(self):
        return self._grafo.number_of_nodes()

    def getAllEdges(self):
        return self._grafo.edges

    def fillIDMap(self):
        for n in self._nodi:
            self._idMap[n.ID] = n

    def getAvgDist(self, v1, v2):
        data = self._grafo.get_edge_data(v1, v2)
        return data["weight"]
