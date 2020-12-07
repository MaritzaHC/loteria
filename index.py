from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    cantidad = 0
    return render_template('home.html', cantidad=cantidad)

@app.route('/nuevoSorteo', methods = ['POST'])
def nuevoSorteo():
    data = request.form
    print(data)
    cantidad = 50
    return render_template('home.html',cantidad = cantidad)

if __name__ == '__main__':
    app.run(debug=True)

#https://www.youtube.com/watch?v=JqUV25aFRV0