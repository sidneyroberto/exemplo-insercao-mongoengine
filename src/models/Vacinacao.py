from mongoengine import *


class Vacinacao(Document):
    municipio = StringField(required=True)
    dose = StringField(required=True)
    total_doses_aplicadas = IntField(required=True)
    data_atualizacao = DateTimeField(required=True)
