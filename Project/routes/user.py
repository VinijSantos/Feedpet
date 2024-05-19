from flask import Blueprint, render_template, url_for, request
from database.database import db
from database.models.usuario import User

# from database.t_users import users_list

user_route = Blueprint('user', __name__)

"""
    Rotas para users:

    /user/ (GET) -> Vai listar os clientes
    /user/ (POST) -> Vai inserir o cliente no servidor
    /user/new (GET) -> vai renderizar a pagina de cadastro de leticia
    /user/<id> (GET) -> vai renderizar o menu principal 
    /user/<id>/edit (GET) -> vai renderizar a editpage
    /user/<id>/update (PUT) -> vai inputar as alterações feitas pelo editpage
    /user/<id>/delete (DELETE) -> vai deletar os dados do usuario
"""


@user_route.route('/', methods=['POST'])
def inserir_usuario():
    data = request.form

    User.create(
        NOME=data['nome'] + ' ' + data['sobrenome'],
        EMAIL=data['email'],
        CELULAR=data['celular'],
        SENHA=data['senha']
    )

    usuario_registrado = User.select()

    for u in usuario_registrado:
        print(u.NOME, u.EMAIL, u.CELULAR, u.SENHA)

    return render_template('index.html')


@user_route.route('/new')
def register_page():
    return render_template('registerpage.html')


@user_route.route('/menu')
def menu_page():
    return render_template('menupage.html')


@user_route.route('/edit')
def edit_page():
    return render_template('editpage.html')
