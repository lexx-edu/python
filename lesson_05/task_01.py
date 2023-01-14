from random import randint


class Table:
    def __init__(self, limit=1000, take_max=28):
        self.capacity = 0
        self.limit = limit
        self.take_max = take_max

    def loading(self):
        self.capacity = randint(self.take_max + 1, self.limit)

    def give_away_candy(self, candy_qty):
        if candy_qty > self.take_max or candy_qty > self.capacity:
            return False

        self.capacity -= candy_qty
        return candy_qty

    def __str__(self):
        return f'Остаток конфет на столе: {self.capacity}, брать можно не больше {self.take_max}.'


class Bot:
    def __init__(self, name):
        self.name = name
        self.log = 0

    def toss(self, table, oponent_log):
        if table.capacity <= table.take_max:
            toss_result = table.capacity
        elif oponent_log == 0:
            toss_result = table.capacity % (table.take_max + 1)
        else:
            toss_result = table.take_max + 1 - oponent_log

        self.log = toss_result
        table.give_away_candy(self.log)
        print(self.name, f'взял {self.log} конфет')


class Human(Bot):
    def __init__(self, name):
        Bot.__init__(self, name)

    def toss(self, table, oponent_log):
        toss_result = False

        while not toss_result:
            give_candy = int(input((f'{self.name}, введите количество конфет: ')))
            toss_result = table.give_away_candy(give_candy)

        self.log = toss_result
        print(self.name, f'взял {self.log} конфет')

class Game:
    def __init__(self, table, *, first, second):
        self.table = table
        self.first = first
        self.second = second
        self.first_move = self.coin_toss()
        self.toss_first = False

    def start(self):
        self.table.loading()
        self.first_move = self.coin_toss()
        self.first.log = 0
        self.second.log = 0
        self.toss_first = bool(self.first_move - 1)

        self.party()

    def coin_toss(self):
        return randint(0, 1) + 1

    def message(self, gamer, opponent):
        print(
            f'Ходит {gamer.name}. Опонент за прошлый ход забрал {opponent.log} конфет')

    def party(self):
        while self.table.capacity > 0:
            print(f'\n{self.table}')
            if self.toss_first:
                self.message(self.first, self.second)
                self.first.toss(self.table, self.second.log)
            else:
                self.message(self.second, self.first)
                self.second.toss(self.table, self.first.log)

            self.toss_first = not self.toss_first

        winner = self.first.name if self.toss_first else self.second.name
        print(f'\n\nПобедил {winner}!')



tb = Table()
bot = Bot('Вова')

# human = Human('Паша')
# gm = Game(tb, first=bot, second=human)

bot_oponent = Bot('Паша')
gm = Game(tb, first=bot, second=bot_oponent)

gm.start()