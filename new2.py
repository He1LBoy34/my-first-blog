class Animal:
    def __init__(self, age=0, weight=0, length=5):
        self.age = age
        self.weight = weight
        self.length = length
        self.hungry = 0
        self.speech = ""

    def eat(self):
        self.hungry += 1

    def get_eat(self):
        print(self.hungry)

    def show_age(self):
        print(self.age)

    def show_weight(self):
        print(self.weight)

    def show_length(self):
        print(self.length)

    def get_speech(self):
        print(self.speech)

    def set_speech(self, speech):
        self.speech = speech


class Tail():
    def __init__(self, length=10, diametr=3, fluffiness=True):
        self.length = length
        self.diametr = diametr
        self.fluffiness = fluffiness


class Cat(Animal, Tail):
    def __init__(self):
        super(Cat, self).__init__()
        self.speech = "Meow, meow!"
        super(Animal, self).__init__()


    #def __init_subclass__(Animal, self):
        #super().__init__()


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.speech = "Wow, wow!"
        self.tail = Tail()








# dog1 = Dog()
# dog1.get_speech()
# # print(dog1.age)
# print(dog1.tail.diametr)

#
cat1 = Cat()
print(cat1.diametr)
print(cat1.age)

# cat1.show_age()
# cat1.get_speech()
# cat1.set_speech("May")
# cat1.get_speech()
# cat1.age = 5
# cat1.show_age()

class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")

class D:
    def __init__(self):
        print("D")


class C(A, B, D):
    def __init__(self):
        super().__init__()
        print("C")
        super(A, self).__init__()
        super(B, self).__init__()



test = C()