from bs4 import BeautifulSoup
from Exercicio.testeRequests import download

from selenium import webdriver

def clima():
    url = "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/264/teresina-pi"

    temperaturas = []

    html = download(url)
    # print(html)
    soup = BeautifulSoup(html, 'html5lib')
    tabela = (soup.find(attrs={'id': 'forecast-first-period'}))
    primeiro_dia = (tabela.find(attrs={'id': 'resumeDay-0'}).find_all(attrs={'class': 'temperature-block'}))
    temperaturas.append({"dia": tabela.find(attrs={'id': 'resumeDay-0'}).find(attrs={'class':'title'})['data-dia'],
                         "maxima": primeiro_dia[0].find('p').text,
                         "minima": primeiro_dia[1].find('p').text})

    temperaturas.append({"dia": tabela.find(attrs={'id': 'resumeDay-1'}).find(attrs={'class': 'title'})['data-dia'],
                         "maxima": tabela.find(attrs={'id': 'tempMax1'}).text,
                         "minima": tabela.find(attrs={'id': 'tempMin1'}).text})

    temperaturas.append({"dia": tabela.find(attrs={'id': 'resumeDay-2'}).find(attrs={'class': 'title'})['data-dia'],
                         "maxima": tabela.find(attrs={'id': 'tempMax2'}).text,
                         "minima": tabela.find(attrs={'id': 'tempMin2'}).text})

    temperaturas.append({"dia": tabela.find(attrs={'id': 'resumeDay-3'}).find(attrs={'class': 'title'})['data-dia'],
                         "maxima": tabela.find(attrs={'id': 'tempMax3'}).text,
                         "minima": tabela.find(attrs={'id': 'tempMin3'}).text})

    temperaturas.append({"dia": tabela.find(attrs={'id': 'resumeDay-4'}).find(attrs={'class': 'title'})['data-dia'],
                         "maxima": tabela.find(attrs={'id': 'tempMax4'}).text,
                         "minima": tabela.find(attrs={'id': 'tempMin4'}).text})


    return temperaturas