import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# --- Configuração do App ---
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'uma-chave-super-secreta-para-desenvolvimento')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'
login_manager.login_message_category = 'warning'

# Importar modelos, rotas e decoradores após instanciar app, db, login_manager
from models import User
from routes import *
from decorators import *

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Comando para criar usuário admin via CLI
@app.cli.command("create-admin")
def create_admin():
    from werkzeug.security import generate_password_hash
    if User.query.filter_by(username='admin').first():
        print("Usuário 'admin' já existe.")
        return

    print("Criando usuário admin inicial...")
    admin_user = User(
        username='admin',
        senha=generate_password_hash('admin123', method='pbkdf2:sha256'),
        nome_completo='Dr. Admin',
        funcao='médico'
    )
    db.session.add(admin_user)
    db.session.commit()
    print("Usuário 'admin' com senha 'admin123' criado com sucesso.")
    print("Você também pode criar outros usuários (ex: recepcao) se desejar.")
