import requests
from bs4 import BeautifulSoup

def obtener_noticias_pjud(url):
    """
    Obtiene los titulares de noticias desde la página del Poder Judicial.

    Args:
        url (str): URL de la sección de noticias del PJUD.

    Returns:
        list: Lista de tuplas con el título y el enlace de cada noticia.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Selector para los títulos de las noticias
        titulares = soup.select("div.itemList h2.itemTitle a")

        # Extraer títulos y enlaces
        noticias = [(t.text.strip(), t['href']) for t in titulares]
        return noticias

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []

# Uso
url_noticias = "https://www.pjud.cl/prensa-y-comunicaciones/noticias-del-poder-judicial"
noticias = obtener_noticias_pjud(url_noticias)

if noticias:
    print("📰 Últimos titulares del Poder Judicial:")
    for titulo, enlace in noticias:
        print(f"- {titulo} → {enlace}")
else:
    print("No se encontraron noticias.")
