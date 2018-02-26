from bs4 import BeautifulSoup

# url = "http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento"

def gastos_copa2014():
    pagina = open('copa.xml', encoding="utf8").read()
    # html = download(url)
    soup = BeautifulSoup(pagina, features="xml")
    empreendimentos = soup.find_all('copa:empreendimento')

    valor_total = 0;
    valor_gasto = 0;
    valorPrevisto = 0;
    percentual = 0;
    for e in empreendimentos:
        if e.valorTotalPrevisto:
            valor_total += float(e.valorTotalPrevisto.text)
            valorPrevisto = float(e.valorTotalPrevisto.text)
            # print(e.valorTotalPrevisto.text)

        if e.valorPercentualExecucaoFisica:
            percentual = float(e.valorPercentualExecucaoFisica.text)
            # print(e.valorPercentualExecucaoFisica.text)
            valor_gasto += valorPrevisto * (percentual / 100)

    return {'valorPrevisto':valor_total, 'valorGasto': valor_gasto}