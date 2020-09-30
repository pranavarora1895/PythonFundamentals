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

