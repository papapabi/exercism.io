class Matrix(object):
    def __init__(self, matrix_string):
        rows = []
        for line in matrix_string.split('\n'):
            row = [int(num) for num in line.split()]
            rows.append(row)
        columns = [list(column) for column in zip(*rows)]
        self.rows = rows
        self.columns = columns

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return self.columns[index]
