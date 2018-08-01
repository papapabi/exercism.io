class Matrix(object):
    def __init__(self, matrix_string):
        rows = [[int(num) for num in row.split()] for row in
                matrix_string.split('\n')]
        columns = [list(column) for column in zip(*rows)]
        self.rows = rows
        self.columns = columns

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return self.columns[index]
