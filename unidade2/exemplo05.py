import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def print_time(self, threadName, delay, counter):
        start = time.time()
        while counter:
            countertime = time.time()
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            
            print("%s: %.2f Sec" % (threadName, time.time() - countertime))
            counter -= 1
        print("Total time %s: %.2f Sec" % (threadName, time.time() - start))
        
    def run(self):
        print("Iniciando " + self.name)
        self.print_time(self.name, self.counter, 5)
        print("Finalizando " + self.name)


# Create new threads
thread1 = myThread(1, "Thread-1", 1)    
thread2 = myThread(2, "Thread-2", 2)    
thread3 = myThread(3, "Thread-3", 5)    

#Start new threads
thread1.start()
thread3.start()
thread2.start()
print("Saindo do Thread Principal!")