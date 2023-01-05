import random


class Ship:
    ship = [[0, 0], [0, 1], [0, 2], [0, 3]]

    def create_ship(self):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        d = random.randint(0, 1)
        if d == 0:
            self.ship = [[x, y], [x, y + 1], [x, y + 2], [x, y + 3]]
        else:
            self.ship = [[x, y], [x + 1, y], [x + 2, y], [x + 3, y]]


class Board(Ship):
    matrix = [["~" for _ in range(11)] for _ in range(11)]
    alphabet_line = ["A", "B", "C", "D", "I", "F", "G", "H", "I", "J"]
    number_line = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def place_boats(self):
        pass

    def draw_board(self):
        for i in range(len(self.number_line)):
            self.matrix[0][0] = ""
            self.matrix[0][i + 1] = self.alphabet_line[i]
            self.matrix[i + 1][0] = str(self.number_line[i])

        for i in range(len(self.matrix)):
            for k in range(len(self.matrix)):
                print("{:^3}".format(self.matrix[i][k]), end='')
            print()


ship = Ship()
ship.create_ship()
draw = Board()
draw.place_boats()
draw.draw_board()
