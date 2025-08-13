from models.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.lower()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'nome: {self._nome.ljust(10)} | categoria: {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls): 
        print(f'{'Restaurante:'.ljust(10)} | {'categoria:'.ljust(11)} | {'Avliacoes:'.ljust(11)} | ativo:')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(12)} | {restaurante._categoria.ljust(11)} | {str(restaurante.media).ljust(11)} | {restaurante.ativo}')                 
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

    def altelnar_estado(self):
        self._ativo = not self._ativo 

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) 
        num_avaliacoe = len(self._avaliacao)
        media = round(soma_das_notas / num_avaliacoe, 1)
        return media





