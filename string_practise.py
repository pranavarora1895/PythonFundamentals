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

    def is_substring(self, substring):
        print(substring in self.inp_string)

    def even_char_words(self):
        input_string = self.inp_string
        even_list = []
        even_string = ''
        ls_list = input_string.split(' ')
        for character in ls_list:
            if len(character) % 2 == 0 and not character.isdigit():
                even_list.append(character + ', ')

        join_str = even_string.join(even_list)
        print(f'The words with even number of digits are {join_str}')

    def acceptable_if_vowels(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        present_vowels = []
        inp_vow_list = self.inp_string
        for i in inp_vow_list.lower():
            for j in vowels:
                if j in i:
                    present_vowels.append(j)

        if ('a' and 'e' and 'i' and 'o' and 'u') in present_vowels:

            print("Acceptable")
        else:
            print('Not Acceptable')

    def two_strings_common(self, compared_string):
        inp_str = self.inp_string
        common_letters = []
        for i_term in inp_str.lower():
            for j_term in compared_string.lower():
                if j_term in common_letters or j_term.isspace():
                    continue
                if i_term == j_term:
                    common_letters.append(j_term)
        return common_letters

    def pr_common_char(self, compared_string):
        inp_str = self.inp_string
        common_char = StringPractise.two_strings_common(self, compared_string)
        print(f'The common characters in the strings "{inp_str}" and "{compared_string}" are {common_char}')
        print(f'Number of common characters: {len(common_char)}')

    def vowels_in_string(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        inp_str = self.inp_string
        common_vowels_list = []

        for character in inp_str.lower():
            if character in vowels:
                if character in common_vowels_list:
                    continue
                common_vowels_list.append(character)

        common_vowels_list.sort()
        print(f'The vowels in string "{inp_str}" are {common_vowels_list}')
        print(f'The number of vowels are: {common_vowels_list.__len__()}')

    def rm_duplicate_char(self):
        inp_str = self.inp_string
        unique_string = ''
        copy_string = inp_str
        unique_char = StringPractise.two_strings_common(self, copy_string)
        print(f'The unique string without duplicates is {unique_string.join(unique_char)}')