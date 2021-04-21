import os
import csv
from datetime import datetime
from mongoengine import connect
from models.Vacinacao import Vacinacao

connect('vacinacao-test')

nome_arquivo = '20210420_vacinometro.csv'
informacao_data = nome_arquivo.split('_')[0]
ano = int(informacao_data[0:4])
mes = int(informacao_data[4:6])
dia = int(informacao_data[6:8])
data_atualizacao = datetime(ano, mes, dia)

diretorio_atual = os.path.dirname(__file__)
caminho_arquivo = os.path.join(
    diretorio_atual, '../data/' + nome_arquivo)
with open(caminho_arquivo, encoding='utf8') as arquivo:
    conteudo_csv = csv.reader(arquivo)
    cabecalhos = next(conteudo_csv)
    for linha in conteudo_csv:
        municipio, dose, aux = linha[0].split(';')
        total_doses_aplicadas = int(aux)
        v = Vacinacao(
            municipio=municipio,
            dose=dose,
            total_doses_aplicadas=total_doses_aplicadas,
            data_atualizacao=data_atualizacao
        )
        v.save()
