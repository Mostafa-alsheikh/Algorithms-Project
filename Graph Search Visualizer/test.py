class Dictionary:
    dictionary = {}

    @classmethod
    def addNode(cls, nodeName):
        if nodeName not in cls.dictionary:
            cls.dictionary[nodeName] = []

    def addEdge(cls, node1, node2):
        if node1 in cls.dictionary and node2 in cls.dictionary:
            cls.dictionary[node1].append(node2)
            cls.dictionary[node2].append(node1)

    def addEdgeWithWeight(cls, node1, node2, weight):
        if node1 in cls.dictionary and node2 in cls.dictionary:
            if (node2, weight) not in cls.dictionary[node1]:
                cls.dictionary[node1].append((node2, weight))
            if (node1, weight) not in cls.dictionary[node2]:
                cls.dictionary[node2].append((node1, weight))

    def convertEdgeToWeighted(cls, node1, node2, weight):
        if node1 in cls.dictionary and node2 in cls.dictionary:
            for edge in cls.dictionary[node1]:
                if edge == node2:
                    cls.dictionary[node1].remove(edge)
                    cls.dictionary[node1].append((node2, weight))
            for edge in cls.dictionary[node2]:
                if edge == node1:
                    cls.dictionary[node2].remove(edge)
                    cls.dictionary[node2].append((node1, weight))

    def copyUnweightedAndConvertToWeightedGraph(cls, graph):
        newGraph = {}
        for node in cls.dictionary:
            newGraph[node] = []
        added_edges = set()
        for node in cls.dictionary:
            for edge in cls.dictionary[node]:
                if (node, edge) not in added_edges and (edge, node) not in added_edges:
                    newGraph[node].append((edge, 1))
                    newGraph[edge].append((node, 1))  # Add the edge in the opposite direction
                    added_edges.add((node, edge))
        return newGraph

    def allEdgesHaveWeights(cls):
        for node in cls.dictionary:
            for edge in cls.dictionary[node]:
                if not isinstance(edge, tuple):
                    return False
        return True

    def getDictionary(cls):
        return cls.dictionary

    def nodeNameExists(cls, nodeName):
        return nodeName in cls.dictionary

    def edgeExists(cls, node1, node2):
        if node1 in cls.dictionary:
            return node2 in cls.dictionary[node1]
        return False

    def edgeWeightExists(cls, node1, node2):
        if node1 in cls.dictionary:
            for edge in cls.dictionary[node1]:
                if isinstance(edge, tuple) and edge[0] == node2:
                    return True
        return False


# Example usage
if __name__ == "__main__":
    graph = Dictionary()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addEdge('A', 'B')
    graph.addEdge('A', 'C')

    print("Original graph:", graph.getDictionary())

    weighted_graph = graph.copyUnweightedAndConvertToWeightedGraph(graph)
    print("Converted weighted graph:", weighted_graph)
