from multiprocessing import Process
from threading import Thread
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

#//% PROCESSES
""" processes = []
num_processes = os.cpu_count()
# print(num_processes) # 4

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)
    
#//% start processes
for p in processes:
    p.start()
    
#//% join processes
for p in processes:
    p.join()
    
print("end main") """


#//% THREADS
threads = []
num_threads = 10

# create threads
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)
    
#//% start threads
for t in threads:
    t.start()
    
#//% join threads
for t in threads:
    t.join()
    
print("end main")