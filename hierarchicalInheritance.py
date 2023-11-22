class Animal():
    def __init__(self):
        print('Im an animal')
    
    def legs(self):
        print('I have four legs')


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('Im a dog')
    
    def bark(self):
        print('I can bark\n')


class Cat(Animal):
    def __init__(self):
        super().__init__()
        print('Im a cat')
    
    def meow(self):
        print('I can meow\n')


# anim = Animal()
dog = Dog()

dog.legs()
dog.bark()

cat = Cat()
cat.legs()
cat.meow()