# задание №1 - ресторанное ПО
class Ingredient:
    def __init__(self, name, value) -> None:
        self.name=name
        self.value=value
    def get_name(self):
        return self.name
    def get_quantity(self):
        return f'{self.value} кг'

class Vegetable(Ingredient):
    def get_name(self):
        return super().get_name()
    def get_quantity(self):
        return super().get_quantity()
    
class Fruit(Ingredient):
    def get_name(self):
        return super().get_name()
    def get_quantity(self):
        return super().get_quantity()
    
carrot = Vegetable('Морковь', 5)
apple = Fruit('Яблоки', 10)

# print(f'{carrot.get_name()} {carrot.get_quantity()}')
# print(f'{apple.get_name()} {apple.get_quantity()}')

# задание №2 - палеонтологи

class Dino:
    def __init__(self, name, breed, height, weight, diet) -> None:
        self.name=name
        self.breed=breed
        self.height=height
        self.weight=weight
        self.diet=diet

    def get_name(self):
        return self.name
    
    def get_breed(self):
        return self.breed
    
    def get_height(self):
        return self.height
    
    def get_weight(self):
        return self.weight
    
    def get_diet(self):
        return self.diet
    
class Carnivore(Dino):
    def __init__(self, name, breed, height, weight) -> None:
        self.diet='Плотоядный'
        super().__init__(name, breed, height, weight, self.diet)
        

class Herbivore(Dino):
    def __init__(self, name, breed, height, weight) -> None:
        self.diet='Травоядный'
        super().__init__(name, breed, height, weight, self.diet)

class DinoPark:
    all_dino = list()
    carnivore_dino = list()
    herbivore_dino = list()

    def add_dino(self, dino: Dino):
        if dino.diet == 'Плотоядный':
            self.carnivore_dino.append(dino)
        elif dino.diet == 'Травоядный':
            self.herbivore_dino.append(dino)
        
        self.all_dino.append(dino)
    
    def list_dino(self):
        return self.all_dino

    def list_herbivore(self):
        return self.herbivore_dino

    def list_carnivore(self):
        return self.carnivore_dino
    
t_rex = Carnivore('Тирранозавр', 'Рекс', 4800, 560)
velociraptor = Carnivore('Велоцираптор', 'Зубастик', 30, 70)
stegosaurus = Herbivore('Стегозавр', 'Стегга', 7100, 420)
triceratops = Herbivore('Трицератопс', 'Трипси', 8000, 290)

park = DinoPark()

park.add_dino(t_rex)
park.add_dino(velociraptor)
park.add_dino(stegosaurus)
park.add_dino(triceratops)


for i in range(len(park.list_dino())):
    print(f'Имя: {park.list_dino()[i].get_name()}\n'
          f'Вид: {park.list_dino()[i].get_breed()}\n'
          f'Вес: {park.list_dino()[i].get_weight()} кг\n'
          f'Рост: {park.list_dino()[i].get_height()} см\n'
          f'Рацион: {park.list_dino()[i].get_diet()}\n')