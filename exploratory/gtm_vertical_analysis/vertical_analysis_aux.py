# -*- coding: utf-8 -*-
"""
vertical_analysis_aux.py

Based on a script by Andre Lyra (andre.lyra@inpe.br)
Last update: Feb 2026 by Guilherme Torres Mendonça (guilherme.mendonca@inpe.br)

Description
-----------
This module contains auxiliary functions to be used specifically in this analysis.

Usage
-----
- Import this module in scripts that are part of this specific analysis.
- Do not use this module for defining general-purpose functions.

Examples:
- from vertical_analysis_aux import setup_parser
or
- import vertical_analysis_aux as va_aux
  args = va_aux.setup_parser()

Acknowledgments
---------------
This file was created with the assistance of GitHub Copilot.    
"""

import argparse
import datetime
import os
import sys
from pathlib import Path
import monan_analysis.config as config
import matplotlib.pyplot as plt
import numpy as np

def setup_parser():
    """Set up the argument parser with common arguments."""
    parser = argparse.ArgumentParser(
        description="Vertical analysis of MONAN simulations.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--year', type=str, help='Year of initial conditions (e.g. 2025)')
    parser.add_argument('--month', type=str, help='Month of initial conditions (e.g. 12)')
    parser.add_argument('--day', type=str, help='Day of initial conditions (e.g. 01)')
    parser.add_argument('--hour', type=str, help='Hour of initial conditions (e.g. 00)')
    parser.add_argument('--time_window', type=int, help='Time window between initial conditions')
    
    args = parser.parse_args()
    return args

def plot_zonal_mean(ds, variable, lat_range=(-55, 20), lon_range=(275, 340)):
    """
    Plots the zonal mean of a variable over a specified region.

    Parameters:
        ds (xarray.Dataset): The input dataset.
        variable (str): The variable to analyze (e.g., 'temperature').
        lat_range (tuple): Latitude range (min, max) for the region.
        lon_range (tuple): Longitude range (min, max) for the region.
    """
    # Convert longitude range to -180 to 180 if necessary
    lon_min = lon_range[0] if lon_range[0] <= 180 else lon_range[0] - 360
    lon_max = lon_range[1] if lon_range[1] <= 180 else lon_range[1] - 360

    # Select the region
    region = ds[variable].sel(
        latitude=slice(lat_range[0], lat_range[1]),
        longitude=slice(lon_min, lon_max)
    )

    # Remove the singleton Time dimension
    region = region.squeeze(dim="Time", drop=True)

    # Calculate the zonal mean (mean over longitudes)
    zonal_mean = region.mean(dim="longitude")

    # Plot latitude vs vertical levels
    plt.figure(figsize=(8, 6))
    levels = zonal_mean.coords["level"]
    latitudes = zonal_mean.coords["latitude"]

    # Contour plot
    plt.contourf(latitudes, levels, zonal_mean.T, cmap="coolwarm", extend="both")
    plt.colorbar(label=f"{variable} (Zonal Mean)")
    plt.xlabel("Latitude")
    plt.ylabel("Vertical Levels (hPa)")
    plt.title(f"Zonal Mean of {variable} (South America)")
    plt.gca().invert_yaxis()  # Invert vertical levels for pressure coordinates
    plt.show()