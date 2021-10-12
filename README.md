# SO

Programa que atua como intermediário entre user e hardware - controla a execução de todos os tipos de programas.

Dispositivos I/O têm controladores. Os controladores têm buffers (memória pequena tipo cache) que dps vai (o CPU move) para a memória ram.
O CPU só comunica com a memória RAM, e qdo precisa doss dados de um controlador (o controlador informa a CPU, através dos Drivers) para ir lá buscar.

## Estruturas dos SO

Utilizador e sistema correm programas (processos -> programas em execução) que fazem pedidos ao sistema (syscall) pelas APIs para aceder aos serviços do SO.

## Gestão Processos (Python)
Ter dois códigos em execução ao mesmo tempo. `os.fork()` returna 0 se for o filho, >0 se for o pai (o valor é o pid do filho) ou -1 se der erro
```py
pid = os.fork()
if pid == 0: 
    # filho
    x = 443
    print('(filho) numero ' + str(x))
    sys.exit(x) # o filho morre aqui
else:
    # pai
    ipid, resultado = os.wait() # o pai fica à espera do filho
    if os.WIFEXITED(resultado):
        print('(pai) Resultado do filho: ' + str(os.WIEXITEDSTATUS(resultado)))
```
