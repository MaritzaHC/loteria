from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    x = "sfjsldf"

    return render_template('home.html', x=x)

if __name__ == '__main__':
    app.run(debug=True)


#https://www.youtube.com/watch?v=JqUV25aFRV0