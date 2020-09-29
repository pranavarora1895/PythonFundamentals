class Array:
    def __init__(self, array):
        self.array = array

    def sum_array(self):
        print(sum(self.array))

    def largest_element(self):
        self.array.sort()
        print(self.array[-1])

    def reverse_array(self):
        rev_A = []
        for i in range(1, len(self.array) + 1):
            rev_A.append(self.array[-i])
        print(rev_A)

    def split_array(self):
        for i in range(len(self.array) // 2):
            self.array.insert(len(self.array) + i, self.array[i])

        for i in range(i + 1):
            self.array.remove(self.array[0])
        print(self.array)

