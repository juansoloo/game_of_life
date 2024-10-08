import numpy as np
import random as random
import time 

DEAD = 0
LIVE = 1

def dead_state(height, width):
    arr = []
    for i in range(height * width):
        arr.append(0)

    board_state = np.array(arr).reshape(height,width)
    return board_state


def random_state(height,width):
    state = dead_state(height,width)

    for i in range(height):
        for j in range(width):
            rand_num = random.random()
            if rand_num >= 0.5:
                state[i][j] = DEAD
            else:
                state[i][j] = LIVE
    return state

def state_height(state):
    return len(state)

def state_width(state):
    return len(state[0])

def render(state): 
    display = {
        DEAD: ' ',
        LIVE: '#' 
    }
    lines = [] 
    for i in range(state_height(state)):
        line = ''
        for j in range(state_width(state)):
            line += display[state[i][j]] * 2
        lines.append(line)
    print("\n".join(lines))

def get_cell(coordinate, state):
    height = state_height(state)
    width = state_width(state)
    x = coordinate[0]
    y = coordinate[1]
    live_cell = 0 

    for x_cell in range((x-1), (x+1)+1):
        if x_cell < 0 or x_cell >= height: continue 

        for y_cell in range((y-1),(y+1)+1):
            if y_cell < 0 or y_cell >= width: continue

            if x_cell == x and y_cell == y: continue 

            if state[x_cell][y_cell] == LIVE:
                live_cell += 1

    if state[x][y] == LIVE:
        if live_cell <= 1:
            return DEAD
        elif live_cell <= 3:
            return LIVE
        else:
            return DEAD
    else:
        if live_cell == 3:
            return LIVE
        else:
            return DEAD

def next_board_state(inital_state):
    height = state_height(inital_state)
    width = state_width(inital_state)
    next_state = dead_state(height, width)

    for i in range(height):
        for j in range(width):
            next_state[i][j] = get_cell((i,j), inital_state)

    return next_state    

def run(inital_state):
    next_state = inital_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.03)

if __name__ == "__main__":
    inital_state = random_state(20,20)
    run(inital_state)
