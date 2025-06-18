import requests
from pathlib import Path
import json

Base_Url = "https://data.usajobs.gov"
query_params = {
    "PositionSeries": "1550",
    "StartPositionCloseDate": "2021-01-01",
    "EndPositionCloseDate": "2021-12-31",
    #"PageSize": 1,
}

response = requests.get(Base_Url + "/api/historicjoa", params=query_params)
ayo = response.json()

jsonpath = Path('GS.json')
with open(jsonpath, 'w', encoding='utf-8') as f:
    json.dump(ayo, f, ensure_ascii=False, indent=4)

#print(ayo['data'])
for job in ayo['data']:
    control = job['usajobsControlNumber']
    gs = job['minimumGrade']
    print(str(gs) + " " + str(control))


