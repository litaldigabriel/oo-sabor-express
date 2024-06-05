from modelos.avaliacao import Avaliacao

class Restaurante:
    '''Inicializar a lista de restaurantes'''
    restaurantes = []

    def __init__(self, nome, categoria):   
        '''Construtor com os itens da classe restaurante'''     
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Função que faz retornar como string(letras) quando utilizar o print'''
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_resturantes(cls):
        '''Função para listar o restaurante dentro da lista de restaurantes'''
        print (f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property    
    def ativo(self):
        '''Função que altera a mensagem no print de True/False para a que desejar'''
        return 'Ativado' if self._ativo else 'Desativado'

    def alternar_estado(self):
        '''Função para alterar o estado do restaurante'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Função que recebe as avaliações e coloca dentro de uma lista de avaliações'''
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Função que faz a média das avaliações'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media