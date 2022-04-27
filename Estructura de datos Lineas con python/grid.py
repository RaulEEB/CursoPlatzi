from array import Array

class Grid():

    def __init__(self, rows, cols, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(cols, fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col])

            result += " \n "
        
        return str(result)



if __name__ == '__main__':
    matrix = Grid(3,3)
    print(matrix)