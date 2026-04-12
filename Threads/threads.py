import threading
import time

def task(name):
    print(f"{name} starting")
    time.sleep(2)
    print(f"{name} done")

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

print("Time:", time.time() - start)