class Passenger:
    def __init__(self, pid, age, loyalty, has_child=False,
                 prefers=None, paid_seat=None):
        self.pid = pid
        self.age = age
        self.loyalty = loyalty
        self.has_child = has_child
        self.prefers = prefers  
        self.paid_seat = paid_seat

    def __repr__(self):
        return f"P{self.pid}({self.loyalty}, {self.age})"
    
    def __str__(self):
        return f"P{self.pid}({self.loyalty}, {self.age})"
    
    def is_exit_eligible(self):
        return True if self.age in range(20,60) and not self.has_child else False 
    

class Seats:
    def __init__(self,row, col, is_exit=False):
        self.seatid= str(row)+str(col)
        self.row= row
        self.col= col
        self.is_exit=is_exit
        self.passenger=None

    def __repr__(self):
        return f"{self.seatid} -> {self.passenger}"
    
    def __str__(self):
        return self.seatid
    
    def print_seat_detail(self):
        return self.passenger
    
    def is_exit(self):
        return True if self.row in [1,2,10,11,12] else False
    
    