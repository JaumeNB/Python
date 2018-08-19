import threading
from Queue import Queue
import time

counter = 0
q = Queue()
Lock = threading.Lock()

def do_job(turn):
    global counter
    time.sleep(1)
    with Lock:
        counter += 1
        print(str(threading.current_thread().name) + " took turn n." + str(turn) + " - counter: " + str(counter))

def take_job_from_queue():
    while True:
        job_id = q.get()
        do_job(job_id)
        q.task_done()

for i in range(10):
    t = threading.Thread(target = take_job_from_queue)
    t.daemon = True
    t.start()

start = time.time()

for job in range(100):
    q.put(job)

q.join()
print ('Counter increased to ' + str(counter) + ' in: ' + str(time.time() - start) + ' seconds')
