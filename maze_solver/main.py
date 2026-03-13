import random

ROWS = 10
COLS = 10

WALL = "#"
PATH = " "
START = "S"
END = "E"
VISITED = "*"


def create_maze():

    maze = []

    for i in range(ROWS):
        row = []
        for j in range(COLS):
            if i == 0 or j == 0 or i == ROWS-1 or j == COLS-1:
                row.append(WALL)
            else:
                if random.random() > 0.3:
                    row.append(PATH)
                else:
                    row.append(WALL)

        maze.append(row)

    maze[1][1] = START
    maze[ROWS-2][COLS-2] = END

    return maze


def print_maze(maze):

    for row in maze:
        print(" ".join(row))


def solve_maze(maze, x, y, visited):

    if x < 0 or y < 0 or x >= ROWS or y >= COLS:
        return False

    if maze[x][y] == WALL or (x, y) in visited:
        return False

    if maze[x][y] == END:
        return True

    visited.add((x, y))

    if maze[x][y] != START:
        maze[x][y] = VISITED

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for dx, dy in directions:

        if solve_maze(maze, x+dx, y+dy, visited):
            return True

    return False


def main():

    print("Generating Maze...\n")

    maze = create_maze()

    print("Generated Maze:\n")
    print_maze(maze)

    visited = set()

    solve_maze(maze, 1, 1, visited)

    print("\nSolved Maze:\n")
    print_maze(maze)


if __name__ == "__main__":
    main()