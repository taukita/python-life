import pickle

inf = float("inf")
class Model:
    def __init__(self):
        self.cells = {}
        self.minX = inf
        self.maxX = -inf
        self.minY = inf
        self.maxY = -inf

    def insert_cell(self, posn):
        if (posn not in self.cells) or (not self.cells[posn][0]):
            x, y = posn
            self.minX = min(x, self.minX)
            self.maxX = max(x, self.maxX)
            self.minY = min(y, self.minY)
            self.maxY = max(y, self.maxY)

            n = 0

            def neighbor(posn):
                if posn in self.cells:
                    c1, c2 = self.cells[posn]
                    self.cells[posn] = (c1, c2 + 1)
                    return int(c1)
                else:
                    self.cells[posn] = (False, 1)
                    return 0

            n += neighbor((x - 1, y - 1))
            n += neighbor((x - 1, y))
            n += neighbor((x - 1, y + 1))
            n += neighbor((x, y - 1))
            n += neighbor((x, y + 1))
            n += neighbor((x + 1, y - 1))
            n += neighbor((x + 1, y))
            n += neighbor((x + 1, y + 1))

            self.cells[posn] = (True, n)

    def delete_cell(self, posn):
        if (posn in self.cells) and (self.cells[posn][0]):
            #тут могут "испортиться" минимумы и максимумы, но мы это игнорируем
            x, y = posn

            def dec_c2(posn):
                c1, c2 = self.cells[posn]
                self.cells[posn] = (c1, c2 - 1)

            dec_c2((x - 1, y - 1))
            dec_c2((x - 1, y))
            dec_c2((x - 1, y + 1))
            dec_c2((x, y - 1))
            dec_c2((x, y + 1))
            dec_c2((x + 1, y - 1))
            dec_c2((x + 1, y))
            dec_c2((x + 1, y + 1))

            self.cells[posn] = (False, self.cells[posn][1])

    def clean(self):
        self.minX = inf
        self.maxX = -inf
        self.minY = inf
        self.maxY = -inf
        new_cells = {}
        for posn in iter(self.cells):
            if self.cells[posn] != (0, 0):
                x, y = posn
                self.minX = min(x, self.minX)
                self.maxX = max(x, self.maxX)
                self.minY = min(y, self.minY)
                self.maxY = max(y, self.maxY)
                new_cells[posn] = self.cells[posn]
        self.cells = new_cells

    def next_gen(self):
        model = Model()
        for posn in iter(self.cells):
            c1, c2 = self.cells[posn]
            if (c2 == 3) or (c1 and c2 == 2):
                model.insert_cell(posn)
        return model

    def save_to_file(self, name):
        file = open(name, 'wb')
        pickle.dump(self, file)
        file.close()

    def load_from_file(name):
        file = open(name, 'rb')
        model = pickle.load(file)
        file.close()
        return model
