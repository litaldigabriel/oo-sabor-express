from modelos.restaurante import Restaurante

restaurante_comidaria = Restaurante('Comidaria', 'Hamburgueria')
restaurante_comidaria.receber_avaliacao('Gui', 10)
restaurante_comidaria.receber_avaliacao('Lais', 8)
restaurante_comidaria.receber_avaliacao('Emy', 2)

def main():
    Restaurante.listar_resturantes()

'''Quando criar o arquivo principal sempre utilizar conforme abaixo para dizer qual arquivo é a main e não importar em outro arquivo'''
if __name__ == '__main__':
    main()