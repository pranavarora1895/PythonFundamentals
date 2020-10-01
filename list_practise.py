class ListPractise:

    def __init__(self, inp_list):

        self.inp_list = inp_list

    def swap(self,pos1,pos2):
        inp_list_interchange = self.inp_list.copy()
        temp = inp_list_interchange[pos1-1]
        inp_list_interchange[pos1-1] = inp_list_interchange[pos2-1]
        inp_list_interchange[pos2-1] = temp
        print(inp_list_interchange)

    def swap_extremes(self):
        ListPractise.swap(self, pos1=1, pos2=0)

    def rm_n_occurrence(self, word, Nth):
        lisp = self.inp_list
        word_idx = []
        for element in range(0, len(lisp)):
            if lisp[element] == word:
                word_idx.append(element)

        rm_idx = word_idx[Nth - 1]
        lisp.pop(rm_idx)
        print(lisp)

    def n_largest(self,Nth):
        list_copy = self.inp_list.copy()
        list_copy.sort(reverse=True)
        print(f'{Nth} largest number in the list {self.inp_list} is {list_copy[Nth - 1]}')

    def even_odd(self):
        even_list = []
        odd_list = []
        for term in self.inp_list:
            if term % 2 == 0:
                even_list.append(term)
            else:
                odd_list.append(term)
        even_list.sort()
        print(even_list)
        odd_list.sort()
        print(odd_list)


