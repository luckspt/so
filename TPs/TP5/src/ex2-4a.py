from multiprocessing import Process, Pipe

pipePai, pipeFilho = Pipe()

def calcTabuada(num):
    tabuada = pipeFilho.recv()
    for i in range(10):
        tabuada[i] = num * (i + 1)
    pipeFilho.send(tabuada)

def main():
    num = int(input('Insira um numero: '))

    tabuada = [0] * 10
    filho = Process(target=calcTabuada, args=(num,))
    filho.start()

    pipePai.send(tabuada)
    tabuada = pipePai.recv()

    for i in range(10):
        print(f'{num}x{i+1}={tabuada[i]}')

if __name__ == '__main__':
    main()