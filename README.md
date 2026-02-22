# Maze Solver and Generator

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://github.com/JPGBMR/maze-master)
A Python application that generates random mazes and solves them using the A* pathfinding algorithm. Built with Pygame, this program offers interactive gameplay where users can navigate a maze, regenerate it, or let the program solve it.

## Features
- **Maze Generation**: Generates a random maze using depth-first search.
- **Player Movement**: Navigate the maze manually using arrow keys.
- **Pathfinding**: Solve the maze using the A* algorithm.
- **Interactive Controls**:
  - `Arrow Keys`: Move the player.
  - `S`: Solve the maze.
  - `R`: Generate a new maze.
- **Dynamic Rendering**: Visualizes the maze, player, goal, and solution path.

## Installation

### Prerequisites
- Python 3.x installed on your system.
- Pygame library installed. Install it via pip:
  ```bash
  pip install pygame
  ```

## Usage
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the application:
   ```bash
   python main.py
   ```

## Controls
- **Arrow Keys**: Move the player.
- **R**: Regenerate the maze.
- **S**: Solve the maze.

## How It Works
1. **Maze Generation**: The program creates a grid-based maze using depth-first search.
2. **Pathfinding**: The A* algorithm finds the shortest path from the player's position to the goal.
3. **Rendering**: The maze is rendered with Pygame, featuring dynamic visuals for the player, goal, and solution path.

## Contributing
Feel free to fork the repository, open issues, or submit pull requests to improve the project.

---
**Enjoy solving and navigating mazes with this interactive application!**


## Getting Started

```bash
pip install -r requirements.txt
python main.py
```

---
*Part of the [JPGBMR](https://github.com/JPGBMR) open-source portfolio.*
