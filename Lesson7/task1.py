class Matrix:
    list_1: list
    list_2: list

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        new_matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for x in range(len(self.list_2[i])):
                new_matrix[i][x] = self.list_1[i][x] + self.list_2[i][x]

        return str('\n'.join(['\t'.join([str(x) for x in i]) for i in new_matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(x) for x in i]) for i in new_matrix]))


my_matrix = Matrix([[5, 8, 11],
                    [7, 10, 3],
                    [4, 15, 9]],
                   [[14, 6, 2],
                    [16, 17, 23],
                    [20, 11, 7]])

print(my_matrix.__add__())
