import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier, OutputCodeClassifier
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

#1. Leia o dataset usando o pandas
train_df = pd.read_csv('train.csv', parse_dates=['Dates'])

#2. Elimine as colunas Address, Resolution, X, Y e Descript.
train_df = train_df.drop(columns=['Address','Resolution','X','Y','Descript'])
# print(train_df.head(4))


#3. Verifique se há campos nulos e tome eventuais decisões
for field in train_df.columns:
   print(field, train_df[field].isnull().sum())


#4. Trate as colunas DayOfWeek e PdDistrict de uma forma que possam serprocessadas
train_df['DayOfWeek'] = train_df['DayOfWeek'].map({'Sunday' : 1, 'Monday' : 2,'Tuesday' : 3,
                                                   'Wednesday' : 4, 'Thursday' : 5, 'Friday' : 6, 'Saturday' : 7}).astype(int)
train_df['PdDistrict'] = train_df['PdDistrict'].map({'SOUTHERN': 0, 'NORTHERN' : 1, 'PARK' : 2,'INGLESIDE' : 3, 'BAYVIEW' : 4,
                                                     'RICHMOND' : 5, 'CENTRAL' : 6, 'TARAVAL' : 7, 'TENDERLOIN':8,
                                                     'MISSION':9}).astype(int)

# print(train_df)

#5. Crie coluna chamada estacao com formato string represente uma estação do ano
train_df["date_month"] = train_df["Dates"].dt.month
train_df['estacao'] = train_df['date_month'].map({12 : 'Inverno', 1 : 'Inverno', 2: 'Primavera',
                                             3: 'Primavera', 4: 'Primavera', 5: 'Verão',
                                             6: 'Verão', 7: 'Verão', 8: 'Outono',
                                             9: 'Outono', 10: 'Outono', 11: 'Inverno'})

train_df = train_df.drop(columns= 'date_month')
print(train_df)


#6. Trate a coluna de uma forma que ela possa ser processada
train_df['estacao'] = train_df['estacao'].map({'Inverno':12, 'Inverno':1, 'Primavera': 2,
                                             'Primavera':3, 'Primavera':4, 'Verão':5,
                                             'Verão':6, 'Verão':7, 'Outono':8,
                                             'Outono':9, 'Outono':10, 'Inverno':11})

print(train_df)

#7. Crie uma coluna chamada ocorrencia_noturna que terá 1 caso tenha sido entre 18
#e 5h da manhã. Sabendo-se que podemos acessar o campo hora da data a partir
#de train["Dates"].dt.hour
train_df["date_hour"] = train_df["Dates"].dt.hour
train_df["ocorrencia_noturna"] = 0

for dataset in [train_df]:
    dataset.loc[((dataset['date_hour'] > 18) | (dataset['date_hour'] < 5 )), 'ocorrencia_noturna'] = 1

train_df = train_df.drop(columns= 'date_hour')
print(train_df)

#8. Mapeie todas as categorias em números
print(train_df.Category.unique())
train_df['Category'] = train_df['Category'].map({'WARRANTS' : 0,'OTHER OFFENSES' : 1,'LARCENY/THEFT' : 2,
                                                 'VEHICLE THEFT' : 3, 'VANDALISM' : 4, 'NON-CRIMINAL' : 5,
                                                 'ROBBERY' : 6, 'ASSAULT' : 7, 'WEAPON LAWS' : 8,
                                                 'BURGLARY' : 9, 'SUSPICIOUS OCC' : 10, 'DRUNKENNESS' : 11,
                                                 'FORGERY/COUNTERFEITING' : 12, 'DRUG/NARCOTIC' : 13, 'STOLEN PROPERTY' : 14,
                                                 'SECONDARY CODES' : 15, 'TRESPASS' : 16, 'MISSING PERSON' : 17,
                                                 'FRAUD' : 18, 'KIDNAPPING' : 19, 'RUNAWAY' : 20,
                                                 'DRIVING UNDER THE INFLUENCE' : 21, 'SEX OFFENSES FORCIBLE' : 22,
                                                 'PROSTITUTION' : 23, 'DISORDERLY CONDUCT' : 24, 'ARSON' : 25,
                                                 'FAMILY OFFENSES' : 26, 'LIQUOR LAWS' : 27, 'BRIBERY' : 28,
                                                 'EMBEZZLEMENT' : 29, 'SUICIDE' : 30, 'LOITERING' : 31,
                                                 'SEX OFFENSES NON FORCIBLE' : 32, 'EXTORTION' : 33, 'GAMBLING' : 34,
                                                 'BAD CHECKS' : 35, 'TREA' : 36, 'RECOVERED VEHICLE' : 37,
                                                 'PORNOGRAPHY/OBSCENE MAT' : 38}).astype(int)

