import requests
from bs4 import BeautifulSoup
url = "https://chess-results.com/tnr918851.aspx?lan=1&art=2&flag=30"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
FIXED_SKIP_LENGTH = 9

def get_completed_matches(rounds, no_participant):

    participants = soup.find_all('a', attrs = {'class': "CRdb"})
    cnt = 0
    total_list = []
    small_list = []
    for row in participants:
        if cnt > FIXED_SKIP_LENGTH + rounds * no_participant:
            break

        if cnt < FIXED_SKIP_LENGTH:
            cnt+=1
            continue
        small_list.append(row.text)
        if len(small_list) == 2:
            total_list.append(small_list)
            small_list = []
        cnt+=1
        
        
    return total_list

