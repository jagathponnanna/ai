from multiprocessing import Process
import time

def cpu_task():
    count = 0
    for _ in range(10_000_000):
        count += 1

p1 = Process(target=cpu_task)
p2 = Process(target=cpu_task)

start = time.time()

p1.start()
p2.start()

p1.join()
p2.join()

print("Time:", time.time() - start)