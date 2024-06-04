from flask import Blueprint, render_template, url_for, request
from database.database import db
from database.models.usuario import User

landing_route = Blueprint('landing', __name__)

lista_integrantes = [
    "amanda",
    "caio",
    "ednaldo",
    "leticia",
    "vini"
]


@landing_route.route('/')
def landing_page():
    return render_template('index.html', lista_integrantes=lista_integrantes)


@landing_route.route('/details')
def detail_page():
    return render_template('detailpage.html')


@landing_route.route('/', methods=["POST"])
def login():
    dados_login = request.form

    try:
        valid = User.get(
            User.EMAIL == dados_login['email'],
            User.SENHA == dados_login['senha']
        )
        var_ok = 1
    except:
        valid = "Usuario inexistente"
        var_ok = 0

    print(valid)

    if (var_ok == 1):
        template = render_template('menupage.html')
    else:
        template = render_template(
            'index.html', lista_integrantes=lista_integrantes
        )
    return template


@landing_route.route('/register_sucess', methods=['POST'])
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

    return render_template('sucesso_registro.html')


@landing_route.route('/new')
def register_page():
    return render_template('registerpage.html')


@landing_route.route('/menu')
def menu_page():
    return render_template('menupage.html')


@landing_route.route('/edit')
def edit_page():
    return render_template('editpage.html')
