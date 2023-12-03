from pprint import pp
from typing import List, Text, Tuple

FNAME = 'input'
BLANK = '.'


def gridCheck(grid: List[List[Text]], x: int, y: int, blank: Text) -> List[Tuple[int, int]]:
    ret = []

    #Primary
    # Up
    if ((y - 1) >= 0):
        if grid[x][y - 1] != blank:
            ret.append((x, y - 1))
    # Down
    if ((y + 1) < len(grid[x])):
        if grid[x][y + 1] != blank:
            ret.append((x, y + 1))
    # Left
    if ((x - 1) >= 0):
        if grid[x - 1][y] != blank:
            ret.append((x - 1, y))
    # Right
    if ((x + 1) < len(grid)):
        if grid[x + 1][y] != blank:
            ret.append((x + 1, y))

    # Diagonal
    # Up-Left
    if ((y - 1) >= 0) and ((x - 1) >= 0):
        if grid[x - 1][y - 1] != blank:
            ret.append((x - 1, y - 1))
    # Up-Right
    if ((y - 1) >= 0) and ((x + 1) < len(grid)):
        if grid[x + 1][y - 1] != blank:
            ret.append((x + 1, y - 1))
    # Down-Left
    if ((y + 1) < len(grid[x])) and ((x - 1) >= 0):
        if grid[x - 1][y + 1] != blank:
            ret.append((x - 1, y + 1))
    # Down-Right
    if ((y + 1) < len(grid[x])) and ((x + 1) < len(grid)):
        if grid[x + 1][y + 1] != blank:
            ret.append((x + 1, y + 1))

    return ret

def expandNumber(grid: List[List[Text]], x: int, y: int):
    ret = 0
    # Look left until blank, look right until blank, or end
    vals = []

    #print('\t\t', x, y, "--", grid[x][y])
    ty = y
    ny = y
    while ty >= 0:
        if str.isnumeric(grid[x][ty]):
            vals.insert(0, grid[x][ty])
        else:
            break
        ty = ty - 1
        ny = ny - 1 # use left most point as anchor

    ty = y + 1
    while ty < len(grid):
        if str.isnumeric(grid[x][ty]):
            vals.append(grid[x][ty])
        else:
            break
        ty = ty + 1

    ret = int(''.join(vals))
    return ret, (x, ny)

data: List[Text] = []
with open(FNAME) as f:
    data = f.read().splitlines()

parsed_data: List[List[Text]] = [list(d) for d in data]
#pp(parsed_data)

vals = {}

for x in range(len(parsed_data)):
    for y in range(len(parsed_data[x])):
        
        if (not str.isnumeric(parsed_data[x][y])) and parsed_data[x][y] !=  BLANK:
            n = gridCheck(parsed_data, x, y, BLANK)
            #pp([n, x, y, parsed_data[x][y]])
            for neighbor in n:
                #pp(f"\t {parsed_data[neighbor[0]][neighbor[1]]}")
                nn, pos = expandNumber(parsed_data, neighbor[0], neighbor[1])
                vals[pos] = nn

total = 0 
for _, v in vals.items():
    total = total + v
pp(total)
