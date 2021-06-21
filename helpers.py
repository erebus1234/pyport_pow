"""helper functions

This file contains helper functions to go with core functionality
"""

import time


def get_time_string() -> str:
    """
    return current time as string
    :return: time_str: current time as string
    """
    time_str = time.strftime("%Y%m%d_%H%M%S")
    return time_str
