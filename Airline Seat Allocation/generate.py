from basics import *
import random
def generate_seats(row=30):
    seats={}

    for row in range(1,row+1):
        for col in ['A','B','C','D','E','F']:
            seat_id=f"{row}{col}"
            seat=Seats(row,col,is_exit=(row in [1,2,10,11,12]))
            seats[seat_id]=seat

    return seats


def generate_passengers(rows=30):
    total=rows*6

    passengers=[]
    temp_seats=generate_seats()
    for i in range (1, total+1):
        age = random.randint(1,80)
        pid = chr(random.randint(65,91))+str(random.randint(1000,9999))
        loyalty= random.choices(["Base","Gold","Silver"],weights=[0.6,0.3,0.1])[0]
        has_child = True if age in range(32,40) and random.randint(0,1) else False
        prefers = random.choice(["Window","Aisle"]) if loyalty !='Base' else None
        paid_seat= random.choice(list(temp_seats.keys())) if random.choice([0,1]) else None
        if paid_seat:
            temp_seats.pop(paid_seat)
        p=Passenger(pid,age,loyalty, has_child, prefers, paid_seat)
        passengers.append(p)

    return passengers

