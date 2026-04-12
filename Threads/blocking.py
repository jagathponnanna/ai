import time

def fetch(name):
    print(f"Fetching {name}")
    time.sleep(2)
    print(f"Done {name}")
    return name

start = time.time()

fetch("A")
fetch("B")
fetch("C")

print("Time:", time.time() - start)