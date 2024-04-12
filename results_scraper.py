import requests
from bs4 import BeautifulSoup
url = "https://chess-results.com/tnr918851.aspx?lan=1&art=1&flag=30"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')


NUM_PLAYERS = 8
NUM_FIELDS = 6

def update_state():
    return get_participants()

def get_participants(scores = {}):
    cnt = 0
    
    participants = soup.find_all('a', attrs = {'class': "CRdb"})
    for row in participants[::-1]:
        if cnt < NUM_PLAYERS:
            scores[row.text] = 0
        else:
            break
        cnt+=1
    return get_points(scores)


    


def get_points(scores, write = False):
    points = soup.find_all('td', attrs = {'class':'CRc'})  
    
    cnt = 0
    active_cnt = 0
    score = dict(reversed(scores.items()))

    for row in points:
        if cnt%NUM_FIELDS == 2:
            scores[list(score.keys())[active_cnt]] = float(row.text.replace(",", "."))
            active_cnt += 1
        cnt+=1
    
    if write:
        write_json(scores)
    
    return scores
    
def write_json(scores):
    import json
    with open("results.json", 'w') as f:
        json.dump(scores, f)
    print("Successfully dumped!")


if __name__ == '__main__':
    update_state()
    