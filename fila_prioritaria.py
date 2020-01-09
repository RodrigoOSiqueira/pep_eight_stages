from typing import Dict, Union, List, Any

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{self.codigo}'

    def chama_cliente(self, caixa: int) -> list:
        display = []
        cliente_atual = self.fila.pop(0)
        display.append(f'Cliente: {cliente_atual} - Caixa {caixa}')

        if len(self.fila) >= 3:
            display.append(f'Próximo: {self.fila[0]}')
            display.append(f'Fique atento: {self.fila[1]}')

        self.clientes_atendidos.append(cliente_atual)

        return display

    def estatistica(self, dia: str, agencia: str, flag_detail: str):
        estatistica: Dict[str, Union[int, str, List[str]]] = {}

        if flag_detail != 'detail':
            estatistica = ({
                f'{agencia} - {dia}':
                f'{len(self.clientes_atendidos)} clientes atendido(s)'
            })
        else:
            
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['quantidade de clientes atendidos'] = (
                len(self.clientes_atendidos)
            )
            estatistica['clientes atendidos'] = self.clientes_atendidos

        return estatistica