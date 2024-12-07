from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Добро пожаловать на главную страницу'

@app.route('/about')
def about():
    return 'Это страница о нас'

@app.route('/services')
def services():
    return 'Наши услуги: {}, {}, {}'.format('Консалтинг', 'Разработка', 'Поддержка')

@app.route('/services/<n>/')
def service_n(n):
    return f'Наши услуги: {n}'

if __name__ == '__main__':
    app.run(debug=True)