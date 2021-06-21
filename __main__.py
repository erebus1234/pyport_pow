# -*- coding: utf-8 -*-
"""Main module

This module is the entry point for the application.
Additional CLI functionality for the application (help, params passed etc)
are included in the main function.
"""
import argparse
from argparse import ArgumentParser

from sil_py.power_engine import power_engine_main as power_main


def main(args=None):
    """
    main function of the application, calls other functions within the application
    :param: args : list of str, optional. List of command-line arguments. Defaults to `None`.
    :return: None: prints return from power_engine on the CLI
    """
    # init parser object for command line tool of application
    parser = ArgumentParser("sil-py")
    parser.set_defaults(func=lambda _: parser.print_help())
    parser = argparse.ArgumentParser(description="Print power cal values on screen")
    parser.add_argument(
        "-s",
        "--soc",
        type=float,
        default=0,
        help="state of charge to calculate power values (voltage, current)",
    )
    args = parser.parse_args()
    print(power_main(soc=args.soc))


if __name__ == "__main__":
    main()
