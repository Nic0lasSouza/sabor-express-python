from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato


bebida_suco =Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco2 =Bebida('Suco de Laranja', 3.5, 'Media')

prato_pao = Prato('Pao', 2.00, 'O melhor pão da cidade')
# restaurante_praca = Restaurante('praça', 'Gourmet')
# # restaurante_pizza = Restaurante('pizza express', 'Italiana')
# # restaurante_mexicano = Restaurante('mexican food', 'mexicana')

# restaurante_praca.receber_avaliacao('gui', 10)
# restaurante_praca.receber_avaliacao('joao', 8)

def main():
    # Restaurante.listar_restaurantes()
    print(bebida_suco)
    print(bebida_suco2)
    print(prato_pao)


if __name__ == '__main__':
    main()