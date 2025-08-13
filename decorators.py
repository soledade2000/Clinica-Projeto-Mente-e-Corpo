from functools import wraps
from flask_login import current_user
from flask import flash, redirect, url_for
from app import login_manager  # Certifique-se que importou corretamente

def role_required(role):
    """Decorator para permitir acesso somente a um papel específico."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            if current_user.funcao != role:
                flash(f"Acesso negado. Apenas usuários com a função '{role}' podem acessar esta página.", 'danger')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def roles_required(*roles):
    """Decorator para permitir acesso a múltiplas funções."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            if current_user.funcao not in roles:
                roles_str = ', '.join(roles)
                flash(f"Acesso negado. Apenas usuários com as funções {roles_str} podem acessar esta página.", 'danger')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
