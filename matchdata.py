#For future: 


'''
   


    ["Nakamura, Hikaru", "Nepomniachtchi, Ian"],
    ["Caruana, Fabiano", "Praggnanandhaa, R"],
    ["Abasov, Nijat", "Vidit, Santosh Gujrathi"],
    ["Firouzja, Alireza", "Gukesh, D"],

    ["Nakamura, Hikaru", "Caruana, Fabiano"],
    ["Nepomniachtchi, Ian", "Abasov, Nijat"],
    ["Praggnanandhaa, R", "Firouzja, Alireza"],
    ["Vidit, Santosh Gujrathi", "Gukesh, D"],




    ["Praggnanandhaa, R", "Caruana, Fabiano"],
    ["Nakamura, Hikaru", "Nepomniachtchi, Ian"],
    ["Caruana, Fabiano", "Vidit, Santosh Gujrathi"],
    ["Nepomniachtchi, Ian", "Praggnanandhaa, R"],



    ["Nakamura, Hikaru", "Praggnanandhaa, R"],
    ["Nepomniachtchi, Ian", "Caruana, Fabiano"],
    ["Abasov, Nijat", "Gukesh, D"],
    ["Firouzja, Alireza", "Vidit, Santosh Gujrathi"],
    ["Abasov, Nijat", "Praggnanandhaa, R"],
    ["Caruana, Fabiano", "Vidit, Santosh Gujrathi"],
    ["Nepomniachtchi, Ian", "Nakamura, Hikaru"],
    ["Firouzja, Alireza", "Gukesh, D"],
    ["Nakamura, Hikaru", "Firouzja, Alireza"],
    ["Abasov, Nijat", "Gukesh, D"],
    ["Caruana, Fabiano", "Nepomniachtchi, Ian"]
]'''

def get_results_now():
    
    results_now = {'Caruana, Fabiano': 3.5, 'Nakamura, Hikaru': 3, 'Abasov, Nijat': 1.5, 'Nepomniachtchi, Ian': 4, 'Firouzja, Alireza': 1.5, 'Praggnanandhaa, R': 3.5, 'Gukesh, D': 4, 'Vidit, Santosh Gujrathi': 3}
    return results_now


def get_finished_matches():
    matches_finished = [
    ["Caruana, Fabiano", "Nakamura, Hikaru"],
    ["Abasov, Nijat", "Nepomniachtchi, Ian"],
    ["Firouzja, Alireza", "Praggnanandhaa, R"],
    ["Gukesh, D", "Vidit, Santosh Gujrathi"],
    
    ["Praggnanandhaa, R", "Gukesh, D"],
    ["Nakamura, Hikaru", "Vidit, Santosh Gujrathi"],
    ["Nepomniachtchi, Ian", "Firouzja, Alireza"],
    ["Caruana, Fabiano", "Abasov, Nijat"],

    ["Gukesh, D", "Nepomniachtchi, Ian"],
    ["Abasov, Nijat", "Nakamura, Hikaru"],
    ["Firouzja, Alireza", "Caruana, Fabiano"],
    ["Vidit, Santosh Gujrathi", "Praggnanandhaa, R"],

    ["Nakamura, Hikaru", "Praggnanandhaa, R"],
    ["Nepomniachtchi, Ian", "Vidit, Santosh Gujrathi"],
    ["Caruana, Fabiano", "Gukesh, D"],
    ["Abasov, Nijat", "Firouzja, Alireza"],

    ["Praggnanandhaa, R", "Nepomniachtchi, Ian"],
    ["Firouzja, Alireza", "Nakamura, Hikaru"],
    ["Gukesh, D", "Abasov, Nijat"],
    ["Vidit, Santosh Gujrathi", "Caruana, Fabiano"],

    
    ["Gukesh, D", "Nakamura, Hikaru"],
    ["Vidit, Santosh Gujrathi", "Firouzja, Alireza"],
    ["Praggnanandhaa, R", "Abasov, Nijat"],
    ["Nepomniachtchi, Ian", "Caruana, Fabiano"],
    ]
    return matches_finished

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