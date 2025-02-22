from PyQt5.QtCore import QTimer, QEventLoop
from Drawing_Board import DrawingBoard

def Bellman_Ford_algorithm(graph, start, draw: DrawingBoard):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    edges = [(u, v, w) for u in graph for v, w in graph[u]]
    visited = []

    def process_iteration(iteration):
        draw.paintAllNodes("white")
        for node in visited:
            draw.paintNodeOutline(node, "grey")
            draw.paintNodeFill(node, "grey")

        if iteration < len(graph) - 1:
            for u, v, w in edges:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    if v not in visited:
                        visited.append(v)
                        draw.paintNodeOutlineAndLetter(v, "green", "darkGreen")

            QTimer.singleShot(2000, lambda: process_iteration(iteration + 1))
        else:
            print("finished search")
            for u, v, w in edges:
                if distance[u] + w < distance[v]:
                    print("Graph contains a negative weight cycle")
                    return

    process_iteration(0)

    loop = QEventLoop()
    QTimer.singleShot(2000, loop.quit)
    loop.exec_()
    print(distance)
    return distance
