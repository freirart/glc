from typing import Union
from re import sub

class IO:
    @staticmethod
    def get_first_char(msg: str, is_int=False, is_str=False, expected_values=[]) -> Union[str, int]:
        while True:
            op = input(msg)

            regex_str = "\s"
            err_message = "\nErro! Por favor insira um"

            if is_int:
                regex_str += "|\D"
                err_message += " número."
            elif is_str:
                regex_str += "|\W"
                err_message += "a letra."
            else:
                err_message += " dígito."
        
            try:
                formatted_char = sub(regex_str, '', op)

                if is_int:
                    formatted_char = int(formatted_char)
                else:
                    formatted_char = formatted_char[0]

                if (
                    not expected_values or (
                        expected_values and
                        isinstance(expected_values, list) and
                        formatted_char in expected_values
                    )
                ):
                    return formatted_char
                
                err_message = err_message[:-1] + ' válido.'
                raise ValueError(err_message)
            except:
                print(err_message)
