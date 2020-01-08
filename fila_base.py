import abc


class FilaBase(metaclass=abc.ABCMeta):

    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual = None

    def genha_senhas(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    def inseri_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    def reseta_fila(self):
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa):
        ...

    @abc.abstractmethod
    def estatistica(self, dia, agencia, flag_detail):
        ...
