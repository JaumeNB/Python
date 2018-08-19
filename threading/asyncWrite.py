import threading
import time

class asyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run (self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print("Finished background file write to " + self.out)

def Main():
    message = input("Enter a string to store: ")

    for i in range(1):
      t = asyncWrite(str(message), 'out.txt')
      t.start()

    print("The program can continue while it writes in another thread")
    print ("100 + 400 = ", 100 + 400)

    for i in range(1):
      t = asyncWrite(str(message), 'out.txt')
      t.start()

    threads = threading.enumerate()

    for thread in threads:
        string_thread = str(thread)
        thread_separated = string_thread.split('(')
        print thread_separated[0][1:]


    print (threading.active_count())

    t.join()
    print("Waited until thread was completed")

    print (threading.active_count())


if __name__ == '__main__':
    Main()
