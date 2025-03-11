import threading
import time

def primeira_func():
    print(threading.current_thread().name + str(' Esta inicinado \n'))
    
    time.sleep(5)
    print(threading.current_thread().name + str( 'Está finalizando \n'))
    
def segunda_func():
    print(threading.current_thread().name + str(' Esta inicinado \n'))
    
    time.sleep(5)
    print(threading.current_thread().name + str( 'Está finalizando \n'))
    
def terceira_func():
    print(threading.current_thread().name + str(' Esta inicinado \n'))
    
    time.sleep(5)
    print(threading.current_thread().name + str( 'Está finalizando \n'))
    

if __name__ == "__main__":
    t1 = threading.Thread(name='primeira_funcao', target=primeira_func)
    t2 = threading.Thread(name='segunda_funcao', target=segunda_func)
    t3 = threading.Thread(name='terceira_funcao', target=terceira_func)
    
    t1.start()
    t2.start()
    t3.start()