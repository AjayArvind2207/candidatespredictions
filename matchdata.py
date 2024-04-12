#For future: scrape data from chessresults

from results_scraper import update_state
from finished_matches_scraper import get_completed_matches



def get_results_now():
    results = update_state()
    return results

def get_finished_matches(round, participants):
    return get_completed_matches(round, participants)
   

def get_active_matches(matches_finished):
    matches = []

    players = ["Caruana, Fabiano", "Gukesh, D", "Abasov, Nijat", "Vidit, Santosh Gujrathi", "Nepomniachtchi, Ian", "Nakamura, Hikaru", "Firouzja, Alireza", "Praggnanandhaa, R"]
    for i in players:
        for k in players:
            if i != k:
                if [i,k] in matches_finished:
                    pass
                else:
                    matches.append([i,k])   


    return matches

