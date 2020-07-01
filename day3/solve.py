# I actually needed help from https://www.youtube.com/watch?v=tMPQp60q9GA on this

# open and read file: R8,U5,L5,D3
A, B, _ = open('input.txt').read().split('\n')

# parse them into a list: ['R8', 'U5', 'L5', 'D3']
A, B = [x.split(',') for x in [A, B]]

# lookup tables
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

def get_points(A):
    x = 0
    y = 0

    # this is unsorted, but this doens't matter
    # the only thing we are interested in is, that it's a set
    visited_path = set()

    # A === ['R8', 'U5', 'L5', 'D3']
    for cmd in A:
        dir = cmd[0]
        assert dir in ['L', 'R', 'U', 'D']
        num = int(cmd[1:])
        for _ in range(num):
            x += DX[dir]
            y += DY[dir]
            print("Adding {x:", x, ", y:", y, "} to visited path")
            visited_path.add((x, y))
        print("Command cmd:", cmd, "finished")
    return visited_path

PA = get_points(A)
print("Answer for A:", A, "is:", PA)

PB = get_points(B)
print("Answer for B:", B, "is:", PB)

# & both list of sets to get the sets which appear in both lists
both = PA & PB
print("Both:", both)

# add up x+y for each cross locations to look for the smallest value
# this basically is what the "Manhattan Distance" means
ans = min([abs(x)+abs(y) for (x, y) in both])
print(ans)