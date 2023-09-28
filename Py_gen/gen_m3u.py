from bs4 import BeautifulSoup
import requests
import os

def scrape_links(url):
    # Realizar la solicitud HTTP
    response = requests.get(url)

    # Crear el objeto BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos los elementos 'a' en la página (que corresponden a los enlaces)
    links = soup.find_all('a')

    # Extraer el atributo 'href' y el texto de cada enlace
    urls = [(link.text, link.get('href')) for link in links if link.get('href').startswith('acestream://')]

    return urls

def create_m3u_file(links, filename="lista_ace.m3u"):
    with open(filename, "w") as f:
        f.write("#EXTM3U\n")
        for name, url in links:
            f.write(f"#EXTINF:-1,{name}\n")
            f.write(f"{url}\n")

    print(f"El archivo {filename} se ha guardado en {os.getcwd()}")

# Prueba la función con cualquier URL
url = "https://futbolsinpagar.pages.dev/"
links = scrape_links(url)

# Imprime en pantalla todos los enlaces y sus nombres
#for name, link in links:
 #   print(f" {name}, {link}")

# Crea el archivo M3U
create_m3u_file(links)
