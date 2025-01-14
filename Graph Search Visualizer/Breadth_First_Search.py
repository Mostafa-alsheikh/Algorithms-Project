from Drawing_Board import DrawingBoard
from PyQt5.QtCore import *
def Breadth_First_Search(graph, start, draw: DrawingBoard):
    visited = []
    queue = [start]
    def process_node():
        draw.paintAllNodes("white")
        for node in visited:
            draw.paintNodeOutline(node, "grey")
            draw.paintNodeFill(node, "grey")
        if queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                neighbours = graph[node]
                draw.paintNodeFill(node, "darkRed")  # current node
                print(node) # not important
                print("---------") # not important
                for neighbour in neighbours:
                    if neighbour not in visited:
                        draw.paintNodeOutlineAndLetter(neighbour, "green", "darkGreen") # neighbour node
                        print(neighbour) # not important
                        queue.append(neighbour)
            QTimer.singleShot(2000, process_node)  # Schedule the next call
        else:
            print("finished search")

    process_node()  # Start the process
    loop = QEventLoop()   # wait time for the process to finish
    QTimer.singleShot(2000, loop.quit)
    loop.exec_()

    return visited


