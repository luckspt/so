import os
from random import sample, randint
from threading import Thread

nums = sample(range(1000), 1000)
x = randint(0, 1000)

res = None

def procura(i):
    global res

    sub = nums[i * 200: (i + 1) * 200]
    for j, v in enumerate(sub):
        if v == x:
            print('Indice: ' + str(j + i * 200))
            res = i + 1

threads = []
for i in range(5):
    threads.append(Thread(target=procura, args=(i,)))
    threads[-1].start()

for i in range(len(threads)):
    threads[i].join()

print('Thread que encontrou: ' + str(res))