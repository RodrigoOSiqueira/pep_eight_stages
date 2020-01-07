from typing import Dict, Any


class FilaPrioritaria:
    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual = None

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def chama_cliente(self, caixa:int) -> list:
        display = []
        cliente_atual = self.fila.pop(0)
        display.append(f'Cliente: {cliente_atual} - Caixa {caixa}')

        if len(self.fila) >= 3:
            display.append(f'Próximo: {self.fila[0]}')
            display.append(f'Fique atento: {self.fila[1]}')

        self.clientes_atendidos.append(cliente_atual)

        return display  

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)
        
    def estatistica(self, dia:str, agencia:str, flag_detail:str):
        if flag_detail != 'detail':
            estatistica = (
                f'{agencia} - {dia}: '
                f'{len(self.clientes_atendidos)} clientes atendido(s)'  
            )
        else:
            estatistica: Dict[str, Any] = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['quantidade de clientes atendidos'] = len(self.clientes_atendidos)
            estatistica['clientes atendidos'] = self.clientes_atendidos
            
        return estatistica
        