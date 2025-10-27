from flask import Blueprint, render_template
from app import get_connection

ola_bp = Blueprint('ola', __name__)

@ola_bp.route('/')
def index():
    return render_template('index.html', title='Home')

@ola_bp.route('/CriarConta')
def ola_mundo():
    
    return render_template('criarConta.html', title='Criar Conta')