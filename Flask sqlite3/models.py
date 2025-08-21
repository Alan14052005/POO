from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Trabajador(db.Model):
    __tablename__='trabajador'
    id = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String(80), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(10), nullable=False)
    correo = db.Column(db.String(80), unique=True, nullable=False)
    legajo = db.Column(db.String(80), nullable=False)
    horas = db.Column(db.String(80), nullable=False)
    funcion = db.Column(db.String(80), nullable=False)
    registro_horario = db.relationship('RegistroHorario', backref='trabajador',cascade="all, delete-orphan")
    
class RegistroHorario(db.Model):
    __tablename__='registrohorario'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    horaEntrada = db.Column(db.Time, nullable = False)
    horaSalida = db.Column(db.Time, nullable = False)
    dependencia = db.Column(db.String(80), nullable = False)
    idtrabajador = db.Column(db.Integer, db.ForeignKey('trabajador.id'), nullable = False)
    