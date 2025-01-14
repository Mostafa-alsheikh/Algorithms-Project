import sys
import time

from Drawing_Board import DrawingBoard
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def Depth_First_Search(graph, start, draw: DrawingBoard):
    visited = []
    stack = [start]

    def process_node():
        draw.paintAllNodes("white")
        for node in visited:
            draw.paintNodeOutline(node, "grey")
            draw.paintNodeFill(node, "grey")
        if stack:
            node = stack.pop()
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
                        stack.append(neighbour)

            QTimer.singleShot(2000, process_node)  # Schedule the next call
        else:
            print("finished search")

    process_node()  # Start the process

    loop = QEventLoop()   # wait time for the process to finish
    QTimer.singleShot(2000, loop.quit)
    loop.exec_()

    return visited

