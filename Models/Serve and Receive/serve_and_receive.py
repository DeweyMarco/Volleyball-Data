import numpy as np
import sys

serve_percentage = 0.5
receive_percentage = 0.5
serve = True

def set_serve_percentage(sp):
    global serve_percentage
    serve_percentage = sp
    
def set_receive_percentage(rp):
    global receive_percentage
    receive_percentage = rp

def set_serve(s):
    global serve
    serve = s

        
def point():
    global serve
    turn = np.random.uniform(0,1)
    if serve:
        if turn < serve_percentage:
            return True
        else:
            serve = False
            return False
    else:
        if turn < receive_percentage:
            serve = True
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
    set_serve(True)
    x = set(1)
    print("my score : " + str(x[0]))
    print("opponent score : " + str(x[1]))
    
def read_input():
    global serve_percentage, receive_percentage
    if len(sys.argv) != 3:
        print("ERROR : Invalid Input")
        print()
        print("python3 serve_and_receive.py [serve percentage] [receive percentage]")
        print()
        print("Example : $ python3 serve_and_receive.py 0.49 0.52")
        exit()
    serve_percentage = float(sys.argv[1])
    receive_percentage = float(sys.argv[2])

if __name__ == "__main__":
    read_input()
    experiment()