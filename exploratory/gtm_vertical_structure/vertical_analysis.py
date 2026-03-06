# -*- coding: utf-8 -*-
"""
Based on a script by Andre Lyra (andre.lyra@inpe.br)
Last update: Feb 2026 by Guilherme Torres Mendonça (guilherme.mendonca@inpe.br)

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
"""

import argparse
import datetime
import os
os.environ["CARTOPY_DATA_DIR"] = "/lustre/projetos/monan_gam/andre.lyra/cartopy"
import sys
import xarray as xr
import numpy as np
from pathlib import Path


parser = argparse.ArgumentParser(
        description="Vertical analysis of MONAN simulations.", 
        formatter_class=argparse.RawTextHelpFormatter 
    )

# Argumentos da data inicial
parser.add_argument('year', type=str, help='Year of initial conditions (e.g. 2025)')
parser.add_argument('month', type=str, help='Month of initial conditions (e.g. 12)')
parser.add_argument('day', type=str, help='Day of initial conditions (e.g. 01)')
parser.add_argument('hour', type=str, help='Hour of initial conditions (e.g. 00)')
    
# Argumento do prazo total
parser.add_argument('time_window', type=int, help='Time window between initial conditions and final prediction date in hours (e.g. 72, 120)')

args = parser.parse_args()

data_inicio_base = datetime.datetime(
     int(args.ANO), 
     int(args.MES), 
     int(args.DIA), 
     int(args.HORA)
        )

data_inicial = f"{args.ANO}{args.MES}{args.DIA}{args.HORA}" 

delta_hora = datetime.timedelta(hours=0)
delta_dia = datetime.timedelta(hours=24)
num_dias = args.PRAZO_H // 24
    
print("\n" + "=" * 60)
print(f"PROCESSAMENTO DE {num_dias} PERIODOS DE 24 HORAS")
print("=" * 60)
    
  
pares_arquivos = []

# Loop para cada periodo de 24 horas
for i in range(num_dias):
    data_inicial_acumulo = data_inicio_base + (delta_dia * i) + (delta_hora * (i+1))
    data_final_acumulo = data_inicial_acumulo + delta_dia
    Fct=f"{((i+1)*24):03d}"   

    # Formato de data/hora esperado no nome do arquivo (YYYYMMDDHH)
    formato_data = '%Y%m%d%H'
    data_str_i = data_inicial_acumulo.strftime(formato_data)
    data_str_e = data_final_acumulo.strftime(formato_data)
    
# Montando nome dos arquivos
#    CAMINHO_BASE = "/lustre/projetos/monan_adm/monan/ecf_PREOPER/MONAN-WorkFlow-OPER/MONAN_PRE_OPER/MONAN/scripts_CD-CT/dataout/"
    CAMINHO_BASE = "/lustre/projetos/monan_adm/monan/ecf_PREOPER/MONAN-WorkFlow-OPER/MONAN_PRE_OPER/MONAN/scripts_CD-CT/dataout/flushout/"
    DIR_DATA = f"{data_inicial}/"
    PREFIXO_ARQ  = "MONAN_DIAG_G_POS_GFS_"
    SUFIXO_ARQ   = ".00.00.x5898242L55.nc" 
    nome_arquivo_i = f"{PREFIXO_ARQ}{data_inicial}_{data_str_i}{SUFIXO_ARQ}"
    nome_arquivo_e = f"{PREFIXO_ARQ}{data_inicial}_{data_str_e}{SUFIXO_ARQ}"
    
    # Monta o caminho completo
    caminho_completo_i = os.path.join(CAMINHO_BASE, DIR_DATA, nome_arquivo_i)
    caminho_completo_e = os.path.join(CAMINHO_BASE, DIR_DATA, nome_arquivo_e)

    pares_arquivos.append((caminho_completo_i, caminho_completo_e))

    # Imprimindo as datas de acumulo
    print(f"--- Acumulado {i+1} --- Previsao {Fct}h ---")
    print(f"Data Inicial: {data_inicial_acumulo.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Data Final:   {data_final_acumulo.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Arquivo I: {caminho_completo_i}")
    print(f"Arquivo E: {caminho_completo_e}")
    
    print("=" * 60)
        
# Caminho dos arquivos (MONAN)
    arquivoi = caminho_completo_i
    arquivoe = caminho_completo_e
#    print(arquivoi)
#    print(arquivoe)

# Inicializa variaveis de referencia
    precip_soma = None
    lat = lon = None

    fi = xr.open_dataset(arquivoi, engine="netcdf4")
    fe = xr.open_dataset(arquivoe, engine="netcdf4")
