def main():
    numeros = [int(input('Insira um numero: ')) for _ in range(5)]
    soma = sum(numeros)
    print(f'Soma: {soma}')

if __name__ == '__main__':
    main()