from flask import Blueprint, render_template
from app import get_connection

ola = Blueprint('main', __name__)

@ola.route('/')
def index():
    return render_template('index.html', title='Página Inicial')

@ola.route('/ola')
def ola_mundo():
    
    return "Olá, Mundo!"