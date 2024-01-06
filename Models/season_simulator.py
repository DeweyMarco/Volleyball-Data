import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from simple import simple as model1 
from serve_and_receive import serve_and_receive as model2 
from serve_and_receive_detailed import serve_and_receive_detailed as model3

trials = 10000
season_length = 20
threshold = 12
model = model1
sets_played = [0,0,0,0,0,0]
team_score = 0
opponent_score = 0
set_number = 0
serve_total = 1
receive_total = 1

def flip_for_serve():
    turn = np.random.uniform(0,1)
    if turn < 0.5:
        return True
    else:
        return False

def game(game_num):
    global team_score, opponent_score, set_number
    wins = 0
    loss = 0
    serve = flip_for_serve()
    model.set_serve(serve)
    for i in range(0,5):
        if wins == 3 or loss == 3:
            break
        if i == 4:
            serve = flip_for_serve()
            model.set_serve(serve) 
        sets = model.set(i+1)
        serve = not serve
        model.set_serve(serve)
        team_score += sets[0]
        opponent_score += sets[1]
        set_number += 1
        if sets[0] > sets[1]:
            wins += 1
        else:
            loss += 1
    if wins == 3:
        if loss == 0:
            sets_played[0] += 1
        elif loss == 1:
            sets_played[1] += 1
        else:
            sets_played[2] += 1
    else:
        if wins == 0:
            sets_played[5] += 1
        elif wins == 1:
            sets_played[4] += 1
        else:
            sets_played[3] += 1
    if wins > loss:
        return (wins,loss)
    else: 
        return (wins,loss)
    
def season():
    wins = 0
    loss = 0
    sets_won = 0
    sets_lost = 0
    for i in range(0,season_length):
        match = game(i)
        sets_won += match[0]
        sets_lost += match[1]
        if match[0] > match[1]:
            wins += 1
        else:
            loss += 1
    return (wins, loss, sets_won, sets_lost)

def experiment():
    wins = 0
    loss = 0
    seasons = 0
    post = 0
    best_season = (0,season_length)
    worst_season = (season_length,0)
    sets_won = 0
    sets_lost = 0
    for i in range(0, trials):
        x = season()
        wins += x[0]
        loss += x[1]
        sets_won += x[2]
        sets_lost += x[3]
        if (x[0] > season_length / 2):
            seasons += 1
        if (x[0] > threshold):
            post += 1
        if (x[0] > best_season[0]):
            best_season = (x[0],x[1])
        if (x[1] > worst_season[1]):
            worst_season = (x[0],x[1])
    print_boundary()
    print("Number of seasons : " + str(trials))
    print("Point win percentage : " + str(team_score / (team_score + opponent_score)))
    print("Average wins : " + str(wins / trials))
    print("Average loss : " + str(loss / trials))
    print("Win percentage : " + str(wins / (wins+ loss)))
    print("Winning seasons : " + str(seasons))
    print("Post-season appearance : " + str(post))
    print("Best season : " + str(best_season[0]) + " - " + str(best_season[1]))
    print("Worst season : " + str(worst_season[0]) + " - " + str(worst_season[1]))
    print("Projected points per game : " + str(team_score / set_number))
    print("Projected opponent points per game : " + str(opponent_score / set_number))
    print("Projected set record : " + str(sets_won / trials) + "-" + str(sets_lost / trials))
    print("Projected set percentage : " + str(sets_won / (sets_lost + sets_won)))
    print("Projected 3 - 0 games : " + str(sets_played[0] / trials))
    print("Projected 3 - 1 games : " + str(sets_played[1] / trials))
    print("Projected 3 - 2 games : " + str(sets_played[2] / trials))
    print("Projected 2 - 3 games : " + str(sets_played[3] / trials))
    print("Projected 1 - 3 games : " + str(sets_played[4] / trials))
    print("Projected 0 - 3 games : " + str(sets_played[5] / trials))
    
def get_point_percentage():
    print_boundary()
    point_percentage = float(input("Chance to win individual point (as decimal) : "))
    return point_percentage

def get_season_length():
    global season_length
    print_boundary()
    season_length = int(input("Number of games the season : "))
    
def get_post_season():
    global threshold
    print_boundary()
    threshold = int(input("Post season threshold : "))
    
def print_boundary():
    print("************************************************************************************\n")   
    
def get_number_of_trials():
    global trials
    print_boundary()
    trials = int(input("Number of trials : "))
    
def get_model():
    global model
    print_boundary()
    print("Select the Model")
    print()
    print("1 Simple")
    print("2 Serve and Receive")
    print("3 Serve and Receive Detailed")
    print()
    m = int(input("Model number : "))
    if m == 1:
        model = model1
    elif m == 2:
        model = model2
    elif m == 3:
        model = model3
    return m

def get_serve_percentage():
    print_boundary()
    serve_percentage = float(input("Chance to win individual point when serving (as decimal) : "))
    return serve_percentage

def get_receive_percentage():
    print_boundary()
    receive_percentage = float(input("Chance to win individual point when receiving (as decimal) : "))
    return receive_percentage

