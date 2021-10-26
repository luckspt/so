import time
from multiprocessing import Process, Queue

q = Queue()

def calcTabuada(num):
    tabuada = q.get()
    for i in range(10):
        tabuada[i] = num * (i + 1)
    q.put(tabuada)

def main():
    num = int(input('Insira um numero: '))

    tabuada = [0] * 10
    filho = Process(target=calcTabuada, args=(num,))
    filho.start()

    q.put(tabuada)
    filho.join()
    tabuada = q.get()

    for i in range(10):
        print(f'{num}x{i+1}={tabuada[i]}')

if __name__ == '__main__':
    main()