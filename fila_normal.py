from fila_base import FilaBase

from constantes import CODIGO_NORMAL, TAMANHO_PADRAO_MINIMO


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_NORMAL}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente: {cliente_atual} - Caixa {caixa}'

    def estatistica(self, dia: str, agencia: str, flag_detail: str):
        if flag_detail != 'detail':
            estatistica = (
                f'{agencia} - {dia}: '
                f'{len(self.clientes_atendidos)} clientes atendido(s)'
            )
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['quantidade de clientes atendidos'] = (
                len(self.clientes_atendidos)
            )
            estatistica['clientes atendidos'] = self.clientes_atendidos

        return estatistica

    def busca_posicao_fila(self) -> None:
        if self.codigo >= 1000:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1
