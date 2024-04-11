
from random import choice
from math_methods import compute_odds_and_assign_result, run_simulations
import matplotlib.pyplot as plt
from matchdata import get_finished_matches, get_active_matches, get_results_now
from inputdata import get_elo_dictionary

matches_finished = get_finished_matches()

matches = get_active_matches(matches_finished)

results_now = get_results_now()

d = get_elo_dictionary()


def graph(percentages):
    labels = percentages.keys()
    sizes = percentages.values()

    colors = ['green', 'yellow', 'magenta', 'red', 'purple', 'lightskyblue', "lightgreen", 'orange' ]
    assert(len(colors) == 8)

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.axis('equal')  
    plt.title('Odds to win candidates after round 4', y = 1.1)

    plt.legend(loc='center left', bbox_to_anchor=(0.9, 0.5))

    plt.show()

def main(num_of_iterations = 100000):

    overall_results = {}
    

    for i in d:
        overall_results[i] = 0

    
    for i in range(num_of_iterations):

        one_iteration = run_simulations(d, matches, results_now.copy())
        winners_per_iteration = []
        for k,v in one_iteration.items():
            if v == max(one_iteration.values()):
                winners_per_iteration.append(k)
       
        overall_results[choice(winners_per_iteration)] +=1  #Tiebreak randomly

    overall_results = {k: v for k, v in sorted(overall_results.items(), key=lambda item: item[1], reverse=True)}
    total = sum(overall_results.values())
    percentages = {k: round(100 * v / total, 2) for k, v in overall_results.items()}
        
    
    print(total)
    print(overall_results)
    print(percentages)

    graph(percentages)
   

main(300000)