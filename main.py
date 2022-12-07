from glc_class import GLC
from io_class import IO

Vn = ['S', 'A', 'B']
Vt = ['a', 'b', 'c']
S = 'S'
P = { 'S': ['aAc', 'bBc'], 'A': ['aAc', 'B', ''], 'B': ['bBc', '']}

my_glc = GLC(Vn, Vt, S, P)
op = -1

def get_op():
    global op
    op = IO.get_first_char("""
<1> Exibir GLC atual
<2> Editar GLC atual
<3> Exibir Produções da GLC atual
<0> Sair

Escolha uma opção: """,
    is_int=True,
    expected_values=[0, 1, 2, 3]
)

while op not in [0, None]:
    if op == 1:
        print(my_glc)
    elif op == 2:
        print('some code here')
    elif op == 3:
        char_max = IO.get_first_char(
            "Entre com o número máximo de caracteres desejado: ",
            is_int=True
        )
        my_glc.generate_sentences(char_max)

    get_op()

