import requests
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
print(header)
 
for row in rows:
    print(row)

