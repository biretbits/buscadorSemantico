import requests
from bs4 import BeautifulSoup as b

def search_google(query):
    response = requests.get(f'https://www.google.com/search?q={query}')
    html = response.content
    soup = b(html, 'lxml')
    print(soup)
    results = []
    for item in soup.select('.tF2Cxc'):
        link_element = item.select_one('a')
        if link_element:
            link = link_element['href']
            results.append(link)
    
    return results
    
if __name__ == "__main__":
    user_query = input("Introduce el texto para buscar: ")
    search_results = search_google(user_query)
    if search_results:
        for link in search_results:
            print(f"Link: {link}")
    else:
        print("No se encontraron resultados.")

