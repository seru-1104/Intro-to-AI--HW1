# Coded by [Saranya Chakravarthy Korrapati]
# CS 580: Introduction to Artificial Intelligence
# H1: A* Search Algorithm for Maze Solving

from pyamaze import maze, agent, textLabel
import heapq
import math

def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) # this helps to calculate the Euclidean distance between 2 points

def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) #this helps to calculate the Manhattan distance between 2 points

def astar(m):
    start = (m.rows, m.cols)
    goal = (1, 1)

    open_li = []
    heapq.heappush(open_li, (0, 0, start))

    closed_set = set() # this helps to keep track of all the visited nodes
    came_from = {} # this helps in Storing the parent of each node for path reconstruction

    g_cost = {start: 0}

    while open_li:
        current_f, current_g, current_cell = heapq.heappop(open_li)
        if current_cell in closed_set:
            continue

        closed_set.add(current_cell)

        if current_cell == goal:
            path = {}
            current = goal
            while current in came_from:
                parent = came_from[current]
                path[parent] = current
                current = parent
            return path


        for direction in 'EWSN': # this helps to explore neighbors in all four directions
            if m.maze_map[current_cell][direction]:
                # this helps in Calculating neighbor coordinates based on direction
                if direction == 'E':
                    neighbor = (current_cell[0], current_cell[1] + 1)
                elif direction == 'W':
                    neighbor = (current_cell[0], current_cell[1] - 1)
                elif direction == 'S':
                    neighbor = (current_cell[0] + 1, current_cell[1])
                elif direction == 'N':
                    neighbor = (current_cell[0] - 1, current_cell[1])

                if neighbor in closed_set:
                    continue

                tentative_g = euclidean_dist(start, neighbor)

                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                    came_from[neighbor] = current_cell
                    g_cost[neighbor] = tentative_g

                    h_cost = manhattan_dist(neighbor, goal)
                    f_cost = tentative_g + h_cost
                    heapq.heappush(open_li, (f_cost, tentative_g, neighbor))

    return {}

def main():
    rows, cols = 5, 5
    m = maze(rows, cols)
    m.CreateMaze()
    path = astar(m)
    a = agent(m, footprints=True)
    m.tracePath({a: path})
    l = textLabel(m, 'Path Length', len(path) + 1)
    m.run()

if __name__ == "__main__":
    main()