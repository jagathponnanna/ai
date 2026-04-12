import random

def categorize_seats(seats):
    categories = {
        "exit": [],
        "window": [],
        "aisle": [],
        "middle": []
    }

    for seat in seats.values():
        if seat.is_exit:
            categories['exit'].append(seat)
        if seat.col in ['A','F']:
            categories["window"].append(seat)
        if seat.col in ['C','D']:
            categories["aisle"].append(seat)
        else:
            categories["middle"].append(seat)
    return categories

def categorize_passengers(passengers):
    categories = {
        "exit_eligible": [],
        "window_pref": [],
        "aisle_pref": [],
        "no_pref": []
    }

    for p in passengers:
        if p.is_exit_eligible():
            categories["exit_eligible"].append(p)
        if p.prefers=="Window":
            categories["window_pref"].append(p)
        elif p.prefers=="Aisle":
            categories["aisle_pref"].append(p)
        else:
            categories["no_pref"].append(p)
    return categories

def assign_random(passenger,seat_list):
    available = [ s for s in seat_list if s.passenger is None]

    if not available:
        return False
    seat=random.choice(available)
    seat.passenger=passenger
    return True

def hybrid_allocate(passengers,seats):
    seat_cat=categorize_seats(seats)
    pass_cat=categorize_passengers(passengers)

    assigned=set()

    for p in passengers:
        if p.paid_seat:
            seat = seats.get(p.paid_seat)

            if seat and seat.passenger is None:
                seat.passenger = p
                assigned.add(p)

    for p in pass_cat["exit_eligible"]:
        if p in assigned:
            continue
        if assign_random(p,seat_cat["exit"]):
            assigned.add(p)
    
    for p in pass_cat["window_pref"]:
        if p in assigned:
            continue
        if assign_random(p,seat_cat["window"]):
            assigned.add(p)

    for p in pass_cat["aisle_pref"]:
        if p in assigned:
            continue
        if assign_random(p,seat_cat["aisle"]):
            assigned.add(p)
    
    for p in passengers:
        if p in assigned:
            continue

        if assign_random(p, list(seats.values())):
            assigned.add(p)
    print("\n--- PAID SEAT CHECK ---")

    wrong_seat=0
    for p in passengers:
        if p.paid_seat:
            assigned_passenger = seats[p.paid_seat].passenger

            if assigned_passenger == p:
                print(f"{p.pid} got {p.paid_seat}")
            else:
                print(f"{p.pid} FAILED for {p.paid_seat} -> got {assigned_passenger}")
                wrong_seat=wrong_seat+1

            print("Total Wrong Seats:",wrong_seat)