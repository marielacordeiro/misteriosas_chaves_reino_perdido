import os
import sys
sys.setrecursionlimit(50000)


def read_file(test_case: str):
    lines = []
    with open(f'casos-cohen/{test_case}') as f:
        for line in f:
            lines.append(list(line.strip()))
    return lines


def find_players(list):
    players = {}
    # this function will find the players and keep their coordinates
    for x in range(len(list)-1):
        for y in range(len(list[0])):
            if list[x][y].isnumeric():
                number = int(list[x][y])
                players[number] = x, y
            if y == len(list[0])-1:
                break
    return players


def print_field(list):
    for y in range(len(list)):
        for x in range(len(list[0])):
            # value by column and row
            print(list[y][x], end=' ')
            if x == len(list[0])-1:
                # print a new line at the end of each row
                print('\n')


def flood_fill(x, y, dot, door_keys, doors):
    # make sure the x and y are inbounds
    if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[0]):
        return

    # check if the current position has already been visited
    if vis[x][y] == 1:
        return

    # check if the current position equals the desirable value
    if lines[x][y] != dot:
        position = lines[x][y]
        if position.isalpha():
            if position.islower():
                door_keys.add(position)
                if position.upper() in doors.keys():
                    vis[x][y] = 0
                    flood_fill(doors[position.upper()][
                        0], doors[position.upper()][1], dot, door_keys, doors)
            elif position.lower() not in door_keys:
                doors[position] = x, y
                return
        elif position.isnumeric():
            pass
        else:
            return

    # thirdly, set the current position to visited and increment the positions visited
    vis[x][y] = 1
    global curr_size
    curr_size += 1

    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, dot, door_keys, doors)
    flood_fill(x-1, y, dot, door_keys, doors)
    flood_fill(x, y+1, dot, door_keys, doors)
    flood_fill(x, y-1, dot, door_keys, doors)

    return curr_size


if __name__ == "__main__":
    print(sys.getrecursionlimit())
    results = {}
    for file in os.listdir('casos-cohen'):
        if file not in results:
            results[file] = []
        lines = read_file(file)
        players = find_players(lines)
        for x, y in players.items():
            curr_size = 0
            door_keys = set()
            doors = {}
            vis = [[0 for _ in range(len(lines[0]))]
                   for _ in range(len(lines))]
            path_size = flood_fill(y[0], y[1], ".", door_keys, doors)
            results[file].append((x, path_size))
            print()
            print(
                f'caso de teste: {file} \t player: {x} \t casinhas exploradas: {path_size}')

    """ print()
    [print(f'caso de teste: {k} \t player: {v} \t casinhas exploradas: {v}')
     for k, v in results.items()]
    print() """
