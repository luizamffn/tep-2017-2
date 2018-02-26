from bs4 import BeautifulSoup
from utilitario import download

def download_tags(link):
    pagina = download(link)
    soup = BeautifulSoup(pagina, 'html5lib')
    tags = soup.find(attrs={"class": "tags_section"})
    try:
        links = tags.find_all('a')
        info_tags = "Tags: ";
        for i in links:
            info_tags += i.text + " "
        print(info_tags)
    except:
        print("Não pussui tags")

url = "http://www.pi.gov.br/"

pagina = download(url)
soup = BeautifulSoup(pagina, 'html5lib')
container = soup.find(attrs={"class":"thumbnails_container"})
materias = container.find_all('li')
for m in materias:
    informacoes = m.find(attrs={"class": "post_text"})
    link = informacoes.find('a')['href']
    titulo = informacoes.find('h4').text
    print(titulo)
    print(url + link)
    download_tags(url + link)
    print()

