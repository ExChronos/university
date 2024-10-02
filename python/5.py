import random
from time import sleep

class Hero:
    def __init__(self, name, health, armor, power):
        self.name=name
        self.health=health
        self.armor=armor
        self.power=power
        self.new=True

    def refill(self, heal):
        self.health=heal
        self.armor=0
    
    def show_info(self):
        print(f'{self.name} обладает {self.health} ОЗ и {self.armor} ОБ')

    def check_alive(self):
        if self.health <= 0:
            return False
        else:
            return True
    
    def strike(self, enemy):
        chanse = random.randint(0, 6)

        if(chanse == 0 or chanse == 1):
            print('Промах! В следующий раз повезет...')
        elif(chanse == 2 or chanse == 3):
            if enemy.armor > 0:
                enemy.armor -= self.power*0.4
                enemy.health -= self.power*0.2
                print(f'{self.name} наносит {self.power*0.2} ед урона здоровью и {self.power*0.4} ед броне')
            else:
                enemy.health -= self.power*0.6
                print(f'{self.name} наносит {self.power*0.6} ед урона здоровью')
        elif(chanse == 4 or chanse == 5):
            if enemy.armor > 0:
                enemy.armor -= self.power*0.6
                enemy.health -= self.power*0.4
                print(f'{self.name} наносит {self.power*0.4} ед урона здоровью и {self.power*0.6} ед броне')
            else:
                enemy.health -= self.power*0.6
                print(f'{self.name} наносит {self.power*0.6} ед урона здоровью')
        elif(chanse == 6):
            if enemy.armor > 0:
                enemy.armor -= self.power
                enemy.health -= self.power*0.8
                print(f'{self.name} наносит {self.power*0.8} ед урона здоровью и {self.power} ед броне')
            else:
                enemy.health -= self.power
                print(f'{self.name} наносит {self.power} ед урона здоровью')
        
        print(f'{self.name} имеет {self.health} ОЗ и {self.armor} ОБ')

class Dragon(Hero):
    def __init__(self, name, health, armor, power):
        super().__init__(name, health, armor, power)
        self.type='Дракон'
        
    def hello(self):
        if self.new == True:
            print(f'Где-то неподалеку раздается шум. Перед вами появляется {self.type} - {self.name}')
            self.new = False
        else:
            print(f'Перед вами появляется {self.name}')
            super().show_info()
    def attack(self, enemy):
        print(f'{self.name} атакует {enemy.name}')
        super().strike(enemy)
    
class Warrior(Hero):
    def __init__(self, name, health, armor, power):
        super().__init__(name, health, armor, power)
        self.type='Разбойник'
    def hello(self):
        if self.new == True:
            print(f'Где-то неподалеку раздается шум. Перед вами появляется {self.type} - {self.name}')
            self.new = False
        else:
            print(f'Перед вами появляется {self.name}')
            super().show_info()
    def attack(self, enemy):
        print(f'{self.name} атакует {enemy.name}')
        super().strike(enemy)

knight = Hero('Arthur', 1000, 500, 150)

enemies = dict()
enemies[0] = Dragon('Маур', 3000, 2000, 500)
enemies[1] = Dragon('Норберт', 1500, 1000, 200)
enemies[2] = Warrior('Исикава', 450, 100, 100)
enemies[3] = Warrior('Юрай', 150, 170, 270)

play = True

while play:
    turn = random.randint(0,3)

    enemies[turn].hello()
    enemies[turn].show_info()
    
    knight.show_info()
    answer = input('Желаете ли сразиться? (да/нет)\n')

    if answer[0].lower() == 'д':
        print('Атака началась')
        alive = knight.check_alive()
        survive = enemies[turn].check_alive()

        while alive and survive:
            now_turn = random.randint(0,1)

            if now_turn == 0:
                knight.strike(enemies[turn])

                survive=enemies[turn].check_alive()
                alive=knight.check_alive()

                if(not alive):
                    print(enemies[turn].show_info())
                    print('___________________________________\nГерой умер. Вы проиграли. Удачи в следующий раз\n__________________________________')
                    play=False

                if(not(survive) and (len(enemies.keys()) == 0)):
                    print('_____________________\nВы выиграли эту партию\n________________________')
                    play=False
                elif(not survive):
                    print('_____________________\nПротивник повержен!\n______________________')
                    del enemies[turn]
                    knight.refill(1000)

            elif now_turn == 1:
                enemies[turn].strike(knight)

                alive=knight.check_alive()
                survive=enemies[turn].check_alive()

                if(not(survive) and (len(enemies.keys()) == 0)):
                    print('_____________________\nВы выиграли эту партию\n________________________')
                    play=False
                elif(not survive):
                    print('_____________________\nПротивник повержен!\n______________________')
                    del enemies[turn]
                    knight.refill(1000)
                
                if(not alive):
                    print(enemies[turn].show_info())
                    print('___________________________________\nГерой умер. Вы проиграли. Удачи в следующий раз\n__________________________________')
                    play=False
                


            sleep(1)


    elif answer[0].lower() == 'н':
        print('Вы продолжаете путь')
        continue

