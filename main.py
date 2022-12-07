from json import dumps
from re import sub

from glc_class import GLC
from io_class import IO

Vn = ["S", "A", "B"]
Vt = ["a", "b", "c"]
S = "S"
P = { "S": ["aAc", "bBc"], "A": ["aAc", "B", ""], "B": ["bBc", ""]}

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
                my_glc.Vn = IO.get_list_from_input(
                    "Não-Terminais: ",
                    dumps(my_glc.Vn),
                    isupper=True
                )
            elif edit_op == 3:
                my_glc.Vt = IO.get_list_from_input(
                    "Terminais: ",
                    dumps(my_glc.Vt),
                    islower=True
                )
            elif edit_op == 4:
                my_glc.S = IO.get_first_char(
                    "Símbolo Inicial: ",
                    is_str=True,
                    expected_values=my_glc.Vn,
                    pre_input=my_glc.S
                )
            elif edit_op == 5:
                expected_values = IO().bool_expected_answer
                prod_op = "X"

                while prod_op not in expected_values:
                    print("\nAtenção: suas produções atuais serão removidas!")
                    print("Só é possível alterar as produções da GLC atual removendo-as e reinserindo-as.")
                    print("Recomenda-se separar num bloco de notas as produções desejadas e colar elas no prompt.")
                    prod_op = IO.get_first_char(
                        "\nDeseja continuar? <Y/n>: ",
                        is_str=True,
                        expected_values=expected_values
                    )
                
                if prod_op == "Y":
                    my_glc.P = {}
                    prod_op = -1
                    separator = my_glc.production_separator

                    print("\nRecomendações:")
                    print("1. As produções devem ser inseridas individualmente. Se um mesmo cabo produz mais de uma produção, cada produção deve estar em uma linha diferente.")
                    print(f"2. As produções devem utilizar do símbolo '{separator}' para separar o cabo da produção.")
                    print("3. Recomenda-se separar num bloco de notas as produções desejadas e colar elas no prompt.")
                    print("\nInsira suas produções abaixo seguindo as orientações mencionadas:")
                    while True:
                        prod_op = input()

                        if prod_op:
                            try:
                                prod_op = sub(r'\s', '', prod_op)
                                if my_glc.validate_production(prod_op):
                                    non_terminal, production = prod_op.split(separator)

                                    if non_terminal in my_glc.P:
                                        if production not in my_glc.P[non_terminal]:
                                            my_glc.P[non_terminal].append(production)
                                    else:
                                        my_glc.P[non_terminal] = [production]
                            except:
                                pass
                        else:
                            break

            edit_op = IO.get_first_char(
                my_glc.edit_glc_menu,
                is_int=True,
                expected_values=[0, 1, 2, 3, 4, 5]
            )

        op = -1
    elif op == 3:
        if my_glc.validate_glc():
            char_max = IO.get_first_char(
                "Entre com o número máximo de caracteres desejado: ",
                is_int=True
            )
    
            my_glc.generate_sentences(char_max)
        else:
            print('\nErro: a GLC atual não é válida! Favor corrigir para fazer uso desta opção.')

    op = IO.get_first_char(
        msg=my_glc.initial_menu,
        is_int=True,
        expected_values=[0, 1, 2, 3]
    )

