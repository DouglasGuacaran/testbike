
import requests
from core.models import Estacion
from dateutil import parser
import json
from bs4 import BeautifulSoup

def getConnection(url):
    response = requests.get(url)
    data = response.json()

    # Procesar los datos y actualizar los registros en la base de datos
    estaciones = data['network']['stations']
    for estacion in estaciones:
        # Comprobar si la estación ya existe en la base de datos
        try:
            obj = Estacion.objects.get(id=estacion['id'])
        except Estacion.DoesNotExist:
            obj = Estacion(id=estacion['id'])

        # Actualizar los campos de la estación
        obj.nombre = estacion['name']
        obj.latitud = estacion['latitude']
        obj.longitud = estacion['longitude']
        obj.bicicletas_disponibles = estacion['free_bikes']
        obj.espacios_disponibles = estacion['empty_slots']
        obj.ultima_actualizacion = parser.parse(estacion['timestamp'])

        # Guardar la estación en la base de datos
        obj.save()
    estaciones=Estacion.objects.all()
    # Redirigir a una página de confirmación de actualización
    return

def obtenerData():
    # Scrappin datos de la pagina
    
    soup = BeautifulSoup(requests.get('https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php').text, "html.parser")
    index = soup.select_one('select')
    
    table = soup.find('table')
    scrap = enumerate(table.find_all('tr'))

    header = []
    project_list = []

    for i, row in scrap:
        if i == 0:
            # obtencion del header
            header = [el.text.strip() for el in row.find_all('th')]
        else:
            # 
            extracted_row = [el.text.strip() for el in row.find_all('td')]
            # asegurando que la fila tenga la misma longitud que el encabezado de la tabla
            if len(header) == len(extracted_row):
                # construyendo el dict
                dict_row = {}
                for j, header_key in enumerate(header):
                    dict_row.update({header_key: extracted_row[j]})
                project_list.append(dict_row)

    return (project_list)
# imprimir archivo
with open("data.json", "w", encoding='utf8') as final:
    json.dump(obtenerData(), final, ensure_ascii=False)
    