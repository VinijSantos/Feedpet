from peewee import *
from database.database import db


class User(Model):
    NOME = CharField()
    EMAIL = CharField(unique=True)
    CELULAR = CharField()
    SENHA = CharField()
    # GENERO = CharField()
    # CRIADO_EM = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Horarios(Model):
    NOME = ForeignKeyField(User, backref='usuarios')
    HORARIO = CharField()

    class Meta:
        database = db
