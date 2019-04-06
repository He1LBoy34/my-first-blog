# var1 = None
# var2 = True
# var3 = 3
# var4 = 3.0
# var5 = [1, 2.0, 'Hello']
# var6 = {1, 2, 3}
# var7 = 'Hello world'
# var8 = {'a': 1, 'b': 2}
# var9 = (1, 2, 3)
# var10 = list(range(5))
# var11 = tuple()
# var12 = dict()
# var13 = int()
# x = 100
# while x < 100:
#     print(x)
#     x =+ 1
#     if x == 50:
#         break
#     elif x < 100:
#         print()
#     if x == 40:
#         continue
#     else:
#         pass
#
# for i in var5:
#     print(i)


# def summ(a, b):
#     c = a + b
#     return c


# def func(**kwargs):
#     return kwargs
#
#
# s = func(a=5)
# print(type(s))


class Cat:
    def __init__(self, age=0):
        self.age = age

    def meow(self):
        print("Meow, meow")

    def get_age(self):
        print(self.age)

    def set_age(self, age):
        self.age = age


cat1 = Cat(10)
cat1.meow()
cat1.get_age()
cat1.set_age(2)
cat1.get_age()

