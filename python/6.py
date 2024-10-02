# задание №1 - участники хакатона
class User:
    def __init__(self, name, sname, age, lang) -> None:
        self.name=name
        self.sname=sname
        self.age=age
        self.lang=lang
    def ret_age(self):
        return self.age
    
def take_info():
    count = int(input('Сколько будет участников?\n>>> '))
    users = list()

    for i in range(count):
        new_user = input('Введите имя, фамилию, возраст и ЯП через пробел:\n').split()
        users.append(User(new_user[0], new_user[1], int(new_user[2]), new_user[3]))
    
    return users

def ungest_user(args):
    ung = args[0].ret_age()
    user = args[0]

    for i in range(len(args)):
        age = args[i].ret_age()
        if ung > age:
            user=args[i]
            ung=age
    print(f'Самый молодой участник: {user.name}. Он(а) программирует на {user.lang} в возрасте {user.age} лет')

# задание №2 - ведение учета закаов от блогеров
def take_orders():
    count = int(input('Сколько будет услуг?\n>>>'))
    orders = dict()

    for i in range(count):
        services = input('Введите название услуги и количество через пробел\n>>> ').split()
        orders[services[0]]=int(services[1])
    
    return orders

def show_orders():
    args = take_orders()
    total_count = 0
    category_count = 0
    for key in args:
        print(f'Услуга: {key} в размере {args[key]}')
        if args[key] == 0:
            continue
        else:
            category_count+=1
            total_count+=args[key]
    return f'Общее количество заказанных услуг: {total_count}. Количество категорий по заказанным услугам: {category_count}'

print(show_orders())