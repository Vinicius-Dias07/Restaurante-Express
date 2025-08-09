from models.restaurante import Restaurante
rest_1 = Restaurante('surf dog', 'executivo')
rest_2 = Restaurante('burgman', 'bar')
rest_3 = Restaurante('Sr miag', 'japones')

rest_1.altelnar_estado()
rest_1.receber_avaliacao('Vinicius', 8)
rest_1.receber_avaliacao('Amanda', 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()