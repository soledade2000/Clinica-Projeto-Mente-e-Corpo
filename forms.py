from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, TextAreaField, SelectField,
    DateField, DateTimeLocalField, IntegerField, RadioField
)
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange


# Formulário de Login
class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

# Formulário de Cadastro de Paciente
class NovoPacienteForm(FlaskForm):
    nome_completo = StringField("Nome Completo", validators=[DataRequired()])
    nome_social = StringField("Nome Social", validators=[Optional()])
    idade = IntegerField("Idade", validators=[Optional(), NumberRange(min=0, max=150)])
    data_nascimento = DateField("Data de Nascimento", format="%Y-%m-%d", validators=[DataRequired()])
    paciente_dependente = RadioField("Paciente Dependente", choices=[('sim', 'Sim'), ('nao', 'Não')], validators=[DataRequired()])
    nome_dependente = StringField("Nome do Dependente", validators=[Optional()])
    data_nascimento_dependente = DateField("Data Nascimento do Dependente", format="%Y-%m-%d", validators=[Optional()])
    idade_dependente = IntegerField("Idade do Dependente", validators=[Optional(), NumberRange(min=0, max=150)])
    endereco = TextAreaField("Endereço", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    telefone = StringField("Telefone", validators=[DataRequired()])
    escolaridade = SelectField("Escolaridade", choices=[
        ('fundamental', 'Fundamental'),
        ('medio', 'Médio'),
        ('superior', 'Superior'),
        ('pos', 'Pós-Graduação'),
        ('outro', 'Outro')
    ], validators=[DataRequired()])
    religiao = StringField("Religião", validators=[Optional()])
    estado_civil = SelectField("Estado Civil", choices=[
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)')
    ], validators=[DataRequired()])
    servico_buscado = SelectField("Serviço Buscado", choices=[
        ('consulta', 'Consulta'),
        ('terapia', 'Terapia'),
        ('exame', 'Exame'),
        ('outro', 'Outro')
    ], validators=[DataRequired()])
    servico_buscado_outro = StringField("Outro Serviço", validators=[Optional()])

    submit = SubmitField("Salvar")


# Formulário de Registro Médico
class MedicalRecordForm(FlaskForm):
    data_sessao = DateTimeLocalField('Data da Sessão', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    evolucao = TextAreaField('Evolução', validators=[DataRequired()])
    submit = SubmitField('Adicionar Evolução')

# Formulário de Agendamento
class AppointmentForm(FlaskForm):
    paciente_id = SelectField('Paciente', coerce=int, validators=[DataRequired()])
    sala = SelectField('Sala', choices=[
        ('Sala 1', 'Sala 1'),
        ('Sala 2', 'Sala 2'),
        ('Sala 3', 'Sala 3'),
        ('Sala 4', 'Sala 4'),
    ], validators=[DataRequired()])
    data_hora = DateTimeLocalField('Data e Hora', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    duracao = SelectField('Duração', choices=[
        ('30', '30 minutos'),
        ('40', '40 minutos'),
        ('60', '1 hora'),
    ], validators=[DataRequired()])
    observacoes = TextAreaField('Observações', validators=[Optional()])
    submit = SubmitField('Agendar')

# Formulário de Usuário
class UserForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(min=3, max=80)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    nome_completo = StringField('Nome Completo', validators=[DataRequired(), Length(max=120)])
    funcao = SelectField(
        'Função',
        choices=[
            ('administrador', 'Administrador'),
            ('gerencia', 'Gerência'),
            ('médico', 'Médico'),
            ('recepcao', 'Recepção')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Criar Usuário')
