from peewee import Model, CharField, DateTimeField
from database.database import db


class User(Model):
    NOME = CharField()
    EMAIL = CharField()
    CELULAR = CharField()
    SENHA = CharField()
    # GENERO = CharField()
    # CRIADO_EM = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
