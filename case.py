'''exc_type: tipo de exceção que ocorreu, se houver
    Se não houver exceção, exc_type será None
exc_val: valor da exceção que ocorreu, se houver
    Se não houver exceção, exc_val será None
tb: traceback (rastreamento de pilha) do erro, se houver
    Se não houver exceção, tb será None'''

class AlgumaCoisa:
    def __enter__(self):
        print('Entrando')

    def __exit__(self, exc_type, exc_val, tb):
        print('Saindo')


with AlgumaCoisa() as something:

    print("estou no meio")
