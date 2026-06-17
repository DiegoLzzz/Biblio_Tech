from flask_wtf import FlaskForm
from wtforms   import StringField, FloatField, IntegerField, DateField, SelectField, PasswordField, SubmitField  
from wtforms.validators import DataRequired, NumberRange, Email, Optional, EqualTo, ValidationError
from app.models         import Produto, User
from app import bcrypt, db


class UserForm(FlaskForm):
    name             = StringField('Primeiro nome:',          validators = [DataRequired()])
    last_name        = StringField('Sobrenome:',              validators = [DataRequired()])
    email            = StringField('E-mail',                  validators = [DataRequired(), Email()])
    password         = PasswordField('Senha:',                validators = [DataRequired()])
    pwd_confirmation = PasswordField('Confirmação de Senha:', validators = [DataRequired(), EqualTo('password')])
    role             = SelectField('Nível de Acesso', choices = [('Prof', 'Professor'), ('admin', 'Administrador'), ('Alu', 'Aluno')], validators = [DataRequired()])
    btn_submit       = SubmitField("Cadastrar")

    def saveUser(self):
        pwd  = bcrypt.generate_password_hash(self.password.data.encode('utf-8'))
        user = User(name       = self.name.data,
                    last_name  = self.last_name.data,
                    email      = self.email.data,
                    password   = pwd)
        db.session.add(user)
        db.session.commit()
        return user
