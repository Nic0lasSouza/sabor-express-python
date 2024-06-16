from models.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_pizza = Restaurante('pizza express', 'Italiana')
# restaurante_mexicano = Restaurante('mexican food', 'mexicana')

restaurante_praca.receber_avaliacao('gui', 10)
restaurante_praca.receber_avaliacao('joao', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()