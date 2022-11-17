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
