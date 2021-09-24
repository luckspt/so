# SO
Programa que atua como intermediário entre user e hardware - controla a execução de todos os tipos de programas.

Dispositivos I/O têm controladores. Os controladores têm buffers (memória pequena tipo cache) que dps vai (o CPU move) para a memória ram.
O CPU só comunica com a memória RAM, e qdo precisa doss dados de um controlador (o controlador informa a CPU, através dos Drivers) para ir lá buscar.

## Estruturas dos SO

Utilizador e sistema correm programas (processos -> programas em execução) que fazem pedidos ao sistema (syscall) pelas APIs para aceder aos serviços do SO.
