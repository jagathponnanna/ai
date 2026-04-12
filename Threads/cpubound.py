import threading
import time

def cpu_task():
    count = 0
    for _ in range(10_000_000):
        count += 1

t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

print("Time:", time.time() - start)