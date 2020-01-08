import abc

from constantes import TAMANHO_PADRAO_MINIMO, TAMANHO_PADRAO_MAXIMO


class FilaBase(metaclass=abc.ABCMeta):

    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual = None

    def genha_senhas(self):
        self.busca_posicao_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    def inseri_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    def busca_posicao_fila(self):
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
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
