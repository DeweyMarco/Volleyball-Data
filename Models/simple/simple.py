import numpy as np
import sys

point_percentage = 0.5

def set_point_percentage(pp):
    global point_percentage
    point_percentage = pp
    
def set_serve(s):
    return

def point():
    turn = np.random.uniform(0,1)
    if turn < point_percentage:
        return True
    else:
        return False

def set(set_num):
    team = 0
    opponent = 0
    cap = 25
    if set_num == 5:
        cap = 15
    while team < cap and opponent < cap:
        if point():
            team += 1
        else:
            opponent += 1
    while abs(team - opponent) <= 1:
        if point():
            team += 1
        else:
            opponent += 1
    return (team, opponent)

def experiment():
    x = set(1)
    print("my score : " + str(x[0]))
    print("opponent score : " + str(x[1]))
    
def read_input():
    global point_percentage
    if len(sys.argv) != 2:
        print("ERROR : Invalid Input")
        print()
        print("python3 simple.py [win percentage]")
        print()
        print("Example : $ python3 simple.py 0.52")
        exit()
    point_percentage = float(sys.argv[1])

if __name__ == "__main__":
    read_input()
    experiment()