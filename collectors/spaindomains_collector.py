import csv
import requests


def get_domains_from_file(file_url):
    
    # utilizamos el fichero donde se encuentran los dominios
    domains_file = requests.get(file_url)

    # formateo el fichero linea a linea para extraer los dominios
    # utilizo el delimitador ";" para dividir los diferentes campos
    text = domains_file.text.splitlines()
    reader = csv.reader(text[4:], delimiter=";")

    domains_list = []
    for row in reader:
        domains_list.append(row[1])
        
    return domains_list

if __name__ == "__main__":
    # Comprobar que correctamente me está leyendo bien el correspondiente fichero de dominios
    # print(get_spanish_domains("https://www.dominios.es/sites/dominios/files/2024-01/Alt_es_202312.xls.csv")[0])
    print(get_domains_from_file("https://www.dominios.es/sites/dominios/files/2024-02/Alt_es_202401.xls.csv"))
