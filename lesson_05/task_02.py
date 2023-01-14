from random import choice


class Field:
    def __init__(self):
        self.field_grid = []
        self.new_grid()
        self.win_positins = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        )

    def new_grid(self):
        self.field_grid = [str(i) for i in range(1, 10)]

    def draw_grid(self):
        grid = self.field_grid

        for i in range(3):
            print(13 * '-')
            print("|", grid[0 + i * 3], "|", grid[1 + i * 3], "|", grid[2 + i * 3], "|")
        else:
            print(13 * '-')

    def make_move(self, side, coordinate):
        self.field_grid[coordinate] = side

    def get_winpositions(self):
        return self.win_positins

    def get_capacity(self):
        return list(filter(lambda x: x.isdigit(), self.field_grid))

    def get_grid(self):
        return self.field_grid


class Bot:
    def __init__(self, name):
        self.name = name
        self.side = None

    def assign_side(self, side):
        if side not in ('X', 'O'):
            return False
        self.side = side

    def toss(self, grid):
        coordinate = self.choosing_move(grid)

        if not coordinate:
            probality = grid.get_capacity()
            coordinate = int(choice(probality)) - 1

        grid.make_move(self.side, coordinate)

    def choosing_move(self, grid):
        possibility = self.current_status_analysis(grid)

        if possibility['win']:
            return possibility['win'][0]

        if possibility['danger']:
            return possibility['danger'][0]

        if possibility['winline'] and possibility['attack']:
            for i in possibility['winline']:
                if i in possibility['attack']:
                    return i

        if possibility['winline']:
            return choice(possibility['winline'])
        elif possibility['attack']:
            return choice(possibility['attack'])
        else:
            return False

    def current_status_analysis(self, grid):
        win_positions = grid.get_winpositions()
        current_status = grid.get_grid()

        possibility = {
            'danger': [],
            'winline': [],
            'win': [],
            'attack': []
        }

        for i in win_positions:
            my_side = 0
            opponent = 0
            digit = []

            for j in i:
                value = current_status[j]
                if value.isdigit():
                    digit.append(int(value) - 1)
                elif value == self.side:
                    my_side += 1
                else:
                    opponent += 1

            if my_side == 2 and opponent == 0:
                possibility['win'].append(digit[0])
            elif my_side == 0 and opponent == 2:
                possibility['danger'].append(digit[0])
            elif my_side == 1 and opponent == 0:
                possibility['winline'] += digit
            elif my_side == 0 and opponent == 1:
                possibility['attack'] += digit

        return possibility


class Game:
    def __init__(self, field, X, O, draw_process=False):
        self.field = field
        self.X = X
        self.O = O
        self.current_side = False
        self.draw_process = draw_process

        X.assign_side('X')
        O.assign_side('O')

    def start(self):
        self.field.new_grid()
        self.current_side = False

        self.party()

    def party(self):
        decision = None
        while decision is None:
            self.current_side = not self.current_side

            if self.draw_process:
                self.field.draw_grid()

            if self.current_side:
                self.X.toss(self.field)
            else:
                self.O.toss(self.field)

            decision = self.refery()

        self.field.draw_grid()

        if decision != 'победа':
            print('Ничья')
        else:
            winner = 'X' if self.current_side else 'O'
            print(f'Победил {winner}')

    def refery(self):
        field = self.field.get_grid()
        for i in self.field.get_winpositions():
            pos_1 = field[i[0]]
            pos_2 = field[i[1]]
            pos_3 = field[i[2]]

            if pos_1 == pos_2 == pos_3:
                return 'победа'

        if len(self.field.get_capacity()) == 0:
            return 'ничья'
        else:
            return None


fld = Field()

bot_1 = Bot('Васька')
bot_2 = Bot('Мурка')

gm = Game(fld, bot_1, bot_2, False)
gm.start()

