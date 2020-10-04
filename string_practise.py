class StringPractise:
    def __init__(self, inp_string):
        self.inp_string = inp_string

    def reversal_algo(self):
        inp_str = self.inp_string
        reversal_string = ''
        for character in range(len(inp_str)):
            reversal_string += inp_str[len(inp_str) - (1 + character)]
        return reversal_string

    def reverse_string(self):
        print(StringPractise.reversal_algo(self))

    def is_palindrome(self):
        in_str = self.inp_string
        print(in_str == StringPractise.reversal_algo(self))

    def rm_character(self, char_idx):
        given_string = self.inp_string
        new_String = ''
        Str_list = []
        for character in given_string:
            Str_list.append(character)
        Str_list.pop(char_idx - 1)

        print(new_String.join(Str_list))