#9. Separe para treino os 800.000 primeiros registros e para testes os demais;
# definindo dataframes
dump_data = train_df[['Category','DayOfWeek', 'PdDistrict', 'estacao', 'ocorrencia_noturna']]
dump_answers = train_df['Category']

# variáveis categóricas
data = pd.get_dummies(dump_data).values
answers = dump_answers.values

#definição de treino, teste e validação
tamanho_de_treino = int(800000)
tamanho_de_teste = int(len(answers) - 800000)
tamanho_de_validacao = len(answers) - tamanho_de_treino - tamanho_de_teste

# 10. Aplique os dados de treino e teste para os seguintes algoritmos e para cada um
# verifique o percentual de acerto.
treino_dados = data[:tamanho_de_treino]
treino_marcacoes = answers[:tamanho_de_treino]

fim_de_treino = tamanho_de_treino + tamanho_de_teste

teste_dados = data[tamanho_de_treino:fim_de_treino]
teste_marcacoes = answers[tamanho_de_treino:fim_de_treino]

validacao_dados = data[fim_de_treino:]
validacao_marcacoes = answers[fim_de_treino:]

def fit_and_predict(nome,modelo,treino_dados, treino_marcacoes,teste_dados, teste_marcacoes):
    modelo.fit(treino_dados, treino_marcacoes)
    resultado = modelo.predict(teste_dados)

    print(resultado)
    # print(teste_marcacoes)

    acertos = 0
    tamanho = len(teste_marcacoes)
    for i in range(tamanho):
        if teste_marcacoes[i] == resultado[i]:
            acertos = acertos + 1

    print('%s: %.2f' % (nome, (acertos * 100/ tamanho)))

modeloMultinomial = MultinomialNB()
fit_and_predict("MultinomialNB", modeloMultinomial, treino_dados,treino_marcacoes, teste_dados, teste_marcacoes)

modeloAdaBoost = AdaBoostClassifier()
fit_and_predict("AdaBoostClassifier", modeloAdaBoost, treino_dados,treino_marcacoes, teste_dados, teste_marcacoes)

modeloOneVsRest = OneVsRestClassifier(LinearSVC(random_state = 0))
resultadoOneVsRest = fit_and_predict("OneVsRest", modeloOneVsRest,treino_dados, treino_marcacoes,teste_dados, teste_marcacoes)

modeloOneVsOne = OneVsOneClassifier(LinearSVC(random_state = 0))
resultadoOneVsOne = fit_and_predict("OneVsOne", modeloOneVsOne,treino_dados, treino_marcacoes,teste_dados, teste_marcacoes)

modeloRandomForest = RandomForestClassifier()
fit_and_predict("RandomForest", modeloRandomForest, treino_dados,treino_marcacoes, teste_dados, teste_marcacoes)

# 11. Refaça suas avaliações considerando k-fold com valor 6
# Entrega: os scripts e os resultados por algoritmo.
def k_folding(k, nome, modelo, treino_dados, treino_marcacoes):
    scores = cross_val_score(modelo,treino_dados,treino_marcacoes,cv = k)
    print("%s %.2f" %(nome,(np.mean(scores)*100.0)))

k_folding(6, "MultinomialNB",modeloMultinomial, treino_dados, treino_marcacoes)
k_folding(6, "AdaBoost",modeloAdaBoost, treino_dados, treino_marcacoes)
k_folding(6, "OneVsRest",modeloOneVsRest, treino_dados, treino_marcacoes)
k_folding(6, "OneVsOne",modeloOneVsOne, treino_dados, treino_marcacoes)
k_folding(6, "RandomForest",modeloRandomForest, treino_dados, treino_marcacoes)