def get_serve_zero():
    global serve_total
    print_boundary()
    print("Remaining probability : " + str(serve_total))
    serve_percentage = float(input("Chance that your serve is a 0 (as decimal) : "))
    serve_total -= serve_percentage
    return serve_percentage

def get_serve_one():
    global serve_total
    print_boundary()
    print("Remaining probability : " + str(serve_total))
    serve_percentage = float(input("Chance that your serve is a 1 (as decimal) : "))
    serve_total -= serve_percentage
    return serve_percentage

def get_serve_two():
    global serve_total
    print_boundary()
    print("Remaining probability : " + str(serve_total))
    serve_percentage = float(input("Chance that your serve is a 2 (as decimal) : "))
    serve_total -= serve_percentage
    return serve_percentage

def get_serve_three():
    global serve_total
    print_boundary()
    print("Remaining probability : " + str(serve_total))
    serve_percentage = float(input("Chance that your serve is a 3 (as decimal) : "))
    serve_total -= serve_percentage
    return serve_percentage

def get_serve_four():
    global serve_total
    print_boundary()
    print("Remaining probability : " + str(serve_total))
    serve_percentage = float(input("Chance that your serve is a 4 (as decimal) : "))
    serve_total -= serve_percentage
    return serve_percentage

def get_receive_zero():
    global receive_total
    print_boundary()
    print("Remaining probability : " + str(receive_total))
    receive_percentage = float(input("Chance that your receive is a 0 (as decimal) : "))
    receive_total -= receive_percentage
    return receive_percentage

def get_receive_one():
    global receive_total
    print_boundary()
    print("Remaining probability : " + str(receive_total))
    receive_percentage = float(input("Chance that your receive is a 1 (as decimal) : "))
    receive_total -= receive_percentage
    return receive_percentage

def get_receive_two():
    global receive_total
    print_boundary()
    print("Remaining probability : " + str(receive_total))
    receive_percentage = float(input("Chance that your receive is a 2 (as decimal) : "))
    receive_total -= receive_percentage
    return receive_percentage

def get_receive_three():
    global receive_total
    print_boundary()
    print("Remaining probability : " + str(receive_total))
    receive_percentage = float(input("Chance that your receive is a 3 (as decimal) : "))
    receive_total -= receive_percentage
    return receive_percentage

def get_receive_four():
    global receive_total
    print_boundary()
    print("Remaining probability : " + str(receive_total))
    receive_percentage = float(input("Chance that your receive is a 4 (as decimal) : "))
    receive_total -= receive_percentage
    return receive_percentage

def get_serve_win_one():
    print_boundary()
    serve_percentage = float(input("Chance to win individual point when serving a 1 (as decimal) : "))
    return serve_percentage

def get_serve_win_two():
    print_boundary()
    serve_percentage = float(input("Chance to win individual point when serving a 2 (as decimal) : "))
    return serve_percentage

def get_serve_win_three():
    print_boundary()
    serve_percentage = float(input("Chance to win individual point when serving a 3 (as decimal) : "))
    return serve_percentage

def get_receive_win_one():
    print_boundary()
    receive_percentage = float(input("Chance to win individual point when receiving a 1 (as decimal) : "))
    return receive_percentage

def get_receive_win_two():
    print_boundary()
    receive_percentage = float(input("Chance to win individual point when receiving a 2 (as decimal) : "))
    return receive_percentage

def get_receive_win_three():
    print_boundary()
    receive_percentage = float(input("Chance to win individual point when receiving a 3 (as decimal) : "))
    return receive_percentage


if __name__ == "__main__":
    val = get_model()
    get_number_of_trials()
    get_season_length()
    get_post_season()
    if val == 1:
        pp = get_point_percentage()
        model.set_point_percentage(pp)
        experiment()
    if val == 2:
        sp = get_serve_percentage()
        rp = get_receive_percentage()
        model.set_serve_percentage(sp)
        model.set_receive_percentage(rp)
        experiment()
    if val == 3:
        sz = get_serve_zero()
        so = get_serve_one()
        swo = get_serve_win_one()
        st = get_serve_two()
        swt = get_serve_win_two()
        sr = get_serve_three()
        swr = get_serve_win_three()
        sf = get_serve_four()
        model.set_serve_zero(sz)
        model.set_serve_one(so)
        model.set_serve_win_one(swo)
        model.set_serve_two(st)
        model.set_serve_win_two(swt)
        model.set_serve_three(sr)
        model.set_serve_win_three(swr)
        model.set_serve_four(sf)
        rz = get_receive_zero()
        ro = get_receive_one()
        rwo = get_receive_win_one()
        rt = get_receive_two()
        rwt = get_receive_win_two()
        rr = get_receive_three()
        rwr = get_receive_win_three()
        rf = get_receive_four()
        model.set_receive_zero(rz)
        model.set_receive_one(ro)
        model.set_receive_win_one(rwo)
        model.set_receive_two(rt)
        model.set_receive_win_two(rwt)
        model.set_receive_three(rr)
        model.set_receive_win_three(rwr)
        model.set_receive_four(rf)
        experiment()
        
        
    