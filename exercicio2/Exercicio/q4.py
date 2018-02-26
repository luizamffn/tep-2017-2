from bs4 import BeautifulSoup
from Exercicio.testeRequests import download
import time

url_inicial = "http://example.webscraping.com/"
url = "http://example.webscraping.com/"
link_pais = []
proximo = ""
list_paises = []

def download_pagina():
    global url
    html = download(url)
    # print(html)
    soup = BeautifulSoup(html, 'html5lib')
    tabela = soup.find('table')

    global proximo
    proximo = (soup.find(attrs={'id':'pagination'})).find_all('a', href=True)
    for p in proximo:
        if(p.text == "Next >"):
            url = url_inicial + p['href']
            # print("url " + url)

    for a in tabela.find_all('a', href=True):
        # print(a['href'])
        link_pais.append(url_inicial+a['href'])


def paises():
    for i in range(0,2):
        time.sleep(1)
        download_pagina()

    count = 1
    for link in link_pais:
        print(count)
        time.sleep(1)
        html = download(link)
        # print(html)
        soup = BeautifulSoup(html, 'html5lib')
        pais = (soup.find(attrs={'id': 'places_country__row'})).find(attrs={'class': 'w2p_fw'})
        area = (soup.find(attrs={'id':'places_area__row'})).find(attrs={'class':'w2p_fw'})
        populacao = (soup.find(attrs={'id':'places_population__row'})).find(attrs={'class':'w2p_fw'})
        area = area.text.replace(" square kilometres", "")
        area = float(area.replace(",", ""))
        populacao = float(populacao.text.replace(",", ''))

        densidade_demografica = 0
        if(area != 0):
            densidade_demografica = populacao/area

        print("pais "+ pais.text + "area " + str(area) + 'populacao ' + str(populacao) + 'densidade ' + str(densidade_demografica))
        list_paises.append({"pais": pais.text, "area": str(area), 'populacao': str(populacao), 'densidade': str(densidade_demografica)})

        count +=1
    return list_paises