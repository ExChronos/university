from flask import Flask

app = Flask(__name__)

@app.route('/square/<int:n>')
def square(n):
    return f'Квадрат числа {n} равен {n**2}'

if __name__ == '__main__':
    app.run(debug=True)