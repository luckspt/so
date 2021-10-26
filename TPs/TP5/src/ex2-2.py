from multiprocessing import Process, Value

soma = Value("i", 0)

def calcSoma(arr):
    soma.value = sum(arr)

def main():
    numeros = [int(input('Insira um numero: ')) for _ in range(5)]

    filho = Process(target=calcSoma, args=(numeros,))
    filho.start()
    filho.join()

    print(f'Soma: {soma.value}')

if __name__ == '__main__':
    main()