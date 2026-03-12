# -*- coding: utf-8 -*-
"""
config.py

Description
-----------
This configuration file contains general-purpose settings and constants that are
shared across multiple analyses. It includes reusable strings, default
parameters, and other general configurations.

Usage
-----
- Import this file in scripts that require general-purpose settings.
- Avoid adding project-specific configurations to this file.

Examples:
- from monan_analysis.config import PREFIX_STRING
or 
- import monan_analysis.config as config
  prefix_string = config.PREFIX_STRING

Acknowledgments
---------------
This file was created with the assistance of GitHub Copilot. 
"""
# Standard strings for MONAN output filenames
## Standard prefix in output filenames
PREFIX_STRING = "MONAN_DIAG_G_POS_GFS"
## Strings for each grid configuration
GRID_10KM_UNIFORM_STRING = "x5898242"
GRID_24KM_UNIFORM_STRING = "x1024002"
## Strings for each vertical level configuration
VERTICAL_LEVEL_L30_STRING = "L30"
VERTICAL_LEVEL_L55_STRING = "L55"

# Standard date format in MONAN output filenames
DATE_FORMAT = "%Y%m%d%H"