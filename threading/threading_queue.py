import threading
from queue import Queue
import time

#lock the print function so it can'tm be used by more than one thread at the same time
#are used to lock the other threads from stepping on each other while printing. Meaning -
#if thread #9 is now printing, all the other threads that currently arrived at this command have to wait until it finishes.
print_lock = threading.Lock()

#job definition
def exampleJob(job_id):
    time.sleep(1)
    #access the print function only if it is not used by other threads
    with print_lock:
        #print thread doing the job and the job_id
        print(threading.current_thread().name, job_id)

#core functionality
def threader():
    while True:
        #get the job_id from the queue
        job_id = q.get()
        #do the job
        exampleJob(job_id)
        #job done, release thread
        q.task_done()

#initialize the queue that will handle all the jobs
q = Queue()

#initialize the threads
#5 threads will simultaneously run the threader command
for x in range(5):
    #threads initialized to execute threader command
    t = threading.Thread(target = threader)
    #defining the thread as a daemon, meaning it is not the main thread
    t.daemon = True
    t.start()

#start time for performance measurements
start = time.time()

#put jobs to be done in the queue so they can be done by the threads
for job_id in range(5):
    q.put(job_id)

#wait until threads have done all jobs in the queue, then execute what's beneath .join()
q.join()
#print results
print ('Done in: ' + str(time.time() - start) + ' seconds')
