from multiprocessing import Process, Array, Semaphore
import random, time

MAX_SIZE = 5
buffer = Array("i",MAX_SIZE)

empty = Semaphore(MAX_SIZE) #Inicialmente, MAX_SIZE posicoes livres
full = Semaphore(0) #Inicialmente, 0 posicoes ocupadas

def produtor():
    inPosition = 0#asd
    while True:
        nextProduced = random.randint(1,100)

        empty.acquire() #Ha’ posicoes livres?
        temp = inPosition % MAX_SIZE
        buffer[temp] = nextProduced
        inPosition += 1
        full.release() #Informo que há nova posicao ocupada

        print ("+++Produzi ", str(nextProduced), " na posicao ", str(temp))
        time.sleep(random.randint(0,3)) #descanso um pouco

def consumidor():
    outPosition = 0
    while True:
        full.acquire() # Ocupo uma posição existente
        temp = outPosition % MAX_SIZE
        valor = buffer[temp]
        outPosition += 1
        empty.release()

        print("---Consumi ", str(valor), " na posicao ", str(temp) )
        time.sleep(random.randint(1,4)) #descanso um pouco

prod = Process(target=produtor)
cons = Process(target=consumidor)
prod.start()
cons.start()
prod.join()
cons.join()