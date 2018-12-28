import time


def maxIncreaseKeepingSkyline(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    lr = []
    tb = []
    sum = 0
    for i in range(m):
        lr.append(max(grid[i]))
        tb.append(max([grid[k][i] for k in range(m)]))
    for i in range(m):
        for j in range(m):
            sum += (min(lr[i],tb[j]) - grid[i][j])
    return sum

def maxIncreaseKeepingSkyline2(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    tb = []
    sum = 0
    for i in range(m):
        tb.append(max([grid[k][i] for k in range(m)]))
    for i in range(m):
        for j in range(m):
            sum += (min(max(grid[i]),tb[j]) - grid[i][j])
    return sum