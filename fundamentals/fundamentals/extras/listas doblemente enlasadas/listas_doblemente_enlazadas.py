class DNode():
    def __init__(self,val):
        self.value = val
        self.next = None
        self.before = None

class DList():
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = DNode(val)
        current_head = self.head
        new_node.next = current_head
        if current_head != None:
            current_head.before = new_node
        self.head = new_node
        return self
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = DNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        new_node.before = runner
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next     
        return self
    def add_next_to_id(self, val, id):
        new_node = DNode(val)
        runner = self.head
        loop = 0
        while (loop != id):
            loop += 1
            runner = runner.next
        if runner.next == None:
            self.add_to_back(val)
            return self
        newloop = loop + 1
        current_head = self.head
        while (newloop != 0):
            newloop -=1
            current_head = current_head.next
        runner.next = new_node
        new_node.next = current_head
        current_head.before = new_node
        new_node.before = runner
        return self
    def add_before_to_id(self,val,id):
        new_node = DNode(val)
        runner = self.head
        loop = 0
        while (loop != id):
            loop += 1
            runner = runner.next
        if runner.before == None:
            self.add_to_front(val)
            return self
        current_head = self.head
        newloop = loop - 1
        while (newloop != 0):
            newloop -=1
            current_head = current_head.next
        runner.before = new_node
        new_node.next = runner
        current_head.next = new_node
        new_node.before = current_head
        return self
    def remove_from_front(self):
        print(f"El valor '{self.head.value}' ha sido eliminado")
        self.head = self.head.next
        self.head.before = None
        return self
    def remove_from_back(self):
        runner = self.head
        loop = 0
        while (runner.next != None):
            loop += 1
            runner = runner.next
        print(f"El valor '{runner.value}' ha sido eliminado")
        runner.before = None
        runner = self.head
        maxloop = loop - 1
        while maxloop != 0:
            maxloop-=1
            runner = runner.next
        runner.next = None
        return self
    def remove_from_id(self,id):
        afterrunner = self.head
        loop = 0
        while loop != id +1:
            loop +=1
            afterrunner = afterrunner.next
        if afterrunner == None:
            self.remove_from_back()
            return self
        beforerunner = self.head
        loop = 0
        while loop != id -1:
            loop +=1
            beforerunner = beforerunner.next
        if beforerunner == None:
            self.remove_from_front()
            return self
        afterrunner.before = beforerunner
        beforerunner.next = afterrunner
        return self

my_list = DList();
my_list.add_to_front("son").add_to_back(8).add_next_to_id("geniales", 0).add_to_front("las listas").add_before_to_id("jaja", 3).remove_from_front().remove_from_back().remove_from_id(1).print_values()

