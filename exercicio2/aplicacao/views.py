from django.shortcuts import render, redirect
from Exercicio.q1 import filmes
from Exercicio.q2 import *
from Exercicio.q3 import clima
from Exercicio.q4 import paises
from Exercicio.q5 import gastos_copa2014
from Exercicio.q6 import percorrer_estados

list_filmes2 = filme2()
# Create your views here.
def home(request):
    return render(request, 'home.html')

def q1(request):
    list_filmes = filmes()
    return render(request, 'q1.html', {'list_filmes' : list_filmes})

def q2(request):
    list_filmes2 = filme2()
    return render(request, 'q2.html', {'list_filmes2' : list_filmes2})

def q3(request):
    list_clima = clima()
    return render(request, 'q3.html', {"list_clima" : list_clima})

def q4(request):
    list_paises = paises()
    return render(request, 'q4.html', {'list_paises': list_paises})

def q5(request):
    gastos_totais = gastos_copa2014()
    return render(request, 'q5.html', {'gastos_totais': gastos_totais})

def q6(request):
    estados = percorrer_estados()
    return render(request, 'q6.html', {'estados': estados})

def salvar_csv(request):
    for f in list_filmes2:
        salvarCsv(f['filme'], f['valor_acumulado'], f['valor_faturado'], f['semanas'])
    return redirect('q2')