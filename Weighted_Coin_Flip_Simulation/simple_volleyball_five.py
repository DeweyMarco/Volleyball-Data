import numpy as np
import sys

trials = 10000
season_length = 26
threshold = 12
point_percentage = 0.5455915599095704
sets_played = [0,0,0,0,0,0]
set_number = 0
team_score = 0
opponent_score = 0


def point():
    turn = np.random.uniform(0,1)
    if turn < point_percentage:
        return True
    else:
        return False


def set(set_num):
    global set_number, team_score, opponent_score
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
    if set_num != 5:
        set_number += 1
        team_score += team
        opponent_score += opponent
    if team > opponent:
        return (True, (team, opponent))
    else:
        return (False, (team, opponent))
    
    

def game(game_num):
    wins = 0
    loss = 0
    set_num = []
    for i in range(0,5):
        if wins == 3 or loss == 3:
            break
        sets = set(i+1)
        set_num.append(sets[1])
        if sets[0]:
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
        return (True, (wins,loss), set_num)
    else: 
        return (False, (wins,loss), set_num)

def season():
    wins = 0
    loss = 0
    sets_won = 0
    sets_lost = 0
    for i in range(0,season_length):
        match = game(i)
        sets_won += match[1][0]
        sets_lost += match[1][1]
        if match[0]:
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
    print("number of seasons : " + str(trials))
    print("winning threshold : " + str(point_percentage))
    print("average wins : " + str(wins / trials))
    print("average loss : " + str(loss / trials))
    print("win percentage : " + str(wins / (wins+ loss)))
    print("winning seasons : " + str(seasons))
    print("post-season appearance : " + str(post))
    print("best season : " + str(best_season[0]) + " - " + str(best_season[1]))
    print("worst season : " + str(worst_season[0]) + " - " + str(worst_season[1]))
    print("projected points per game : " + str(team_score / set_number))
    print("projected opponent points per game : " + str(opponent_score / set_number))
    print("projected set record : " + str(sets_won / trials) + "-" + str(sets_lost / trials))
    print("projected set percentage : " + str(sets_won / (sets_lost + sets_won)))
    print("projected 3 - 0 games : " + str(sets_played[0] / trials))
    print("projected 3 - 1 games : " + str(sets_played[1] / trials))
    print("projected 3 - 2 games : " + str(sets_played[2] / trials))
    print("projected 2 - 3 games : " + str(sets_played[3] / trials))
    print("projected 1 - 3 games : " + str(sets_played[4] / trials))
    print("projected 0 - 3 games : " + str(sets_played[5] / trials))
    
def read_input():
    global trials, season_length, threshold, point_percentage
    if len(sys.argv) != 5:
        print("ERROR : Invalid Input")
        print()
        print("python3 simple_volleyball_five.py [number of trials] [season length] [post season threshold] [win percentage]")
        print()
        print("Example : $ python3 simple_volleyball_five.py 1000 20 12 0.52")
        exit()
    trials = int(sys.argv[1])
    season_length = int(sys.argv[2])
    threshold = int(sys.argv[3])
    point_percentage = float(sys.argv[4])

if __name__ == "__main__":
    read_input()
    experiment()