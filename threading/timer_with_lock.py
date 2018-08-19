import threading
import time

lock = threading.Lock()

def timer(name, delay, repeat):
    print("Timer: " + name + " started")
    lock.acquire()
    print(name + " has acquired the lock")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print(name + " is releasing the lock")
    lock.release()
    print("Timer: " + name + " is completed")

def Main():
    t1 = threading.Thread(target = timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target = timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()

if __name__ == '__main__':
    Main()
