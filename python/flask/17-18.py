from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Вы находитесь на главной странице'

@app.route('/square/<int:n>')
def square(n):
    return f'Квадрат числа {n} равен {n**2}'

@app.route('/length/<string:stroka>')
def length(stroka):
    return f'Длина строки `{stroka}` = {len(stroka)}'

@app.route('/add/<int:n1>/<int:n2>')
def sum(n1, n2):
    return f'Сумма двух чисел: {n1}, {n2} = {n1+n2}'

@app.route('/error')
def error():
    return f'{1/0}'

if __name__ == '__main__':
    app.run(debug=True)