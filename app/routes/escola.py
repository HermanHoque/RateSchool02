from flask import Blueprint, render_template
from app import get_connection

escola_bp = Blueprint('escola', __name__)

@escola_bp.route('/criarConta')
def criarConta():

    return render_template('escola/criarConta.html', title='Criar Conta')


@escola_bp.route('/loginEscola')
def login():

    return render_template('escola/login.html', title='Login Escola')
