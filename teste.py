import sys, os
from enum import Enum

from pytest import mark


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



def pre_flood_fill(x, y):
    door_keys = set()
    return flood_fill(x, y, door_keys, game_map)


def flood_fill(x, y, door_keys, game_map):

    if game_map[x][y] == GameMapAssets.WALL.value:
        return

    if x < 0 or x >= len(game_map[0]) or y < 0 or y >= len(game_map):
        return

    if marked_matrix[x][y] == 1:
        return

    global points
     
    current_position = game_map[x][y]

    if game_map[x][y].isalpha():
            if game_map[x][y].islower():
                door_keys.add(game_map[x][y])
            else:
                game_map[x][y].lower() not in door_keys
                return


    # thirdly, set the current position to the new value
    marked_matrix[x][y] = 1
    points += 1

    # fourthly, attempt to fill the neighboring positions
    flood_fill(x-1, y  , door_keys, game_map)
    flood_fill(x+1, y  , door_keys, game_map)
    flood_fill(x  , y-1, door_keys, game_map)
    flood_fill(x  , y+1, door_keys, game_map)

    return points


if __name__ == "__main__":

    sys.setrecursionlimit(5000)
    points = 0 
    game_map = read_file('./caso04.txt')
    
    print(GameMapAssets.DOT.value)
    marked_matrix = [[0 for _ in range(len(game_map[0]))]
                      for _ in range(len(game_map))]
    # cases 15, 16
    points = pre_flood_fill(4, 6)
    print_field(marked_matrix)
    print(points)


'''
if game_map[x][y].isalpha():
            if game_map[x][y].islower():
                door_keys.add(game_map[x][y])
            else:
                game_map[x][y].lower() not in door_keys
                return
        elif current_position.isnumeric():
            print('hi')
            pass
        else:
            return
            
            '''