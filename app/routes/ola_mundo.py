from flask import Blueprint, render_template
from app import get_connection

ola_bp = Blueprint('ola', __name__)

@ola_bp.route('/')
def index():
    return render_template('index.html', title='Página Inicial')

@ola_bp.route('/ola')
def ola_mundo():
    
    return "Olá, Mundo!"