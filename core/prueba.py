import requests
import json
from bs4 import BeautifulSoup

    
soup = BeautifulSoup(requests.get("https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php").text, "html.parser")
table = soup.find('table')
data_json = {}
header = []
rows = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

data_json = { 'header': header, 'rows': rows}
with open("data.json", "w") as f:
    json.dump(data_json, f)
with open('data.json') as f:
    data = json.load(f)
print(data)
# for row in rows:
    # print(row)

