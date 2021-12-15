import signal, time, sys
counter = 0
t1 = time.time()

def handler(sig, NULL):
    global counter

    secs = time.time() - t1
    if secs < 10:
        counter += 1

signal.signal(signal.SIGINT, handler)
time.sleep(15)
print(f'Contei {counter} CTRL+Cs')