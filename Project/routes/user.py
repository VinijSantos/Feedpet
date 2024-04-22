from flask import Blueprint, render_template, url_for
from database.t_users import users_list

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


@user_route.route('/')
def menu_principal():
    return "Menu principal do usuario"


@user_route.route('/new')
def register_page():
    return render_template('registerpage.html')


@user_route.route('/edit')
def edit_page():
    return render_template('editpage.html')
