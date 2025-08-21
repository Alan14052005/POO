from datetime import datetime
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Trabajador, RegistroHorario


# INDEX
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ingreso_trabajador', methods = ['GET', 'POST'])
def ingreso_trabajador():
    return render_template('ingreso_trabajador.html')

@app.route('/ingreso_administrativo', methods = ['GET', 'POST'])
def ingreso_administrativo():
    return render_template('ingreso_administrativo.html')



# INGRESO ADMINISTRATIVO
@app.route('/generar_informe_general', methods = ['GET', 'POST'])
def generar_informe_general():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni = request.form['dni']
        
        if not legajo or not dni:
            return render_template('error.html', mensaje="Faltan datos obligatorios")
        
        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        if trabajador is None:
            return render_template('error.html', mensaje="Legajo no encontrado")
        
        if trabajador.dni[-4:] != dni:
            return render_template('error', mensaje="el DNI ingresado no coincide con el Legajo")
        
        if trabajador.funcion != 'AD':
            return render_template('error.html', mensaje="El trabajador no es del tipo administrativo")
        
        return redirect(url_for('formulario_adm', legajo = legajo))
    return render_template('generar_informe_general.html')

@app.route('/formulario_adm', methods = ['GET', 'POST'])
def formulario_adm():
    legajo = request.args.get('legajo') if request.method == 'GET' else request.form.get('legajo')
    
    if request.method == 'POST':
        fecha_inicio= request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        funcion = request.form.get('funcion', 'TODOS')
        dependencia = request.form.get('dependencia', 'TODAS')
        
        if not fecha_inicio or not fecha_fin:
            return render_template('error.html', mensaje="Debes ingresar el perío")

        filtros = [RegistroHorario.fecha.between(fecha_inicio, fecha_fin)]
                
        if funcion != 'TODOS':
            filtros.append(Trabajador.funcion == funcion)
                    
        if dependencia != 'TODAS':
            filtros.append(RegistroHorario.dependencia == dependencia)
                
        informe = RegistroHorario.query.join(Trabajador).filter(*filtros).order_by(Trabajador.apellido).all() 
        return render_template('mostrar_informe.html', informe=informe)
    return render_template('formulario_adm.html', legajo = legajo)





@app.route('/generar_informe_personal', methods = ['GET', 'POST'])
def generar_informe_personal():
    return render_template('generar_informe_personal.html')



# INGRESO TRABAJADOR 
@app.route('/registrar_entrada', methods = ['GET', 'POST'])
def registrar_entrada():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni = request.form['dni'][-4:]
        dependencia = request.form['dependencia']
        
        if not legajo or not dni or not dependencia:
            return render_template('error.html', mensaje= "Faltan datos obligatorios")
        
        trabajador = Trabajador.query.filter_by(legajo = legajo).first()
        if trabajador is None:
            return render_template('error.html', mensaje= "Legajo no encontrado" )
        
        if trabajador.dni[-4:] != dni:
            return render_template('error.html', mensaje="el DNI ingresado no coincide con el Legajo")
        
        fecha_actual = datetime.now().date()
        entrada_existente = RegistroHorario.query.filter_by(idtrabajador = trabajador.id, fecha=fecha_actual).first()
        
        
        if entrada_existente:
            return render_template('error.html', mensaje="Entrada ya registrada para hoy")
        
        nueva_entrada = RegistroHorario(idtrabajador=trabajador.id,fecha=fecha_actual,horaEntrada=datetime.now().time(),dependencia=dependencia)
        
        db.session.add(nueva_entrada)
        db.session.commit()
        
        return render_template('aviso.html', mensaje="Entrada registrada")
    return render_template('registrar_entrada.html')


@app.route('/registrar_salida', methods = ['GET', 'POST'])
def registrar_salida():
    if  request.method == 'POST': 
        legajo = request.form['legajo']
        dni = request.form['dni'][-4:]
        
        if not legajo or not dni:
            return render_template('error.html', mensaje="Debe completar todos los campos")

        trabajador = Trabajador.query.filter_by(legajo = legajo).first()
        if trabajador is None:
            return render_template('error.html', mensaje= "Legajo no encontrado") 
        
        if trabajador.dni[-4:] != dni:
            return render_template('error.html', mensaje="el DNI ingresado no coincide con el Legajo")          
        
        fecha_actual = datetime.now().date()
        entrada_existente = RegistroHorario.query.filter_by(idtrabajador = trabajador.id, fecha=fecha_actual).first()
        
        if entrada_existente:
            if entrada_existente.horaSalida is not None:
                return render_template('error.html', mensaje="La salida ya fue registrada anteriormente")
            
            entrada_existente.horaSalida = datetime.now().time()
            db.session.commit()
            return render_template('aviso.html', mensaje="Salida Registrada")
        else:
            return render_template('primero debe registrar la entrada')
        
    return render_template('registrar_salida.html')



@app.route('/consultar_registros', methods = ['GET', 'POST'])
def consultar_registros():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni = request.form['dni'][-4:]
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        
        
        if not legajo or not dni:
            return render_template('error.html', mensaje="Debe completar todos los campos")
        
        trabajador = Trabajador.query.filter_by(legajo = legajo).first()
        if trabajador is None:
            return render_template('error.html', mensaje="Legajo no encontrado")
        
        if trabajador.dni[-4:] != dni:
            return render_template('error.html', mensaje="el DNI ingresado no coincide con el Legajo")
        
        registros = RegistroHorario.query.filter(RegistroHorario.trabajador.has(id=trabajador.id), RegistroHorario.fecha.between(fecha_inicio, fecha_fin)).order_by(RegistroHorario.fecha).all()
        
        return render_template('mostrar_registros.html', registros = registros)
    return render_template('consultar_registros.html')



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
