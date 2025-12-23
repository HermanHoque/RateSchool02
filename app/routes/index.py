from flask import Blueprint, render_template
from app import get_connection

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html', title='Home')

@index_bp.route('/sobre-nos')
def sobreNos():
    return render_template('sobreNos.html', title='Sobre Nós')
