from flask import Blueprint, render_template
from app import get_connection

escola_bp = Blueprint('escola', __name__)

@escola_bp.route('/criarConta')
def criarConta():

    return render_template('criarConta.html', title='Criar Conta')

