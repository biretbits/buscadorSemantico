import requests
from bs4 import BeautifulSoup as b
from urllib.parse import urljoin, parse_qs, urlparse
def obtener_resultados_busqueda(consulta):
    response = requests.get(f'https://www.google.com/search?q={consulta}')
    results = []
    soup = b(response.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('/url?q='):
            real_url = parse_qs(urlparse(href).query).get('q')
            if real_url:
                url = real_url[0]
                # Obtener título y descripción
                title = a.get_text() or "No se encontro titulo"
                description = a.find_next('span', class_='aCOpRe').get_text() if a.find_next('span', class_='aCOpRe') else "No se encontro una descripcion"
                results.append({'url':url,'titulo':title})
    
    return results[:5]

def mostrar_resultados(resultados):
    for i, resultado in enumerate(resultados):
        print(f"Resultado {i + 1}:")
        print(f"Título: {resultado['titulo']}")
        print(f"Enlace: {resultado['enlace']}")
        print(f"Descripción: {resultado['descripcion']}\n")

def main():
    consulta = input("Ingrese su consulta de búsqueda: ")
    resultados = obtener_resultados_busqueda(consulta)
    vector = []
    if resultados:
        for re in resultados:
            url,titulo,descripcion = (get_title_and_description(re))
            vector.append({'url':url,'decripcion':descripcion,'titulo':titulo})
    else:
        print("No se encontraron resultados o hubo un error en la solicitud.")

def get_title_and_description(url):
    try:
        print(url)
        url1 = url['url']
        titulo = url['titulo']
        print(url1)
        response = requests.get(url1, timeout=10)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        soup = b(response.text, 'html.parser')
        #texto = soup.get_text() if soup.get_text() else 'No se encontró título'
        # Obtener la descripción
        description = ''
        if soup.find('meta', attrs={'name': 'description'}):
            description = soup.find('meta', attrs={'name': 'description'}).get('content', '')
        elif soup.find('meta', attrs={'property': 'og:description'}):
            description = soup.find('meta', attrs={'property': 'og:description'}).get('content', '')
        else:
            # Intentar obtener la descripción desde los primeros párrafos o encabezados
            paragraphs = soup.find_all('p')
            headers = soup.find_all(['h1', 'h2', 'h3'])
            
            # Combinar textos de párrafos y encabezados en una lista de candidatos
            candidates = [p.get_text() for p in paragraphs] + [h.get_text() for h in headers]
            if candidates:
                # Tomar el primer candidato no vacío
                description = next((text for text in candidates if text.strip()), 'No se encontró descripción')
        #print("titulosssssssssssssssssssssssssssssssssssssss")
        #print('titulo: ',titulo," descripcion ", description)
        return url,titulo,descripcion
    except Exception as e:
        return 'Error', str(e)
if __name__ == '__main__':
    main()
