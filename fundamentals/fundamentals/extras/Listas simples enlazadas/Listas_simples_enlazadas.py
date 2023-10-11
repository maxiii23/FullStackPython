class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next     
        return self
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def remove_from_front(self):
        print(f"El valor '{self.head.value}' ha sido eliminado")
        self.head = self.head.next
        return self
    def remove_from_back(self):
        runner = self.head
        loop = 0
        while (runner.next != None):
            loop+=1
            runner = runner.next
        print(f"El valor '{runner.value}' ha sido eliminado")
        runner = self.head
        loopmax = loop - (loop-1)
        while (loop != loopmax):
            loop -=1
            runner = runner.next
        runner.next = None
        return self
    def remove_val(self, val):
        runner = self.head
        loop = 0
        while (runner.value != val):
            loop += 1
            runner = runner.next
        if loop == 0:
            self.remove_from_front()
        loopmax = loop -(loop -1)
        runner = self.head
        while (loop != loopmax):
            loop -=1
            runner = runner.next
        runner.next = runner.next.next
        print(f"El valor '{val}' ha sido eliminado")
        return self
    def insert_at(self, val, n):
        new_node = SLNode(val)
        runner = self.head
        loop = 0
        while (loop != n):
            loop += 1
            runner = runner.next
        if n == 0:
            self.add_to_front(val)
            return self
        new_node.next = runner
        current_head = self.head
        loopmax = loop - (loop-1)
        while(loop != loopmax):
            loop -= 1
            current_head = current_head.next
        current_head.next = new_node
        return self

my_list = SList()
my_list.add_to_front("son").add_to_front("Las listas enlazadas").add_to_back("divertidas!").add_to_back("hola").add_to_back("buenas").add_to_back("tardes").insert_at("noches", 2).print_values()