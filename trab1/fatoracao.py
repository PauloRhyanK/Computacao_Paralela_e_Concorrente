"""""
Aluno: Paulo Rhyan Kuster
Turma: CC7N

A partir do código "fatoracao.py", trabalhado em laboratório, apresentar as soluções para o problema de fatoração do input proposto:

1. utilizando LIFO para gestão dos números a serem fatorados;

2. utilizando PRIORITY, sendo que o imput_ = [1, 10, 4, 3] deve ter a seguinte ordem de prioridade (2, 3, 0, 1).

"""
# Problema de fatoracao com threads
import queue
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, fila):
        threading.Thread.__init__(self)
        self.name = name
        self.fila = fila        
        
    def run(self):
        print("Iniciando thread %s." % self.name)
        processando_fila(self.fila)
        print("Encerrando thread %s." % self.name)
        
def processando_fila(fila):
    while True:
        try:
            item = fila.get(block=False)
        except queue.Empty:
            return
        else:
            if isinstance(item, tuple):
                _, x = item
            else:
                x = item    
            fatoracao(x)
        time.sleep(1)
        
def fatoracao(x):
    resultado = 'Fatores positivos de %i sao: ' % x
    for i in range(1, x + 1):
        if x % i == 0:
            resultado += str(i) + ' '
    resultado += '\n' + '_' * 30
    print(resultado)
    
# Carregando o manipulador de filas
my_queue = queue.Queue()
my_lifo_queue = queue.LifoQueue()
my_priority_queue = queue.PriorityQueue()
# Determinando valores a serem fatorados
input_ = [1, 10, 4, 3]
priority = [2, 3, 0, 1]

# Inserindo os valores numa fila
for x,p in zip(input_, priority):
    my_queue.put(x)
    my_lifo_queue.put(x)
    my_priority_queue.put((p,x))
    
print("Tamanho Queue: %d" %(my_queue.qsize()))
print("Tamanho LifoQueue: %d" %(my_lifo_queue.qsize()))
print("Tamanho PriorityQueue: %d" %(my_priority_queue.qsize()))

for j in input_:
 fatoracao(j)

# Inicializando 3 threads
thread1 = MyThread('Queue', my_queue)
thread2 = MyThread('LIFO Queue', my_lifo_queue)
thread3 = MyThread('Priority Queue', my_priority_queue)

thread1.start()
thread2.start()
thread3.start()

# Finalizando os 3 threads
thread1.join()
thread2.join()
thread3.join()

print('\n', 'Concluido')