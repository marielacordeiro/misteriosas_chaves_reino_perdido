
import sys, os
from enum import Enum

class GameMapAssets(Enum):
    DOT = "."
    WALL = "#"

def read_file(test_case: str):
    matrix = []
    with open(f'casos-cohen/{test_case}') as f:
        for line in f:
            matrix.append(list(line.strip()))
    return matrix

def print_field(list):
    #  function that traverses the array and prints any list wanted
    for y in range(len(list)):
        for x in range(len(list[0])):
            print(list[y][x], end=' ')
            if x == len(list[0])-1:
                print('\n')

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

def flood_fill(x, y, game_map, door_keys):

    if game_map[x][y] == GameMapAssets.WALL.value:
        return

    if marked_matrix[x][y] == 1:
        return

    global points 

    current_position = game_map[x][y]

    if current_position.isalpha():
        if current_position.islower():
            door_keys.add(current_position)
        elif current_position.lower() not in door_keys:
            return

    # thirdly, set the current position to the new value
    marked_matrix[x][y] = 1
    points += 1

    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y  , game_map, door_keys)
    flood_fill(x-1, y  , game_map, door_keys)
    flood_fill(x  , y-1, game_map, door_keys)
    flood_fill(x  , y+1, game_map, door_keys)

    return points

if __name__ == "__main__":
    sys.setrecursionlimit(15000)
    points = 0 
    game_map = read_file('./caso10.txt')
    players = find_players(game_map)
    var = 9
    x = players[var][0]
    y = players[var][1]

    door_keys = set()
    marked_matrix = [[0 for _ in range(len(game_map[0]))]
                      for _ in range(len(game_map))]

    points = flood_fill(x, y, game_map, door_keys)

    print(points)
