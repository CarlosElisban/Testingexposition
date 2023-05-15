from flask import Flask, render_template, request, flash, redirect, url_for
import pymysql

app = Flask(__name__)
app.secret_key = 'bestteam'


def connect():
    return pymysql.connect(
        host='localhost',
        password='clavenueva',
        user='root',
        db='ejerciciopractico',
        port=3306
    )

@app.route('/', methods=['GET'])
def inicio():
    return render_template('Form.html')

@app.route('/registrar', methods=['POST'])
def registrar_usuario():
    connection = connect()
    cursor = connection.cursor()
    if request.method == 'POST':
        Name = request.form['name']
        Age = request.form['age']
        Gender = request.form['gender']
        Interests = ','.join(request.form.getlist('interests'))  # Convertir la lista en una cadena separada por comas
        Subscription = request.form['subscription']

        # Insertar el nuevo usuario en la tabla Cliente
        query = "INSERT INTO users (name, age, gender, interests, subscription) VALUES (%s, %s, %s, %s, %s)"
        values = (Name, Age, Gender, Interests, Subscription)
        cursor.execute(query, values)

        connection.commit()
        cursor.close()
        connection.close()

        flash('Registro exitoso. Por favor inicia sesión.', 'success')
        return render_template('datos.html', name=Name, age=Age, gender=Gender, interests=Interests, subscription=Subscription)

    return render_template('Form.html')


if __name__ == '__main__':
    app.run()
