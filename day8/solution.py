visible_trees = 0
def get_input():
    grid = []
    with open("input_file_name") as f:
        for line in f:
            grid.append([int(number) for number in line.strip()])
    return grid

def part1(grid):
    global visible_trees
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tree = grid[i][j]
                    #left                                               #right                                          #above                                  below
            if all(grid[i][l] < tree for l in range(j)) or all(grid[i][r] < tree for r in range(j+1, len(grid[i]))) or all(grid[a][j] < tree for a in range(i)) or all(grid[b][j] < tree for b in range(i + 1, len(grid))):
                visible_trees += 1

    return visible_trees

def part2(grid):
    t = 0
    ans = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tree = grid[i][j]
            L, R, T, B = 0, 0, 0, 0
            #left
            for l in range(j -1, -1,-1):
                L += 1
                if grid[i][l] >= tree:
                    break
            #right
            for r in range(j +1, len(grid[i])):
                R += 1
                if grid[i][r] >= tree:
                    break
            #top
            for t in range(i -1, -1,-1):
                T += 1
                if grid[t][j] >= tree:
                    break
            #bottom
            for b in range(i+1, len(grid)):
                B += 1
                if grid[b][j] >= tree:
                    break
            ans_max = int(L * R * T * B)
            ans.append(ans_max)
            ans.sort()
    return ans[-1]
print('Part1: ',part1(grid=get_input()))
print('Part2: ', part2(grid=get_input()))