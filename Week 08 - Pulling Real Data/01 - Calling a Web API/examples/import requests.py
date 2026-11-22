import requests
response = requests.get("http://api.github.com/orgs/python")
print(response.status_code)

#2
import json
text = text = '{"name": "Rex", "age": 4, "vaccinated": true, "owner": null, "tags": ["dog", "friendly"]}'
print(type(text))
pet = json.loads(text)
print(type(pet))
print(pet["name"], pet["vaccinated"], pet["owner"], pet["tags"][0])
#3
import requests
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
response = requests.get(url, timeout=10)
print(response.status_code)
print(response.text[:100])
#4
import pandas as pd
from io import StringIO
df = pd.read_csv(StringIO(response.text))
print(df.head())
print(len(df), "rows")
#5
import pandas as pd
records = [
    {"id": "a1", "properties": {"mag": 4.5, "place": "Chile", "time": 1700000000000}},
        {"id": "a2", "properties": {"mag": None, "place": "Japan", "time": 1700003600000}},
        {"id": "a3", "properties": {"mag": 5.1, "place": "Peru", "time": 1700007200000}},
]
df = pd.json_normalize(records)
print(df.columns.tolist())
print(df)
#6
quakes = pd.DataFrame({"place": ["chile", "japan"], "coordinates": [[-70.1, -33.4, 12.0], [139.7, 35.7, 30.5]]})
quakes["depth_km"] = quakes["coordinates"].apply(lambda coords: coords[2])
print(quakes)
#8
import re
log = "attempts from 10.0.0.5 and 192.168.1.1 and 10.0.0.9"
all_ips = re.findall(r"\d+\.\d+\.\d+\.\d+", log)
print(all_ips)