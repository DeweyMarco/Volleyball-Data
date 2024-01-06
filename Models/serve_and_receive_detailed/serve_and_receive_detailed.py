import numpy as np
import sys

serve_percentages = [0.09, 0.16, 0.5, 0.16, 0.09]
receive_percentages = [0.09, 0.16, 0.5, 0.16, 0.09]
serve_win_percentages = [0, 0.33, 0.5, 0.66, 1]
receive_win_percentages = [0, 0.33, 0.5, 0.66, 1]
serve = True

def set_serve_zero(sz):
    serve_percentages[0] = sz
    
def set_serve_one(so):
    serve_percentages[1] = so
    
def set_serve_two(st):
    serve_percentages[2] = st
    
def set_serve_three(sr):
    serve_percentages[3] = sr
    
def set_serve_four(sf):
    serve_percentages[4] = sf
    
def set_serve_win_one(so):
    serve_win_percentages[1] = so
    
def set_serve_win_two(st):
    serve_win_percentages[2] = st
    
def set_serve_win_three(sr):
    serve_win_percentages[3] = sr
    
def set_receive_zero(rz):
    receive_percentages[0] = rz
    
def set_receive_one(ro):
    receive_percentages[1] = ro
    
def set_receive_two(rt):
    receive_percentages[2] = rt
    
def set_receive_three(rr):
    receive_percentages[3] = rr
    
def set_receive_four(rf):
    receive_percentages[4] = rf
    
def set_receive_win_one(ro):
    receive_win_percentages[1] = ro
    
def set_receive_win_two(rt):
    receive_win_percentages[2] = rt
    
def set_receive_win_three(rr):
    receive_win_percentages[3] = rr

def set_serve(s):
    global serve
    serve = s
        
def num_point(num):
    global serve
    turn = np.random.uniform(0,1)
    if serve:
        if turn < serve_win_percentages[num]:
            return True
        else:
            serve = False
            return False
    else:
        if turn < receive_win_percentages[num]:
            serve = True
            return True
        else:
            return False
        
def point():
    global serve
    turn = np.random.uniform(0,1)
    if serve:
        if turn < serve_percentages[0]:
            serve = False
            return False
        if turn < serve_percentages[0] + serve_percentages[1]:
            return num_point(1)
        if turn < serve_percentages[0] + serve_percentages[1] + serve_percentages[2]:
            return num_point(2)
        if turn < serve_percentages[0] + serve_percentages[1] + serve_percentages[2] + serve_percentages[3]:
            return num_point(3)
        else:
            return True
    else:
        if turn < receive_percentages[0]:
            return False
        if turn < receive_percentages[0] + receive_percentages[1]:
            return num_point(1)
        if turn < receive_percentages[0] + receive_percentages[1] + receive_percentages[2]:
            return num_point(2)
        if turn < receive_percentages[0] + receive_percentages[1] + receive_percentages[2] + receive_percentages[3]:
            return num_point(3)
        else:
            serve = True
            return True


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

if __name__ == "__main__":
    experiment()