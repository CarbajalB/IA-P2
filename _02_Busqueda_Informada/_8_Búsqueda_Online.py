import requests
from bs4 import BeautifulSoup

def buscar_en_google(query):
    # Construimos la URL de Google para realizar la búsqueda.
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        resultados = soup.find_all('h3', class_='t')
        for resultado in resultados:
            titulo = resultado.get_text()
            enlace = resultado.find('a')['href']
            print(f"Resultado: {titulo}")
            print(f"Enlace: {enlace}\n")
    else:
        print("No se pudo conectar a Google.")
if __name__ == "__main__":
    busqueda = input("Introduce tu busqueda: ")
    buscar_en_google(busqueda)