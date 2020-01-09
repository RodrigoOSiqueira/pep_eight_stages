from typing import Union

from constantes import FILA_NORMAL, FILA_PRIORITARIA
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila)-> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == FILA_NORMAL:
            return FilaNormal()
        if tipo_fila == FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo não cadastrado')
