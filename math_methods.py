from math import sqrt, exp, e, pi
import random


def arclogit(x):
    return exp(x) / (1 + exp(x))

def compute_draw_probability(rwhite, rblack):
    probability = arclogit(-1.627 + 0.0006955 * rwhite - 0.004668 * abs(rwhite - rblack))
    return probability

def assign_result(win_probability_a, draw_probability):
    num = random.random()
    if num <= win_probability_a:
        res = "White win"
    elif win_probability_a < num <= win_probability_a + draw_probability:
        res = "Draw"
    else:
        res = "Black win"
    return res

def compute_odds_and_assign_result(rwhite, rblack):

    dr = rwhite - rblack
    expected_a = 1 / (1 + 10 ** ((-dr - 40)/400))
    expected_b = 1 - expected_a

    draw_probability = (compute_draw_probability(rwhite, rblack))
    win_probability_a = expected_a - draw_probability/2
    win_probability_b = expected_b - draw_probability/2
    return (assign_result(win_probability_a, draw_probability))


def run_simulations(d, matches, results):


    for i in matches:
        elo1 = d[i[0]]
        elo2 = d[i[1]]
        result = compute_odds_and_assign_result(elo1, elo2)

        if result == "White win":
            results[i[0]] +=1

        elif result == "Draw":
            results[i[0]] += 1/2
            results[i[1]] += 1/2
        else:
            results[i[1]] += 1

    return results

