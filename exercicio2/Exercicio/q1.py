from bs4 import BeautifulSoup
from Exercicio.testeRequests import download
from selenium import webdriver

def filmes ():
    browser = webdriver.Chrome()
    browser.get('https://www.rottentomatoes.com/browse/tv-list-1')

    filmes = browser.find_elements_by_css_selector('.movie_info')
    filmes_percentual = []

    for f in filmes:
        try:
            percentual = f.find_element_by_css_selector('.tMeterScore').text
            # print(f.find_element_by_css_selector('.movieTitle').text + " - " + percentual)
            filmes_percentual.append({"filme": f.find_element_by_css_selector('.movieTitle').text, "percentual" : percentual})
        except:
            pass

    browser.close()
    return filmes_percentual