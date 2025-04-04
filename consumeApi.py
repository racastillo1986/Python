import requests
import concurrent.futures
import time

url_1 = "http://localhost:8080/CuadreATM/clienteTrx/verid"
url_2 = "http://localhost:8080/CuadreATM/rpa_comision_diaria_atm/verid"
url_3 = "http://localhost:8080/CuadreATM/rpa_resumen_trx_atm/verid"
url_4 = "http://localhost:8080/CuadreATM/rpa_trx_diaria_atm/verid"
url_5 = "http://localhost:8080/CuadreATM/seedValores/verid"

data = {
    "gd_fecha_desde": "30-01-2025",
    "gd_fecha_hasta": "30-01-2025"
}

data2 = {
    "gv_identificacion": "1307851608",
    "gd_fecha_desde": "09-07-2023",
    "gd_fecha_hasta": "09-07-2023"
}

def consume_url(url, data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"**************************** Respuesta exitosa de {url}: ****************************")
        print(response.json())
    else:
        print(f"Error {response.status_code} al consumir {url}: {response.text}")

def contar():
    for i in range(1, 11):
        print(i)
        time.sleep(0.5)

# secuencial
'''
consume_url(url_1, data)
consume_url(url_2, data)
consume_url(url_3, data)
consume_url(url_4, data)
consume_url(url_5, data2)
'''        

num_requests = 1
# threads
''''''
with concurrent.futures.ThreadPoolExecutor() as executor:
    [executor.submit(consume_url, url_1, data) for _ in range(num_requests)] #clientes
    [executor.submit(consume_url, url_2, data) for _ in range(num_requests)] #comisiones
    [executor.submit(consume_url, url_3, data) for _ in range(num_requests)] #resumen
    [executor.submit(consume_url, url_4, data) for _ in range(num_requests)] #trxDiarias
    [executor.submit(consume_url, url_5, data2) for _ in range(num_requests)] #seed