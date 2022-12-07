import readline

from typing import Union
from re import sub
from json import loads

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
                
                err_message = err_message[:-1] + ' válido(a).'
                raise ValueError(err_message)
            except:
                print(err_message)
    
    @staticmethod
    def get_json_parsed_from_input(prompt, text):
        while True:
            try:
                value_inputted = IO.__input_with_prefill(prompt, text)
                json_parsed = loads(value_inputted)
                return json_parsed
            except:
                print('\nO valor digitado é inválido! Favor tentar novamente.\n')

    @staticmethod
    def __input_with_prefill(prompt, text):
        def hook():
            readline.insert_text(text)
            readline.redisplay()
        readline.set_pre_input_hook(hook)
        result = input(prompt)
        readline.set_pre_input_hook()
        return result
