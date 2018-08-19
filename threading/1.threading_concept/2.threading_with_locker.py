import threading
import datetime
import time

Lock = threading.Lock()

def timer(thread_name, work_duration, repetitions):
    Lock.acquire()
    print(thread_name + " started: " + str(datetime.datetime.now().strftime("%M:%S")))
    while repetitions > 0:
        time.sleep(work_duration)
        print(thread_name + ": " + str(datetime.datetime.now().strftime("%M:%S")))
        repetitions -= 1
    print(thread_name + " is completed: " + str(datetime.datetime.now().strftime("%M:%S")))
    Lock.release()
def Main():
    thread_1 = threading.Thread(target = timer, args=("thread 1", 1, 4))
    thread_2 = threading.Thread(target = timer, args=("thread 2", 2, 2))
    thread_1.start()
    thread_2.start()


if __name__ == '__main__':
    Main()
