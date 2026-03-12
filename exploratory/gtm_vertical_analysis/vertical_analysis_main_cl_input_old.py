# -*- coding: utf-8 -*-
"""
vertical_analysis_main.py

Based on a script by Andre Lyra (andre.lyra@inpe.br)
Last update: Feb 2026 by Guilherme Torres Mendonça (guilherme.mendonca@inpe.br)
Last update: Mar 2026 by Guilherme Torres Mendonça (guilherme.mendonca@inpe.br)

Description
-----------
Takes in data from MONAN and from GFS and performs an analysis of the vertical structure of MONAN.

Steps:
1. Read data from MONAN and from GFS
2. Preprocess data
3. Calculate statistics
4. Plot and save results

Input
-----
- ds_monan (xr.Dataset): netcdf file containing MONAN data
- ds_gfs (xr.Dataset): netcdf file containing GFS data

Output
------
- RMSE values
- Analysis maps

Main variables
--------------
- RMSE (float64): root mean square error

Acknowledgments
---------------
This file was created with the assistance of GitHub Copilot. 
"""

import vertical_analysis_aux as va_aux
import monan_analysis.config as config
import monan_analysis.io as io
import monan_analysis.utils as utils
import xarray as xr
import vertical_analysis_config as va_config
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    # Get input arguments
    args = va_aux.setup_parser()

    # Get filename for reading MONAN data
    ## Date for initial conditions
    date_init_in_datetime = utils.date_as_datetime(args.year, args.month, args.day, args.hour)
    date_init_in_string = utils.date_as_YYYYMMDDHH_str(args.year, args.month, args.day, args.hour)
    ## Date for end of time window
    date_final_in_datetime = utils.get_final_date_from_initial_date(date_init_in_datetime, args.time_window)
    date_final_in_string = date_final_in_datetime.strftime(config.DATE_FORMAT)
    ## MONAN output filename
    filename = io.get_MONAN_DIAG_filename(date_init_in_string,date_final_in_string,grid_spec=va_config.GRID_SPEC)
    print (filename)

    # Read data from MONAN
    ## Get complete path
    filepath = f"{va_config.MONAN_PREOP}/{date_init_in_string}/{filename}"
    print (filepath)
    ds_monan = xr.open_dataset(filepath, engine="netcdf4")
    print (ds_monan)

    va_aux.plot_zonal_mean(ds_monan)

    # Preprocess MONAN data
    #var='temperature'
    #ds_monan_preprocessed = va_aux.preprocess_monan_data(ds_monan)

    # Plot MONAN data
    #ds = xr.open_dataset("/lustre/projetos/monan_atm/guilherme.mendonca/scratch/output2.nc", engine="netcdf4")
    #print (ds)
    #plt.figure(figsize=(10, 6))

    

    # # Extract data
    # temperature = ds['temperature'].squeeze()  # Remove single-dimensional entries (e.g., Time, lon)
    # levels = ds['level']
    # print (levels)
    # latitudes = ds['lat']
    # print (latitudes)

    # # Create the plot
    # plt.figure(figsize=(10, 6))
    # contour = plt.contourf(latitudes, levels, temperature, levels=18, cmap='coolwarm')

    # # Invert the y-axis so pressure levels decrease upward
    # plt.gca().invert_yaxis()

    # # Add labels and title
    # plt.xlabel('Latitude')
    # plt.ylabel('Pressure Level (hPa)')
    # plt.title('Zonal Mean Temperature')
    # plt.colorbar(contour, label='Temperature (K)')

    # # Show the plot
    # plt.show()
    # plt.savefig('zonal_mean_temperature.png', dpi=300, bbox_inches='tight')  # Save as PNG with high resolution
    # plt.close()
