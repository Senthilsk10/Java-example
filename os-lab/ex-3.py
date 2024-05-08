import threading
import time

CAPACITY = 10
buffer = [-1 for _ in range(CAPACITY)]
in_index = 0
out_index = 0
p = int(input("Enter the number of producers: "))
c = int(input("Enter the number of consumers: "))

# Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)

class Producer(threading.Thread):
    def run(self):
        global CAPACITY, buffer, in_index, out_index
        global mutex, empty, full
        items_produced = 0
        while items_produced < p:
            empty.acquire()
            mutex.acquire()
            counter = buffer[in_index]
            in_index = (in_index + 1) % CAPACITY
            print("Producer produced : ", counter)
            mutex.release()
            full.release()
            time.sleep(1)
            items_produced += 1

class Consumer(threading.Thread):
    def run(self):
        global CAPACITY, buffer, in_index, out_index
        global mutex, empty, full
        items_consumed = 0
        while items_consumed < c:
            full.acquire()
            mutex.acquire()
            item = buffer[out_index]
            out_index = (out_index + 1) % CAPACITY
            print("Consumer consumed item : ", item)
            mutex.release()
            empty.release()
            time.sleep(2.5)
            items_consumed += 1

# Creating Threads
producer = Producer()
consumer = Consumer()

# Starting Threads
consumer.start()
producer.start()

# Waiting for threads to complete
producer.join()
consumer.join()
