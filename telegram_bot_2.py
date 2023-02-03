class Person:
    def __init__(self,name,rost:int,color):
        self.name=name
        self.rost = rost
        self.color = color
        self.weight = None
    def say_hello(self):
        print(f'Меня зовут {self.name} мой рост {self.rost}')

ivan = Person("Ivan",190,"brown")
ivan.say_hello()
vasya = Person("Vasya",180,"green")

vasya.say_hello()