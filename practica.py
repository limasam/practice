# Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

# def card_number(card):
#     return '*' * len(card[:-4]) + card[-4:]
#
# print(card_number('1234567890123456'))




# Напишите функцию, которая проверяет: является ли слово палиндромом
# a = input('Введите слово: ')
# def palindrome(a):
#     return a[::-1] == a
# if palindrome(a) is True:
#     print(a, ' is a palindrome')
# else:
#     print(a, 'not a palindrome')



# Решите задачу
class Tomato:
    # Стадии созревания помидора
    states = {1 : 'Отсутствует', 2 : 'Цветение', 3 : 'Зеленый помидор', 4 : 'Красный помидор'}

    def __init__(self, index):
        self._index = index
        self._state = 1

    # Переводит томат на следующую стадию созревания
    def grow(self):
        if self._state < 4:
            self._state += 1
            print('Томат', self._index, 'на стадии', Tomato.states[self._state])


    # Проверяет созрел ли томат
    def is_ripe(self):
        if self._state == 4:
            return True
        return False


class TomatoBush:

    # Список из объектов класса Tomato
    def __init__(self, a):
        self.tomatoes = [Tomato(index) for index in range (0, a)]

    # Переводим томаты на следующий уровень
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем все ли томаты созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Чистим список после сбора урожая
    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Выращиваем растение
    def work(self):
        print('Идет работа ...')
        self._plant.grow_all()
        print('Работа закончена')

    # Проверяем все ли созрело
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print('Цветы еще не выросли')


    @staticmethod
    def knowledge_base():
        print('Хочется, чтобы все и сразу. Сегодня была только трава по пояс — а через неделю уже терем стоит, '
              'по озеру уточки плавают, на ветвях яблочки наливаются… Сказка, ага.')


# Тесты
Gardener.knowledge_base()
tomato_bush_1 = TomatoBush(4)
gardener_1 = Gardener('lilia', tomato_bush_1)
gardener_1.work()
gardener_1.work()
gardener_1.harvest()
gardener_1.work()
gardener_1.harvest()