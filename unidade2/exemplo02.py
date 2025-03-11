
from mythread import MyThread
thread1 = MyThread('A', 0.8)
thread2 = MyThread('B', 1.5)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('Finalizado.')