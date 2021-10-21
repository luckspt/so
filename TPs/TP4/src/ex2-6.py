import os
from random import sample, randint

nums = sample(range(1000), 1000)
x = randint(0, 1000)

def procura():
    sub = nums[i * 200: (i + 1) * 200]
    for j, v in enumerate(sub):
        if v == x:
            print('Indice: ' + str(j + i * 200))
            return i + 1
    return 0

for i in range(5):
    pid = os.fork()
    if pid == 0: #filho
        exit(procura())

res = []
for i in range(5):
    ipid, status = os.wait()
    if os.WIFEXITED(status) and os.WEXITSTATUS(status) != 0:
        res = os.WEXITSTATUS(status)

print('Filho que encontrou: ' + str(res))