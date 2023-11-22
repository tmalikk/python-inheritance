class GrandParent():
    gp = 0
    def __init__(self) -> None:
        print('This is Grand Parent or top Class')
        self.gp = int(input('Enter Value for gp: '))


class Parent(GrandParent):
    p = 0

    def __init__(self) -> None:
        super().__init__()
        print('This is Parent or intermediate Class')
        self.p = int(input('Enter value for p: '))


class Child(Parent):
    c = 0

    def __init__(self) -> None:
        super().__init__()
        print('This is Child or Lower Class')
        self.c = int(input('Enter value for c: '))
    
    def sum(self):
        result = self.gp + self.p + self.c
        print(result)

child = Child()
child.sum()