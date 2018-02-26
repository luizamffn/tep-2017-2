from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^questao/q1$', q1, name = 'q1'),
    url(r'^questao/q2$', q2, name = 'q2'),
    url(r'^questao/q2/salvarcsv$', salvar_csv, name='salvar_csv'),
    url(r'^questao/q3$', q3, name = 'q3'),
    url(r'^questao/q4$', q4, name='q4'),
    url(r'^questao/q5$', q5, name='q5'),
    url(r'^questao/q6$', q6, name='q6'),
]


