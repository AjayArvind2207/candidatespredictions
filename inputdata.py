import json
elo_ratings = {
    "Caruana, Fabiano": 2803,
    "Nakamura, Hikaru": 2789,
    "Abasov, Nijat": 2632,
    "Nepomniachtchi, Ian": 2758,
    "Firouzja, Alireza": 2760,
    "Praggnanandhaa, R": 2747,
    "Gukesh, D": 2743,
    "Vidit, Santosh Gujrathi": 2727
}

def make_elo_dictionary():
    with open("players.json", 'w') as f:
        json.dump(elo_ratings, f)
        print("Sucess!")


def get_elo_dictionary():
    with open("players.json") as f:
        dicto = json.load(f)
        return dicto
    

if __name__ == '__main__':
    make_elo_dictionary()