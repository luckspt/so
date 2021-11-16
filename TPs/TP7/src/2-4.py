from multiprocessing import Process, Array, Semaphore, Value
import random, time

MAX_SIZE = 5
buffer = Array("i",MAX_SIZE)

empty = Semaphore(MAX_SIZE) #Inicialmente, MAX_SIZE posicoes livres
full = Semaphore(0) #Inicialmente, 0 posicoes ocupadas

posProdutor = Value("i", 0)
posConsumidor = Value("i", 0)

def produtor():
    while True:
        nextProduced = random.randint(1,100)

        empty.acquire() #Ha’ posicoes livres?
        temp = posProdutor.value % MAX_SIZE
        buffer[temp] = nextProduced
        posProdutor.value += 1
        full.release() #Informo que há nova posicao ocupada

        print ("+++Produzi ", str(nextProduced), " na posicao ", str(temp))
        time.sleep(random.randint(0,3)) #descanso um pouco

def consumidor():
    while True:
        full.acquire() # Ocupo uma posição existente
        temp = posConsumidor.value % MAX_SIZE
        valor = buffer[temp]
        posConsumidor.value += 1
        empty.release()

        print("---Consumi ", str(valor), " na posicao ", str(temp) )
        time.sleep(random.randint(1,4)) #descanso um pouco

prod = Process(target=produtor)
prod2 = Process(target=produtor)
cons = Process(target=consumidor)
cons2 = Process(target=consumidor)

prod.start()
prod2.start()
cons.start()
cons2.start()

prod.join()
prod2.join()
cons.join()
cons2.join()