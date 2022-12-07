from json import dumps

from glc_class import GLC
from io_class import IO

Vn = ['S', 'A', 'B']
Vt = ['a', 'b', 'c']
S = 'S'
P = { 'S': ['aAc', 'bBc'], 'A': ['aAc', 'B', ''], 'B': ['bBc', '']}

my_glc = GLC(Vn, Vt, S, P)
op = -1

while op not in [0, None]:
    if op == 1:
        print(my_glc)
    elif op == 2:
        edit_op = -1

        while edit_op not in [0, None]:
            if edit_op == 1:
                print(my_glc)
            elif edit_op == 2:
                my_glc.Vn = IO.get_json_parsed_from_input(
                    "Não-Terminais: ",
                    dumps(my_glc.Vn)
                )
            elif edit_op == 3:
                my_glc.Vt = IO.get_json_parsed_from_input(
                    "Terminais: ",
                    dumps(my_glc.Vt)
                )
            elif edit_op == 4:
                my_glc.S = IO.get_first_char(
                    "Símbolo Inicial: ",
                    is_str=True,
                    expected_values=my_glc.Vn
                )
            elif edit_op == 5:
                print('some code here')

            edit_op = IO.get_first_char(
                my_glc.edit_glc_menu,
                is_int=True,
                expected_values=[0, 1, 2, 3, 4, 5]
            )

        op = -1
    elif op == 3:
        char_max = IO.get_first_char(
            "Entre com o número máximo de caracteres desejado: ",
            is_int=True
        )
        my_glc.generate_sentences(char_max)

    op = IO.get_first_char(
        msg=my_glc.initial_menu,
        is_int=True,
        expected_values=[0, 1, 2, 3]
    )

