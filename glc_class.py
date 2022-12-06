class GLC:
    def __init__(self, Vn: list, Vt: list, S: str, P: dict):
        self.Vn = Vn
        self.Vt = Vt
        self.S = S
        self.P = P
        self.present_class = f"Não Terminais: {Vn}\nTerminais: {Vt}\nSímbolo Inicial: {S}\nProduções: {P}\n"

    def __str__(self):
        return self.present_class
    
    def __repr__(self):
        return self.present_class

    def generate_sentences(self, largest_sencente_length: int) -> list:
        sentences = []

        productions_to_check = ['S']

        fn = lambda x: len(x) == len([c for c in x if c.islower()])

        while True:
            curr_production = productions_to_check[0]

            found_non_terminal = False

            # replaces first non-terminal found on sentece by its productions
            for index, sentence_char in enumerate(curr_production):
                if sentence_char.isupper():
                    found_non_terminal = True
                    non_terminal_productions = []

                    for p in self.P[sentence_char]:
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

        print(sentences)

        return sentences
    
    def is_upper_char(self, char):
        UPPER_ASCII_MIN = 65
        UPPER_ASCII_MAX = 90

        return (
            isinstance(char, str) and
            ord(char) >= UPPER_ASCII_MIN and
            ord(char) <= UPPER_ASCII_MAX
        )
    
    def is_lower_char(self, char):
        LOWER_ASCII_MIN = 61
        LOWER_ASCII_MAX = 122

        return (
            isinstance(char, str) and
            ord(char) >= LOWER_ASCII_MIN and
            ord(char) <= LOWER_ASCII_MAX
        )

    def is_non_terminal(self, char):
        return isinstance(char, str) and self.is_upper_char(char) and char in self.Vn
    
    def is_terminal(self, char):
        return isinstance(char, str) and self.is_lower_char(char) and char in self.Vt
    
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
                            are_productions_valid = False

                            for p in productions:
                                is_production_valid = False

                                for c in p:
                                    if (
                                        self.is_terminal(c) or
                                        self.is_non_terminal(c)
                                    ):
                                        continue
                                    break
                                else:
                                    is_production_valid = True
                                
                                if not is_production_valid:
                                    break
                            else:
                                are_productions_valid = True
                            
                            if not are_productions_valid:
                                break
                        else:
                            break
                    else: # went through all productions and they are all valid
                        return self.is_non_terminal(self.S)
        return False
        
