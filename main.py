# task from https://www.practicepython.org/
import datetime


class User:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def checkingYears(self):
        date = datetime.datetime.now()
        print("{}, you'll have 100 years in {} year".format(self.name, date.year + (100 - self.age)))


class Number:

    def __init__(self, number = 0, lista = []):
        self.number = number
        self.lista = lista

    def __iter__(self):
        return iter(self.lista)

    def __next__(self):
        a = self.lista
        return a

    def even_or_odd(self):
        if self.number % 2 == 0:
            print("{} is even ".format(self.number))
        else:
            print("{} is odd".format(self.number))

    def is_number_divisible(self, divider):
        if self.number % divider == 0:
            print("{} is divisible by {}".format(self.number, divider))
        else:
            print("{} isn't divisible by {}".format(self.number, divider))

    def all_divisors(self):
        list_of_all_divisors = [x for x in range(1, self.number+1) if self.number % x == 0]
        return list_of_all_divisors

    def common_elements_in_lists(self, list1, list2):
        list_of_common_elements = [x for x in list1 if x in list2]
        list_of_common_elements = list(dict.fromkeys(list_of_common_elements))
        return list_of_common_elements








lista = [1, 2, 4, 10, 12, 15]
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

user_one = User(12, "Emil")
number_one = Number(12, lista)

list_less_than_5 = [x for x in number_one if x < 10]
lista2 = number_one.all_divisors()
lista3 = number_one.common_elements_in_lists(a, b)

number_one.even_or_odd()
number_one.is_number_divisible(3)
user_one.checkingYears()

print(list_less_than_5)
print(lista2)
print(lista3)




