import pygame
import random
from queue import PriorityQueue

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
GRID_SIZE = 21  # Must be odd for proper maze generation
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Maze Generator
def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]  # 1 = Wall, 0 = Path
    start = (0, 0)
    stack = [start]

    while stack:
        x, y = stack.pop()
        maze[x][y] = 0
        neighbors = get_neighbors(x, y, maze)
        random.shuffle(neighbors)
        for nx, ny in neighbors:
            if maze[nx][ny] == 1:
                maze[nx][ny] = 0
                maze[(x + nx) // 2][(y + ny) // 2] = 0  # Carve passage
                stack.append((nx, ny))

    return maze

def render_legend(screen):
    font = pygame.font.Font(None, 36)
    text_solve = font.render("Press S: Solve Maze", True, (255, 255, 0))
    text_reset = font.render("Press R: New Maze", True, (255, 255, 0))
    screen.blit(text_solve, (10, SCREEN_HEIGHT - 60))
    screen.blit(text_reset, (10, SCREEN_HEIGHT - 30))

def get_neighbors(x, y, maze):
    neighbors = []
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            neighbors.append((nx, ny))
    return neighbors

# Pathfinding (A* Algorithm)
def a_star(maze, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in get_neighbors_astar(current, maze):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                open_set.put((priority, neighbor))
                came_from[neighbor] = current

    return []

def get_neighbors_astar(position, maze):
    x, y = position
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

# Rendering Functions
def render_maze(screen, maze, player_pos, goal_pos, solution_path=None):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            color = WHITE if maze[x][y] == 0 else BLACK
            pygame.draw.rect(screen, color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(screen, GREEN, (player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (goal_pos[1] * CELL_SIZE, goal_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    if solution_path:
        for x, y in solution_path:
            pygame.draw.rect(screen, YELLOW, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Event Handling
def handle_events(event, player_pos, maze):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and is_valid_move(player_pos, (-1, 0), maze):
            player_pos[0] -= 1
        elif event.key == pygame.K_DOWN and is_valid_move(player_pos, (1, 0), maze):
            player_pos[0] += 1
        elif event.key == pygame.K_LEFT and is_valid_move(player_pos, (0, -1), maze):
            player_pos[1] -= 1
        elif event.key == pygame.K_RIGHT and is_valid_move(player_pos, (0, 1), maze):
            player_pos[1] += 1

def is_valid_move(player_pos, direction, maze):
    x, y = player_pos
    dx, dy = direction
    nx, ny = x + dx, y + dy
    return 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0

# Main Function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("MazeMaster")

    clock = pygame.time.Clock()
    running = True
    maze = generate_maze(GRID_SIZE, GRID_SIZE)
    player_pos = [0, 0]
    goal_pos = [GRID_SIZE - 1, GRID_SIZE - 1]
    solution_path = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handle_events(event, player_pos, maze)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Regenerate maze
                    maze = generate_maze(GRID_SIZE, GRID_SIZE)
                    player_pos = [0, 0]
                    goal_pos = [GRID_SIZE - 1, GRID_SIZE - 1]
                    solution_path = []
                elif event.key == pygame.K_s:  # Solve maze
                    solution_path = a_star(maze, tuple(player_pos), tuple(goal_pos))

        screen.fill(WHITE)
        render_maze(screen, maze, player_pos, goal_pos, solution_path)
        render_legend(screen)  # Add this line to display the legend
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
