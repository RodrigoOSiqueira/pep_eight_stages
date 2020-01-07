class filanormal:
    codigo = 0
    fila = []
    clintesatendidos = []
    senhaatual = None
    def gerasenhaatual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'
    def chamacliente(self, caixa:int) -> str:
        clienteatual = self.fila.pop(0)
        self.clintesatendidos.append(clienteatual)
        return f'Cliente: {clienteatual} - Caixa {caixa}'
    def estatistica(self, dia:str, agencia:str, flag_detail:str):
        if flag_detail != 'detail':
            estatistica = (
                f'{agencia} - {dia}: '
                f'{len(self.clintesatendidos)} clientes atendido(s)'  
            )
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['quantidade de clientes atendidos'] = len(self.clintesatendidos)
            estatistica['clientes atendidos'] = self.clintesatendidos
        return estatistica
    def resetafila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
    def atualizafila(self) -> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)
