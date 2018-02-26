from bs4 import BeautifulSoup
from utilitario import download

url = "https://servicodados.ibge.gov.br/api/v1/censos/nomes/basica?nome="

nome = input("Digite o nome: ")
pagina = download(url+ nome)
pagina = (pagina.replace('}]', "")).replace('[{', "")
valores = (pagina.split(",\""))

for v in valores:
    if(v.__contains__("freq")):
        print((v.replace("\"", "")))
    elif (v.__contains__("nomes")):
        print((v.replace("\"", "")).replace("nomes", "Nomes semelhantes"))

