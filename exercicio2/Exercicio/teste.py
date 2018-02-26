from bs4 import BeautifulSoup

page = open('copa.xml',  encoding="utf8").read()
soup = BeautifulSoup(page, 'xml')

empreendimentos = []

for empreendimento in soup.find_all('copa:empreendimento'):
    as_dict = {
        'id': int(empreendimento.id.text),
        'sede_id': int(empreendimento.cidadeSede.id.text),
        'sede_descricao': empreendimento.cidadeSede.descricao.text
    }
    if empreendimento.valorTotalPrevisto:
        as_dict['valor'] = float(empreendimento.valorTotalPrevisto.text)
    empreendimentos.append(as_dict)

def filter_by_sede_id(sede_id):
    total = 0.0
    sede = ""
    for empreendimento in empreendimentos:
        if empreendimento['sede_id'] == sede_id and 'valor' in empreendimento:
            if (sede == ""):
                sede = empreendimento['sede_descricao']
            total += empreendimento['valor']

for sede_id in range(1, 15):
    filter_by_sede_id(sede_id)