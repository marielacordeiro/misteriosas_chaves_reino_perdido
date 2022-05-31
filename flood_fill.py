lines = []
curr_size = 1

with open("casos-cohen/caso04.txt") as f:
    for line in f:
        lines.append(list(line.strip()))


def print_field():
    # this function will print the content of the array to the console
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            # value by column and row
            print(lines[y][x], end=' ')
            if x == len(lines[0])-1:
                # print a new line at the end of each row
                print('\n')


vis = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]


def flood_fill(x, y, dot, door_keys):
    # we need the x and y of the start position, the old value,
    # and the new value

    # the flood fill has 4 parts

    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
        return

    # secondly, check if the current position equals the old value
    if lines[x][y] != dot:
        if lines[x][y].isalpha():
            if lines[x][y].islower():
                door_keys.add(lines[x][y])
            else:
                lines[x][y].lower() not in door_keys
                return
        else:
            return

    if vis[x][y] == 1:
        return

    # thirdly, set the current position to the new value
    vis[x][y] = 1
    global curr_size
    curr_size += 1

    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, dot, door_keys)
    flood_fill(x-1, y, dot, door_keys)
    flood_fill(x, y+1, dot, door_keys)
    flood_fill(x, y-1, dot, door_keys)

    return curr_size


if __name__ == "__main__":
    # print field before the flood fill
    # print_field()

    door_keys = set()

    # cases 15, 16
    points = flood_fill(16, 15, ".", door_keys)

    print("Doing flood fill with ")

    # print the field after the flood fill
    # print_field()

    print(points)
