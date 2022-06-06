import os
import sys
sys.setrecursionlimit(15000)


def read_file(test_case: str):
    matrix = []
    with open(f'casos-cohen/{test_case}') as f:
        for line in f:
            matrix.append(list(line.strip()))
    return matrix


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
    #  function that traverses the array and prints any list wanted
    for y in range(len(list)):
        for x in range(len(list[0])):
            print(list[y][x], end=' ')
            if x == len(list[0])-1:
                print('\n')


def flood_fill(x, y, dot, door_keys, doors):

    global pos_visited

    # make sure the x and y are inbounds
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return

    # check if the current position has already been visited
    if marked[x][y] == 1:
        return

    # check if the current position equals the desirable value
    if matrix[x][y] != dot:
        position = matrix[x][y]
        # if it´s a key or door
        if position.isalpha():
            # if it´s a key
            if position.islower():
                door_keys.add(position)
                # if the player found the door before getting the key
                if position.upper() in doors.keys():
                    marked[x][y] = 1
                    for t in doors.get(position.upper()):
                        flood_fill(t[0], t[1],
                                   dot, door_keys, doors)
            # if it´s a door never visited
            elif position.lower() not in door_keys:
                if position not in doors:
                    doors[position] = []
                if ((x, y)) not in doors.get(position):
                    doors[position].append((x, y))
                return
        elif position.isnumeric():
            pass
        else:
            return

    # set the current position to visited and increment the number of positions visited
    marked[x][y] = 1
    pos_visited += 1

    # attempt to fill the neighboring positions
    flood_fill(x-1, y, dot, door_keys, doors)
    flood_fill(x+1, y, dot, door_keys, doors)
    flood_fill(x, y-1, dot, door_keys, doors)
    flood_fill(x, y+1, dot, door_keys, doors)

    return pos_visited


if __name__ == "__main__":
    results = {}
    for file in os.listdir('casos-cohen'):
        if file not in results:
            results[file] = []
        matrix = read_file(file)
        players = find_players(matrix)
        for p, c in players.items():
            pos_visited = 0
            door_keys = set()
            doors = {}
            # array of positions marked with 1 if visited
            marked = [[0 for _ in range(len(matrix[0]))]
                      for _ in range(len(matrix))]
            positions_visited = flood_fill(c[0], c[1], ".", door_keys, doors)
            results[file].append((p, positions_visited))
            print()
            print(
                f'caso de teste: {file} \t player: {p} \t casinhas exploradas: {positions_visited}')
