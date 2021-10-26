from multiprocessing import Process, Array

tabuada = Array("i", 10)

def calcTabuada(num):
    for i in range(10):
        tabuada[i] = num * (i + 1)

def main():
    num = int(input('Insira um numero: '))

    filho = Process(target=calcTabuada, args=(num,))
    filho.start()
    filho.join()

    for i in range(10):
        print(f'{num}x{i+1}={tabuada[i]}')

if __name__ == '__main__':
    main()