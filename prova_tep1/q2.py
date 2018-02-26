from bs4 import BeautifulSoup
from utilitario import download

url = "http://www.portaldatransparencia.gov.br"
estado = input("Digite a sigla do estado: ")
empresas = []

def estados(link):
    page = download(link)
    soup = BeautifulSoup(page, 'html5lib')
    tabela = soup.find_all('tbody')
    paginacao = soup.find(attrs={"class":"paginacao-simples"})

    for campo in tabela[1].find_all('tr'):
        colunas = campo.find_all('td')
        if(colunas != []):
            if(colunas[5].text == estado.upper()):
                if(not empresas.__contains__(colunas[1].text)):
                    print(colunas[1].text)
                    empresas.append(colunas[1].text)

    for link in paginacao.find_all('a'):
        if (link.text == 'Próxima ›'):
            global url
            estados(url + link['href'])

estados(url+ "/cnep")
