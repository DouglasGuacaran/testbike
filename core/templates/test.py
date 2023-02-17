# Hacer una solicitud a la API y obtener los datos
import requests
import json
from bs4 import BeautifulSoup

# Scrap data from page
soup = BeautifulSoup(requests.get("https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php").text, "html.parser")
table = soup.find('table')
scrap = enumerate(table.find_all('tr'))

header = []
project_list = []

for i, row in scrap:
    if i == 0:
        # parse header
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        # parse n row
        extracted_row = [el.text.strip() for el in row.find_all('td')]
        # ensure row has same len than table header
        if len(header) == len(extracted_row):
            # build row dict
            dict_row = {}
            for j, header_key in enumerate(header):
                dict_row.update({header_key: extracted_row[j]})
            project_list.append(dict_row)
            
# write file
with open("data.json", "w", encoding='utf8') as final:
    json.dump(project_list, final, ensure_ascii=False)