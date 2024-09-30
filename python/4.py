import random
from time import sleep

class Hero:
    def __init__(self, name, health, armor, power, weapon):
        self.name=name
        self.health=health
        self.armor=armor
        self.power=power
        self.weapon=weapon

    def print_info(self):
        print(f'Поприветствуйте героя -> {self.name}')
        print(f'Уровень здоровья -> {self.health}')
        print(f'Уровень брони -> {self.armor}')
        print(f'Запас силы -> {self.power}')
        print(f'Тип оружия -> {self.weapon}')
    
    def strike(self, enemy):
        print('-> УДАР!')
        print(f'{self.name} атакует {enemy.name} используя {self.weapon}\n')

        enemy.armor -= self.power

        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor=0
        
        print(f'{enemy.name} покачнулся\n')
        print(f'класс брони упал до {enemy.armor}')
        print(f'уровень здоровья упал до {enemy.health}')


knight = Hero('Knight', 600, 150, 75, 'Sword')
barbarian = Hero('Barbarian', 700, 100, 125, 'Club')

play = True

while play:
    turn = random.randint(0, 1)
    if(turn == 0):
        knight.strike(barbarian)

        if(barbarian.health <= 0):
            print('Рыцарь победил\n')
            play = False
            break

        else:
            print('Следующий ход\n')
    elif(turn == 1):
        barbarian.strike(knight)

        if(knight.health <= 0):
            print('Варвар победил\n')
            play = False
            break

        else:
            print('Следующий ход')
    print('________________________________________')
    sleep(2)

