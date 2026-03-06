# -*- coding: utf-8 -*-
"""
Based on a script by Andre Lyra (andre.lyra@inpe.br)
Last update: Feb 2026 by Guilherme Torres Mendonça (guilherme.mendonca@inpe.br)

Description
-----------
Module containing auxiliary functions to be used in the main analysis script vertical_analysis.py.
"""

import argparse
import datetime
import os
import sys
from pathlib import Path
import config

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

def date_as_datetime(year,month,day,hour):
    date_in_datetime = datetime.datetime(
            int(year), 
            int(month), 
            int(day), 
            int(hour)
        )
    return date_in_datetime

def date_as_YYYYMMDDHH_str(year,month,day,hour):
    date_in_string = f"{year}{month}{day}{hour}" 
    return date_in_string

def get_MONAN_DIAG_filename(date_in_string_init, date_in_string_final):
    filename = (f"{config.PREFIX_STRING}_{date_in_string_init}_{date_in_string_final}.00.00."
                f"{config.GRID_STRING}{config.VERTICAL_LEVELS_STRING}.nc")
    return filename

def get_final_date_from_initial_date(date_in_datetime, time_window):
    date_final_in_datetime = date_in_datetime + datetime.timedelta(hours=time_window)
    return date_final_in_datetime

# delta_hora = datetime.timedelta(hours=0)
# delta_dia = datetime.timedelta(hours=24)
# num_dias = args.PRAZO_H // 24
    
# print("\n" + "=" * 60)
# print(f"PROCESSAMENTO DE {num_dias} PERIODOS DE 24 HORAS")
# print("=" * 60)
    
  
# pares_arquivos = []

# # Loop para cada periodo de 24 horas
# for i in range(num_dias):
#     data_inicial_acumulo = data_inicio_base + (delta_dia * i) + (delta_hora * (i+1))
#     data_final_acumulo = data_inicial_acumulo + delta_dia
#     Fct=f"{((i+1)*24):03d}"   

#     # Formato de data/hora esperado no nome do arquivo (YYYYMMDDHH)
#     formato_data = '%Y%m%d%H'
#     data_str_i = data_inicial_acumulo.strftime(formato_data)
#     data_str_e = data_final_acumulo.strftime(formato_data)
    
# # Montando nome dos arquivos
# #    CAMINHO_BASE = "/lustre/projetos/monan_adm/monan/ecf_PREOPER/MONAN-WorkFlow-OPER/MONAN_PRE_OPER/MONAN/scripts_CD-CT/dataout/"
#     CAMINHO_BASE = "/lustre/projetos/monan_adm/monan/ecf_PREOPER/MONAN-WorkFlow-OPER/MONAN_PRE_OPER/MONAN/scripts_CD-CT/dataout/flushout/"
#     DIR_DATA = f"{data_inicial}/"
#     PREFIXO_ARQ  = "MONAN_DIAG_G_POS_GFS_"
#     SUFIXO_ARQ   = ".00.00.x5898242L55.nc" 
#     nome_arquivo_i = f"{PREFIXO_ARQ}{data_inicial}_{data_str_i}{SUFIXO_ARQ}"
#     nome_arquivo_e = f"{PREFIXO_ARQ}{data_inicial}_{data_str_e}{SUFIXO_ARQ}"
    
#     # Monta o caminho completo
#     caminho_completo_i = os.path.join(CAMINHO_BASE, DIR_DATA, nome_arquivo_i)
#     caminho_completo_e = os.path.join(CAMINHO_BASE, DIR_DATA, nome_arquivo_e)

#     pares_arquivos.append((caminho_completo_i, caminho_completo_e))

#     # Imprimindo as datas de acumulo
#     print(f"--- Acumulado {i+1} --- Previsao {Fct}h ---")
#     print(f"Data Inicial: {data_inicial_acumulo.strftime('%Y-%m-%d %H:%M:%S')}")
#     print(f"Data Final:   {data_final_acumulo.strftime('%Y-%m-%d %H:%M:%S')}")
#     print(f"Arquivo I: {caminho_completo_i}")
#     print(f"Arquivo E: {caminho_completo_e}")
    
#     print("=" * 60)
        
# # Caminho dos arquivos (MONAN)
#     arquivoi = caminho_completo_i
#     arquivoe = caminho_completo_e
# #    print(arquivoi)
# #    print(arquivoe)

# # Inicializa variaveis de referencia
#     precip_soma = None
#     lat = lon = None

#     fi = xr.open_dataset(arquivoi, engine="netcdf4")
#     fe = xr.open_dataset(arquivoe, engine="netcdf4")

if __name__ == "__main__":
    args = setup_parser()
    print (args.year)
    date_in_datetime = date_in_datetime_format(args)
    date_in_string = date_in_string_format(args)
    print (f"Date in datetime format: {date_in_datetime}")
    print (f"Date in string format: {date_in_string}")