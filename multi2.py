from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue, Pool
import time


def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        # lock.acquire()
        # number.value += 1
        # lock.release()
        with lock:
            number.value += 1
            
        
def add_100_in_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1
  
  
def square(numbers, queue):
    for i in numbers:
        queue.put(i * i)
        

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(i * -1)
        
        
def cube(number):
    return number ** 3
              


if __name__ == "__main__":
    """ 
    lock = Lock()
    # shared_number = Value("i", 0)
    
    # print("Number at beginning is", shared_number.value)

    # p1 = Process(target=add_100, args=(shared_number, lock))
    # p2 = Process(target=add_100, args=(shared_number, lock))
    
    shared_array = Array("d", [0.0, 100.0, 200.0])
    
    print("Array at beginning is", shared_array[:])
    
    p1 = Process(target=add_100_in_array, args=(shared_array, lock))
    p2 = Process(target=add_100_in_array, args=(shared_array, lock))
    
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    # print('number at end is', shared_number.value)
    print("Array at end is", shared_array[:])
     """
     
    """  
    numbers = range(1, 6)
    
    q = Queue()
    
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())
     """    
     
    numbers = range(10)
    pool = Pool()
    
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])
    
    pool.close()
    pool.join()
    
    print(result)