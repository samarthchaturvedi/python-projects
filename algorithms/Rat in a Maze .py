# Rat in a maze problem

def solve_maze(maze, x, y, path, n):
    if x == n-1 and y == n-1:
        path[x][y] = 1
        for row in path:
            print(row)
        print()
        return
    
    if x < 0 or y < 0 or x >= n or y >= n or maze[x][y] == 0 or path[x][y] == 1:
        return
    
    path[x][y] = 1
    
    solve_maze(maze, x+1, y, path, n)
    solve_maze(maze, x, y+1, path, n)
    
    path[x][y] = 0

n = int(input("Enter size of maze: "))

maze = []
print("Enter maze (0 or 1):")
for i in range(n):
    maze.append(list(map(int, input().split())))

path = [[0]*n for _ in range(n)]

solve_maze(maze, 0, 0, path, n)