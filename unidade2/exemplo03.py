import threading

def function(i):
    print("Função chamada pelo thread %i \n" % i)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=function(i), args=())
    threads.append(t)   
    t.start
    t.join


    