import pandas as pd
import sqlalchemy as sql
from sqlalchemy.sql.schema import Column
import sqlalchemy.types as type
import os

df = pd.read_csv('./data/metricas_acoes_ucs_tratado.csv', sep=";")
areas_queimadas_uc = pd.read_csv('./data/areas_queimadas_uc.csv', sep=";")
desmatamento_uc = pd.read_csv('./data/desmatamento_ucs.csv')
precipitacao = pd.read_csv('./data/precipitacao_por_ano_mes.csv', sep=";")
indicadores = pd.read_csv('./data/indicadores_min_max_ucs.csv', sep=";")

engine = sql.create_engine('sqlite:///data/database.db', echo=False)

df.to_sql('metricas_acoes_ucs_tratado', con=engine, if_exists='replace')
areas_queimadas_uc.to_sql('areas_queimadas_uc', con=engine, if_exists='replace')
desmatamento_uc.to_sql('desmatamento_uc', con=engine, if_exists='replace')
precipitacao.to_sql('precipitacao_ano_mes', con=engine, if_exists='replace')
indicadores.to_sql('indicadores_ucs', con=engine, if_exists='replace')