import pandas as pd
from pathlib import Path
import json
from itertools import islice
from urllib.request import urlopen
import requests


def get_announcement_text(ctl_num):
    return json.load(urlopen('https://data.usajobs.gov/api/historicjoa/announcementtext/' + str(ctl_num)))

def get_announcements(ctl_nums: pd.Series):
    yield from (get_announcement_text(num) for idx, num in df.usajobsControlNumber.items())


def get_announcements_duties():
    response = requests.get('https://data.usajobs.gov/api/historicjoa/announcementtext/' + text_gen[0])
    ayo = response.json()
    print(ayo['majorDutiesList'])

if __name__ == "__main__":
    jsonpath = Path('1550.json')
    df = pd.json_normalize(json.load(jsonpath.open())['data'])
    text_gen = get_announcements(df.usajobsControlNumber)
    #print(pd.DataFrame(islice(text_gen, 10)))
    majorpath = Path('majorduties.txt')
    with open (majorpath, 'w') as f:
        for job in text_gen:
            json.dump(job['majorDutiesList'], f)
            f.write("\n")
            print(job['majorDutiesList'])

