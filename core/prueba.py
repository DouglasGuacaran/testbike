import requests
import json
from bs4 import BeautifulSoup

url='https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php'
soup = BeautifulSoup(requests.get(url).text, "html.parser")
select = soup.select_one("select")
select_element = soup.find('select')
last_option = select_element.find_all('option')[-1].text
print(last_option)

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

print (project_list)
# write file
# with open("data.json", "w", encoding='utf8') as final:
#     json.dump(obtenerData("https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"), final, ensure_ascii=False)

