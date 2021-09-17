import math


class Rocket:

    def __init__(self, x_pos=0, y_pos=0, height=200, crew_size=10, color='blue', owner='Littell', r_class='Exploration', name='Serenity'):
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.crew_size = crew_size
        self.owner = owner
        self.r_class = r_class
        self.name = name

    def move_rocket(self):
        self.x_pos += 10
        self.y_pos += 30

    def get_distance(self, o_rocket):
        x_1 = self.x_pos
        y_1 = self.y_pos
        x_2 = o_rocket.x_pos
        y_2 = o_rocket.y_pos
        dis = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
        return dis

    def launch(self):
        print(f'The rocket {self.name} has taken off!')

    def land(self):
        print(self.x_pos, self.y_pos)
        print('The rocket has Landed.')
        self.x_pos = 0
        self.x_pos = 0
        print(self.x_pos, self.y_pos)

    def safety_check(self, rocket_):
        check = self.get_distance(rocket_)
        if check >= 10:
            print('The distance is good, you are safe')
        elif check == 0:
            print('The rockets have crashed')
        else:
            print('You are to close move away')


rocket1 = Rocket(10, 30)
rocket2 = Rocket()

for i in range(5):
    print(rocket1.x_pos)
    print(rocket1.y_pos)
    rocket1.move_rocket()

rockets_group = []
for u in range(10):
    rocket = Rocket(50, 40)
    rockets_group.append(rocket)
rockets_group[2].move_rocket()
rockets_group[2].move_rocket()
rockets_group[0].move_rocket()
for i in range(len(rockets_group)):
    print(rockets_group[i].x_pos, rockets_group[i].y_pos)
rocket1.get_distance(rocket2)
rockets_group[2].get_distance(rockets_group[0])
rockets_group[2].get_distance(rockets_group[7])

rocket1.safety_check(rocket2)


class Person:

    def __init__(self, name, age, height, weight, birth_place, birthday):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.birth_place = birth_place
        self.birthday = birthday

    def introduction(self):
        print(f'Hello my name is {self.name} and I am {self.age} years old. I was born on {self.birthday} in {self.birth_place} and I am {self.height} and weigh {self.weight} pounds.')


person1 = Person('John Doe', 17, '6 feet 3 inches', 190, 'Portland Maine', 'September 3, 2004')
person1.introduction()


class Car:

    def __init__(self, make, model, year, owner, doors, capacity):
        self.make = make
        self.model = model
        self.year = year
        self.owner = owner
        self.doors = doors
        self.capacity = capacity

    def description(self):
        print(f'The car is a {self.year} {self.make} {self.model}, it has {self.doors} doors and can fit {self.capacity} people, the car is owned by {self.owner}.')


car1 = Car('Toyota', 'Siena', 2004, 'John Doe', 4, 8)
car1.description()
car2 = Car('Lamborghini', 'Sian', 2020, 'Ben Littell', 2, 2)
car2.description()
