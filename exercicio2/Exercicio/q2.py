from bs4 import BeautifulSoup
from Exercicio.testeRequests import download
import csv

def salvarCsv(filme, valor_acumulado, valor_faturado, semanas):
    print("teste.py")
    print(filme, valor_acumulado, valor_faturado, semanas)
    inserir = [filme, valor_acumulado, valor_faturado, semanas]
    with open(r'aplicacao/static/filmes.csv', 'a') as data:
        writer = csv.writer(data)
        writer.writerow(inserir)

def filme2():
    list_filmes = []
    url = "http://www.imdb.com/chart/boxoffice"

    html = download(url)
    # print(html)
    soup = BeautifulSoup(html, 'html5lib')
    tabela = soup.find_all('tbody')
    filmes = tabela[0].find_all('tr')

    for f in filmes:
        valor_acumulado = ""
        valor_faturado = ""
        semanas = ""
        filme = f.find(attrs={'class':'titleColumn'}).text.strip()
        print("Filme: " + filme )

        valores = f.find_all(attrs={'class':'ratingColumn'})
        for i in range(0,2):
            if(i ==0):
                print("Valor faturado no fim de semana: " + valores[i].text.strip())
                valor_acumulado = valores[i].text.strip()
            else:
                print("Valor acumulado: " + valores[i].text.strip())
                valor_faturado = valores[i].text.strip()

        print("Semana: " + f.find(attrs={'class': 'weeksColumn'}).text)
        semanas = f.find(attrs={'class': 'weeksColumn'}).text

        list_filmes.append({"filme": filme, "valor_acumulado" : valor_acumulado, "valor_faturado": valor_faturado, "semanas" : semanas})
        # salvarCsv(filme, valor_acumulado, valor_faturado, semanas)

    return list_filmes