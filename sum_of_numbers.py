class Sum:
    def __init__(self, n):
        self.n = n

    def squares(self):
        sum_of_squares = (self.n * (self.n + 1) * (2 * self.n + 1)) / 6
        print(sum_of_squares)

    def cubes(self):
        sum_of_cubes = pow((self.n * (self.n + 1)) / 2, 2)
        print(sum_of_cubes)
