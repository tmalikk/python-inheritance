class A():
    def __init__(self):
        print('A class has been called')


class B():
    def __init__(self):
        print('B class has been called')


class C( A, B ):
    def __init__(self):
        super().__init__()
        print('C class has been called')


c_object = C()