from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from fila_base import FilaBase
from constantes import FILA_NORMAL, FILA_PRIORITARIA
# fila_dia_x = FilaNormal()
# fila_dia_x.atualiza_fila()
# fila_dia_x.atualiza_fila()
# fila_dia_x.atualiza_fila()
# fila_dia_x.atualiza_fila()
# print(fila_dia_x.chama_cliente(5))
# print(fila_dia_x.estatistica('26/11/2019', '561', 'detail'))

# fila_prioritaria_dia_x = FilaPrioritaria()
# fila_prioritaria_dia_x.atualiza_fila()
# fila_prioritaria_dia_x.atualiza_fila()
# fila_prioritaria_dia_x.atualiza_fila()
# fila_prioritaria_dia_x.atualiza_fila()
# print(fila_prioritaria_dia_x.chama_cliente(5))
# print(fila_prioritaria_dia_x.chama_cliente(5))
# print(fila_prioritaria_dia_x.chama_cliente(5))
# print(fila_prioritaria_dia_x.estatistica('26/11/2019', '512', 'detail'))

# fila_prioritaria = FilaPrioritaria()
# fila_normal = FilaNormal()
# fila_prioritaria.genha_senhas()
# fila_normal.genha_senhas()
# fila_prioritaria.genha_senhas()
# fila_normal.genha_senhas()
# fila_prioritaria.genha_senhas()
# fila_normal.genha_senhas()
# fila_prioritaria.genha_senhas()
# fila_normal.genha_senhas()
# print(fila_prioritaria.chama_cliente(1))
# print(fila_normal.chama_cliente(2))
# print(fila_normal.estatistica('26/11/2019', '512', 'detail'))
# print(fila_prioritaria.estatistica('26/11/2019', '512', 'detail'))

fila = FabricaFila.pega_fila(4)
