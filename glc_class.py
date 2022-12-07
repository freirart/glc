class GLC:
    def __init__(self, Vn: list, Vt: list, S: str, P: dict):
        self.Vn = Vn
        self.Vt = Vt
        self.S = S
        self.P = P
        self.present_class = self.get_updated_present_class_str()
        self.production_separator = '->'
        self.initial_menu = """
<1> Exibir GLC atual
<2> Editar GLC atual
<3> Exibir Produções da GLC atual
<0> Sair

Escolha uma opção: """
        self.edit_glc_menu = """
<1> Exibir GLC
<2> Editar Não-Terminais
<3> Editar Terminais
<4> Editar Símbolo Inicial
<5> Editar Produções
<0> Voltar

Escolha uma opção: """

    def __str__(self):
        return self.get_updated_present_class_str()
    
    def __repr__(self):
        return self.get_updated_present_class_str()

    def get_updated_present_class_str(self):
        return f"\nNão Terminais: {self.Vn}\nTerminais: {self.Vt}\nSímbolo Inicial: {self.S}\nProduções: {self.P}\n"

    def generate_sentences(self, largest_sencente_length: int) -> list:
        sentences = []

        productions_to_check = [self.S]

        fn = lambda x: len(x) == len([c for c in x if c.islower()])

        while productions_to_check:
            curr_production = productions_to_check[0]

            found_non_terminal = False

            # replaces first non-terminal found on sentece by its productions
            for index, sentence_char in enumerate(curr_production):
                registered_productions = self.P.get(sentence_char)
                if (
                    sentence_char.isupper() and
                    registered_productions and
                    isinstance(registered_productions, list)
                ):
                    found_non_terminal = True
                    non_terminal_productions = []

                    for p in registered_productions:
                        replaced_non_terminal = (
                            (
                                curr_production[:index] +
                                p +
                                curr_production[index + 1:]
                            )
                            if len(curr_production) > 1
                            else p
                        )

                        non_terminal_productions.append(replaced_non_terminal)

                    productions_to_check = sorted(
                        sorted(
                            sorted(
                                productions_to_check[1:] + non_terminal_productions,
                                key=fn,
                                reverse=True
                            )
                        ),
                        key=len
                    )

                    break

            if found_non_terminal is False:
                if len(curr_production) <= largest_sencente_length:
                    if curr_production not in sentences:
                        sentences.append(curr_production)
                else:
                    break

                productions_to_check = productions_to_check[1:]

        if len(sentences) == 1 and sentences[0] == self.S:
            sentences = []

        print(sentences)

        return sentences
    
    @staticmethod
    def is_upper_char(char):
        UPPER_ASCII_MIN = 65
        UPPER_ASCII_MAX = 90

        return (
            char and
            isinstance(char, str) and
            len(char) == 1 and
            ord(char) >= UPPER_ASCII_MIN and
            ord(char) <= UPPER_ASCII_MAX
        )
    
    @staticmethod
    def is_lower_char(char):
        LOWER_ASCII_MIN = 97
        LOWER_ASCII_MAX = 122

        return (
            char and
            isinstance(char, str) and
            len(char) == 1 and
            ord(char) >= LOWER_ASCII_MIN and
            ord(char) <= LOWER_ASCII_MAX
        )

    def is_non_terminal(self, char):
        return isinstance(char, str) and self.is_upper_char(char) and char in self.Vn
    
    def is_terminal(self, char):
        return isinstance(char, str) and self.is_lower_char(char) and char in self.Vt
    
    def validate_production(self, production_str: str) -> bool:
        if isinstance(production_str, str) and self.production_separator in production_str:
            try:
                non_terminal, production = production_str.split(self.production_separator)
                if self.is_non_terminal(non_terminal):
                    for char in production:
                        if (
                            self.is_terminal(char) or
                            self.is_non_terminal(char)
                        ):
                            continue
                        break
                    else:
                        return True

            except:
                return False
        
        return False

    
    def validate_glc(self):
        are_non_terminals_valid = (
            isinstance(self.Vn, list) and 
            not len([vn for vn in self.Vn if not self.is_non_terminal(vn)])
        )

        if are_non_terminals_valid:
            are_terminals_valid = (
                isinstance(self.Vn, list) and 
                not len([vn for vn in self.Vt if not self.is_terminal(vn)])
            )
            
            if are_terminals_valid:
                if isinstance(self.P, dict):
                    for non_terminal, productions in self.P.items():
                        if (
                            self.is_non_terminal(non_terminal) and
                            isinstance(productions, list)
                        ):
                            for p in productions:
                                formatted_production = (
                                    f"{non_terminal}{self.production_separator}{p}"
                                )

                                if not self.validate_production(formatted_production):
                                    break
                            else:
                                continue
                            break
                        else:
                            break
                    else: # went through all productions and they are all valid
                        return self.is_non_terminal(self.S)
        return False
        
