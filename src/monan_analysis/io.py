# -*- coding: utf-8 -*-
"""
io.py

Description
-----------
This module contains functions to be used for input and output operations.

Usage
-----
- Import this module in scripts that require input/output functions.
- Functions in this module should be general-purpose and reusable across different analyses.

Examples:
- from monan_analysis.io import get_MONAN_DIAG_filename
or 
- import monan_analysis.io as io
  filename = io.get_MONAN_DIAG_filename(date_in_string_init, date_in_string_final)

Acknowledgments
---------------
This file was created with the assistance of GitHub Copilot. 
"""

import monan_analysis.config as config

def example_function_io():
    print ("this is a function imported from the io.py module.")

def get_MONAN_DIAG_filename(date_in_string_init, date_in_string_final,grid_spec,vertical_level_spec):
    # Check grid configuration
    if grid_spec == '10km_uniform':
        GRID_STRING = config.GRID_10KM_UNIFORM_STRING
    elif grid_spec == '24km_uniform':
        GRID_STRING = config.GRID_24KM_UNIFORM_STRING
    else:
        raise ValueError(f"Grid '{grid_spec}' is not recognized. Please choose a valid grid.")
    # Check vertical level configuration
    if vertical_level_spec == '30':
        VERTICAL_LEVEL_STRING = config.VERTICAL_LEVEL_L30_STRING
    elif vertical_level_spec == '55':
        VERTICAL_LEVEL_STRING = config.VERTICAL_LEVEL_L55_STRING
    else:
        raise ValueError(f"Vertical level configuration '{vertical_level_spec}' is not recognized. " 
                         + "Please choose a valid configuration.")
    
    filename = (f"{config.PREFIX_STRING}_{date_in_string_init}_{date_in_string_final}.00.00."
                f"{GRID_STRING}{VERTICAL_LEVEL_STRING}.nc")
    return filename