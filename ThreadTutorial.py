import threading
import time
import queue

# Número de threadings ativas no programa
threading.activeCount()

# Numero de objetos thread no controle thread atual do chamador
threading.current_thread()

# Lista dos objetos threading ativos no programa
threading.enumerate()

# O objeto Thread contém os seguintes itens
object = threading.Thread(target=function, args=(i,))

# Método chamado quando uma thread é iniciada e disparada ao processador
object.run()

# Isso é o que inicia a Thread, invocando o run()
object.start()

# Este método aguarda o término do objeto thread antes de continuar a executar o restante do programa
object.join()

# Este método retorna um valor booleano, dizendo do se o objeto theread está em execução no momento
object.is_alive()

# Este método retorna o nome do objeto thread
object.name()

# Este método define o nome do objeto thread
object.setName()

# Thread podem ser compostas principalmente po, contador de programa, registradores e Pilha

# Elas tem basicamente três estados, pronto, em execução e bloqueado



##################################
######## O MODULO QUEQUE #########
#################################

# QUEUE          - tipo FIFO, primeiro a entrar, primeiro a sair
# LIFOQUEUE      - tipo LIFO, ultimo a entrar, primeiro a sair
# PRIORITY QUEUE - tipo ordem de prioridade, o com mais prioridade sai primeiro 

###  Mètodos  ###

# get()   = este método retorna o proximo elemento do objeto da fila e o remove do mesmo
# put()   = este método adiciona um novo element ao objeto da fila
# qsize() = este método retorna o número de elementos atuais no objeto da fila de chamada (o seu tamanho)
# empty() = booleano, dizendo se a fila está vazia
# full()  = booleano, dizendo se a fila está cheia


fila_fifo = queue.Queue()
fila_lifo = queue.LifoQueue()
fila_priority = queue.PriorityQueue()

# Exemplo de FIFO
fila_fifo = queue.Queue()
fila_fifo.put("Primeiro da fila")
fila_fifo.put("Segundo da fila")
print(fila_fifo.get())
# Saida sera: Primeiro da fila
# Exemplo de LIFO
fila_fifo = queue.LifoQueue()
fila_fifo.put("Primeiro da fila")
fila_fifo.put("Segundo da fila")
print(fila_fifo.get())
# Saida sera: Segundo da fila
# Exemplo de PriorityQueue
fila_priority = queue.PriorityQueue()
fila_priority.put((2, "Primeiro da fila"))
fila_priority.put((1, "Segundo da fila"))
print(fila_priority.get())
# Saida sera: (1, 'Segundo da fila')