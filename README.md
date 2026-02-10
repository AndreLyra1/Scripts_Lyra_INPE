# Scripts_Lyra_INPE

## Linguagens
 - Python
 - Shell script
 - CDO
 
## Autor
Andr� Lyra

Scripts para processamento, plotagem, verifica��o e avalia��o de precipita��o de 24 horas do modelo MONAN,
incluindo compara��es com GPM IMERG, GSMAP e MSWEP.
O fluxo inclui geração de acumulados, cálculo de métricas contínuas e categóricas, geração de figuras e salvamento de produtos intermediários em NetCDF e TXT.

## Visão Geral do Fluxo de Execução:

1. Geração dos acumulados de precipitação 24h do MONAN  
	MONAN_nc_24h_acum_newcolorbar.py

2. Cálculo do Bias MONAN vs observações  
	Bias_MONAN_x_GPM_x_GSMAP_x_MSWEP.py

3. Cálculo do MAE e RMSE MONAN vs observações  
	RMSE_MONAN_x_GPM_x_GSMAP_x_MSWEP.py

4. Cálculo de Skill Scores binários para limiares de precipitação  
	Skill_score_MONAN_x_GPM_x_GSMAP_x_MSWEP.py

5. Processamento mensal por meio de scripts Shell e CDO 
	Gera_monthly_mean_Bias.sh
	Gera_monthly_mean_MAE_RMSE.sh
	Gera_monthly_sum_Skill.sh

6. Plotagem dos �ndices mensais   
	Mean_Bias_MONAN_BAM_GFS.py 
	Mean_MAE_MONAN_BAM_GFS.py
	Mean_RMSE_MONAN_BAM_GFS.py
