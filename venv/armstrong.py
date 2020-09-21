class Armstrong:

    def __init__(self, number):
        self.number = number

    def count_digits(self):
        temp = self.number
        sum_of_numbers = 0
        while temp != 0:
            sum_of_numbers += 1
            temp //= 10
        return sum_of_numbers

    def is_armstrong(self):

        number_copy = self.number
        sum_of_arm_number = 0
        while number_copy != 0:
            remainder = number_copy % 10
            sum_of_arm_number += pow(remainder, Armstrong.count_digits(self))
            number_copy = number_copy // 10
        return print(sum_of_arm_number == self.number)