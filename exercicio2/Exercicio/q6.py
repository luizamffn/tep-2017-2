from bs4 import BeautifulSoup

# url = "http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento"

estados= []
estados_por_id =[]
def estados_():
    pagina = open('copa.xml', encoding="utf8").read()
    # html = download(url)
    soup = BeautifulSoup(pagina, features="xml")
    empreendimentos = soup.find_all('copa:empreendimento')

    for e in empreendimentos:
        if e.valorTotalPrevisto:
            estados.append({"id": e.cidadeSede.id.text, "cidade": e.cidadeSede.descricao.text, "valor": e.valorTotalPrevisto.text})
        else:
            estados.append({"id": e.cidadeSede.id.text, "cidade": e.cidadeSede.descricao.text, "valor": 0})

def gastos_por_Estado(id):
    valor_total = 0
    nome_estado = ""
    print("id ", id)
    for estado in estados:
        if (int(estado['id']) == id):
            if (nome_estado == ""):
                nome_estado = estado['cidade']
            valor_total += float(estado['valor'])

    estados_por_id.append({'estado': nome_estado, 'valor_gasto': valor_total})

def percorrer_estados():
    estados_()
    for i in range(1,15):
        gastos_por_Estado(i)

    return estados_por_id