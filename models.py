from datetime import datetime
from app import db
from flask_login import UserMixin
from enum import Enum
from datetime import date
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    nome_completo = db.Column(db.String(120), nullable=False)
    funcao = db.Column(db.String(50), nullable=False)  # Ex: médico, recepcao

class UserRole(Enum):
    ADMINISTRADOR = "administrador"
    MEDICO = "médico"
    GERENCIA = "gerencia"
    RECEPCAO = "recepcao"

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(150), nullable=False)
    nome_social = db.Column(db.String(150))
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.Date, nullable=False)

    paciente_dependente = db.Column(db.String(10))  # 'nao', 'sim', 'outro' — nome alinhado com form
    nome_dependente = db.Column(db.String(150))
    data_nascimento_dependente = db.Column(db.Date)  # nome alinhado com form
    idade_dependente = db.Column(db.Integer)

    endereco = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    escolaridade = db.Column(db.String(50), nullable=False)
    religiao = db.Column(db.String(100))
    estado_civil = db.Column(db.String(50), nullable=False)

    servico_buscado = db.Column(db.String(50), nullable=False)
    servico_buscado_outro = db.Column(db.String(150))

    @property
    def nome(self):
        return self.nome_completo

    def calcula_idade(self):
        if self.data_nascimento:
            today = date.today()
            return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return None

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sala = db.Column(db.String(20))
    data_hora = db.Column(db.DateTime, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    duracao = db.Column(db.Integer, nullable=False)  # duração em minutos
    observacoes = db.Column(db.Text)

    paciente = db.relationship('Patient', backref='appointments')
    doctor = db.relationship('User', backref=db.backref('appointments', lazy=True))

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data_sessao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    evolucao = db.Column(db.Text, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.relationship('User', backref='medical_records')
