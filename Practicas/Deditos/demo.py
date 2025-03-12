import requests

target = input("Ingresa una URL: ")

r = requests.get(target)

# Imprimir el código de estado HTTP y el contenido de la respuesta
print(f"Código de estado: {r.status_code}")
print(r.text)  # Aquí muestra el contenido de la página web