#!python2
# Tui Popenoe
# Challenge184E - Smart Stack List

class SmartStackList():
    def __init__(self):
        self.sorted_list = []
        self.stack_list = []

    def push(element):
        self.stack_list.append(element)
        self.sorted_list = sorted(self.stack_list)

    def pop():
        del self.stack_list[-1]
        self.sorted_list =  self.stack_list

    def size():
        return len(self.stack_list)

    def remove_greater(element):
        try:
            i = self.sorted_list.index(element)
            remove_list = self.sorted_list[i:]
            del self.sorted_list[i:]
        except:
            for i in range(len(self.sorted_list)):
                if self.sorted_list[i] > element:
                    remove_list = self.sorted_list[i:]
                    del self.sorted_list[i:]
        for i in remove_list:
            self.stack_list.remove(i)


    def display_stack():
        print(self.stack_list)

    def display_ordered():
        print(self.sorted_list)