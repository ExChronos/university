# 1 - призраки PacMan
# 2 - дополняем призрака
# 3 - расширяем игру

from time import sleep
import random

class Ghost:
    def __init__(self, name, color, strategy, speed):
        self.name=name
        self.color=color
        self.strategy=strategy
        self.speed=speed
    def print_info(self):
        print(f'Цвет персонажа: {self.color}')
        print(f'Имя персонажа: {self.name}')
        print(f'Стратегия, которой придерживается: {self.strategy}')
        print(f'Скорость: {self.speed}')
    def print_string(self):
        print(f'{self.name} поймал пакмана')

class PacMan:
    def __init__(self):
        self.point=0
        self.lives=5
    
    def eat_points(self):
        cur_points = random.randint(20, 50)
        self.point+=cur_points
        return cur_points
    
    def go(self):
        direction=random.randint(1,4)
        return direction

pacman = PacMan()

characters = list()
billy =  Ghost('Billy', 'orange', 'прятаться', 10)
andre = Ghost('Andre', 'green', 'лидер', 7)
sharpen = Ghost('Sharpen', 'purple', 'переговорщик', 5)
cryne = Ghost('Cryne', 'red', 'воин', 8)
characters.append(billy)
characters.append(andre)
characters.append(sharpen)
characters.append(cryne)

play = True

while play:
    choice = pacman.go()

    if choice == 1 or choice == 3:
        points = pacman.eat_points()
        
        if pacman.point >= 240:
            print('Победа! PacMan съел все 240 точек')
            play = False
        else:
            print(f'Удача! PacMan съел {points}/240 точек\n')
        
    else:
        ghost = random.randint(0,3)
        characters[ghost].print_string()
        pacman.lives-=1

        if pacman.lives == 0:
            print('Игра окончена! Вы проиграли. ')
            print(f'PacMan съел {pacman.point}/240 точек\n')
            play=False
        else:
            print('Минус 1 жизнь')

    sleep(1)
