'''
Espera-se que o valor seja 500, mas por vezes é 499.
Isto deve-se aos processos serem preemptivos e podem ser parados a meio,
    que causa problemas de sincronização pois não se está a fazer uma
    secção crítica
'''
from multiprocessing import Process, Value

cnt = Value("i", 0)
def incrementa():
    cnt.value += 1

def main():
    processos = [ Process(target=incrementa) for _ in range(500) ]
    for processo in processos:
        processo.start()

    for processo in processos:
        processo.join()

    print(f'Fim: {cnt.value}')

if __name__ == '__main__':
    main()
