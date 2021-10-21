import os, sys
from multiprocessing import Process
sum=0

def calc_sum(num):
    global sum
    for i in range(num+1):
        sum += i
        print ("soma na funcao: ", str(sum))

n=5
try:
    thread = Process(target=calc_sum, args=(n,))
    thread.start()
    thread.join()

    print ("PID = ", str(os.getpid()), ". Soma = ", str(sum))
except OSError as e:
    print >>sys.stderr, "fork failed ", e.errno, "-", e.strerror
    sys.exit(1)