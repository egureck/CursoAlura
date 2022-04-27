from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria


# fila_teste = FilaNormal()
# fila_teste.AtualizaFila()
# fila_teste.AtualizaFila()
# fila_teste.AtualizaFila()
# print(fila_teste.ChamaCliente(1))
# print(fila_teste.ChamaCliente(10))
fila_teste2 = FilaPrioritaria()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(10))
print(fila_teste2.chama_cliente(2))
print(fila_teste2.estatistica('25/04/2022', 222, 'detail'))