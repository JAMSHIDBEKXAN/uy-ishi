class computer:
    def __init__(self,name,RAM,DISK):
        self.name=name
        self.ram=RAM


class laptop(computer):
    def __init__(self, name, RAM, DISK,price):
        super().__init__(name, RAM, DISK)
        self.price=price



class desktop(computer):
    def __init__(self, name, RAM, DISK,price):
        super().__init__(name, RAM, DISK)
        self.price=price