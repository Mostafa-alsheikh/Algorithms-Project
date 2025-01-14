# Graph Search Visualizer

This project aims to visualize and demonstrate various graph search algorithms, providing insights into their performance and behavior. The goal is to develop a tool that allows the user to interactively explore different graph traversal techniques, such as Depth-First Search (DFS), Breadth-First Search (BFS), and other advanced search algorithms.

## Evaluation Criteria

This project was designed and implemented keeping in mind the following evaluation criteria:

### 1. Problem Understanding
We carefully analyzed the problem statement and aimed to create a clear and interactive visualizer that showcases the core concepts of graph search algorithms. The problem understanding is reflected in the implementation of basic algorithms, followed by optimization techniques where applicable.

### 2. Algorithm Design
The algorithms implemented include:
- **Breadth-First Search (BFS)**: Explores all nodes at the present depth level before moving on to nodes at the next depth level.
- **Depth-First Search (DFS)**: Explores as far down a branch of the graph as possible before backtracking.
- **Dijkstra’s Algorithm**: A pathfinding algorithm used to find the shortest path between nodes in a graph.
- **A* Algorithm**: A heuristic-based pathfinding algorithm for optimal graph traversal.

Each algorithm was chosen to showcase different types of search strategies, and their time complexity, space complexity, and correctness were considered during the design process.

### 3. Algorithm Analysis
We performed both theoretical and empirical analysis of the algorithms:
- **Time Complexity**: We analyzed and compared the time complexity of each algorithm (e.g., O(V + E) for BFS and DFS).
- **Space Complexity**: We analyzed memory usage based on graph representation (adjacency matrix vs adjacency list).
- **Experimental Evaluations**: We conducted tests on various graph sizes to observe the performance in terms of execution time and memory usage.

### 4. Optimization Techniques
While basic search algorithms are implemented, optimization techniques like **A* Search** and **Greedy Algorithms** are also included, enhancing algorithm performance in specific use cases. These techniques were tested on practical graphs to measure their efficiency.

### 5. Correctness and Completeness
The algorithms have been tested on various graph types (directed, undirected, weighted, and unweighted) to ensure correctness. Edge cases such as disconnected graphs, cyclical graphs, and graphs with negative edge weights (where applicable) were also handled.

### 6. Clarity of Explanation
Each algorithm was explained in detail in both the code comments and the project report. The report outlines:
- **Algorithm Design Choices**: Why each algorithm was chosen and its application.
- **Implementation Details**: How the algorithms are implemented and how they interact with the graphical interface.
- **Performance Analysis**: Discussion on the observed time and space complexity, and practical considerations for selecting an algorithm based on the graph size and nature.

### 7. Code Quality
The project follows best practices in coding, including:
- **Readability**: Clear, consistent naming conventions and code structure.
- **Modularity**: Code is modular with well-defined functions for each algorithm.
- **Documentation**: In-depth comments and docstrings explaining the functionality of each function and class.
- **Error Handling**: Proper handling of invalid inputs and edge cases.

### 8. Presentation Skills
The project was presented to highlight the following:
- Clear and concise explanations of the graph search algorithms and their applications.
- Interactive visualizations that allow the user to observe how each algorithm works on different graphs.
- Performance metrics to support the theoretical analysis.

## Project Structure

- **`/src`**: Contains the source code files for the algorithms and visualization tools.
- **`/assets`**: Contains assets for the visualizations (e.g., graph images, UI components).
- **`/docs`**: Documentation and project reports.
- **`/tests`**: Unit tests for algorithm correctness and performance.
- **`README.md`**: This file.

## Getting Started

To run the project locally, follow the steps below:

### Prerequisites
- Python 3.x
- Install the required libraries:
  ```bash
  pip install pygame networkx matplotlib
