from models.restaurante import Restaurante
from models.cardapio.bebidas import Bebidas
from models.cardapio.prato import Prato

rest_1 = Restaurante('surf dog', 'executivo')
rest_2 = Restaurante('burgman', 'bar')
rest_3 = Restaurante('Sr miag', 'japones')

bebida_suco = Bebidas('Laranja', 11.90, '400 ml')
hamburger_prato = Prato('Hamburger master', 45.8, 'O maior burger da casa')

rest_2.adiciona_item_ao_cardapio(hamburger_prato)
rest_2.adiciona_item_ao_cardapio(bebida_suco)



def main():
    rest_2.exibir_cardapio

if __name__ == '__main__':
    main()