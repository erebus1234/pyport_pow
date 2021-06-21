# -*- coding: utf-8 -*-
from sil_py.helpers import get_time_string as time_str


def print_message(print_string: str) -> str:
    """
    returns print message to display on CLI
    :param print_string: string to be displayed
    :return: print_msg:
    """
    print_msg = print_string + " " + time_str()
    return print_msg
