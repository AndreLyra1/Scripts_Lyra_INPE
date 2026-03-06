# -*- coding: utf-8 -*-
"""
Description
-----------
This module contains functions to be used for input and output operations.
"""

import monan_analysis.config as config

def example_function_io():
    print ("this is a function imported from the io.py module.")

def get_MONAN_DIAG_filename(date_in_string_init, date_in_string_final):
    filename = (f"{config.PREFIX_STRING}_{date_in_string_init}_{date_in_string_final}.00.00."
                f"{config.GRID_STRING}{config.VERTICAL_LEVELS_STRING}.nc")
    return filename