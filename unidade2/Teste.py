import time

print(time.time())
print(time.ctime(time.time()))


agora = time.time()
time.sleep(5)
agora2 = time.time() - agora
print(agora2)