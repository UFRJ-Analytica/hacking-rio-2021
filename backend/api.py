# Imports
from flask import (
    Flask,
    request
)
import sqlalchemy as sql
from random import randint, sample
import pandas as pd
from sqlalchemy.sql.schema import Column
from flask_cors import CORS
import json
import numpy as np
import os




# App & Server settings
server = Flask(__name__)
CORS(server)


# Connects to the database
engine = sql.create_engine('sqlite:///data/database.db', echo=False)
#metadata = sql.MetaData()


# metadata.create_all(engine)

# Routes

@server.route('/')
def home():

    return "Coe, broder"


@server.route('/pop', methods=["GET"])
@server.route('/pop/<limit>', methods=["GET"])
def populacao(limit=100):
    # /pop?year=<ano>
    # ex.: /pop?year=2020&limit=10

    year = request.args.get('year')

    query = f"""
        SELECT 
            id_municipio,
            populacao 
        FROM populacao 
        WHERE ano == {year} 
        ORDER BY populacao DESC
        LIMIT {limit}
    """

    response_tuples = []
    table_keys = []

    with engine.connect() as connection:
        result = connection.execute(query)
        #print(result)
        table_keys = result.keys()
        for row in result:
            response_tuples.append(row) 
    return {
        "x": [id_mu for id_mu, _ in response_tuples],
        "y": [pop for _, pop in response_tuples],
        "type": 'bar'
    }

@server.route('/getUCS', methods=["GET"])
def getUCS():

    query = f"""
        SELECT 
            nome_da_uc
        FROM metricas_acoes_ucs_tratado 
    """

    ucs = []

    with engine.connect() as connection:
        result = connection.execute(query)
        #print(result)
        table_keys = result.keys()
        for row in result:
            ucs.append(row[0]) 
    return {
        "ucs_names": ucs
    }


@server.route('/getIndicators', methods=["GET"])
def getIndicators():
    indicadores = pd.read_csv("data/indicadores_min_max_ucs.csv", sep=";")
    indicadores = indicadores.fillna(-1)
    return {
        "uc_names":  indicadores["nome_da_uc"].tolist() ,
        "indicadores": indicadores["indicador_falso_positivo_min_max"].tolist() 
    }

@server.route('/generateRandomData', methods=["GET"])
def generateRandomData():
    geojson = json.load(open('data\\ucs.json'))

    z = {}

    locations = [e['properties']['nome'] for e in geojson['features']]
    codigos = [e['properties']['codigoCnuc'] for e in geojson['features']]

    query = f"""
        SELECT 
            codigo_da_uc, indicador_falso_positivo_min_max
        FROM indicadores_ucs
        WHERE codigo_da_uc IN ({str(codigos)[1:-1]})
    """

    with engine.connect() as connection:
        result = connection.execute(query)
        for row in result:
            z[row[0]] = row[1]


    result = np.array([z[cnuc] if cnuc in z.keys() else 'Dados Insuficientes' for cnuc in codigos], dtype='object')


    return {
        "type": "choroplethmapbox",
        "locations": locations,
        "colorscale": 'Hot',
        "z": list(result),
        "featureidkey": "properties.nome",
        "geojson": geojson
    }

@server.route('/getQueimadasData', methods=["GET"])
def getQueimadasData():

    uc = request.args.get('uc')
    cnuc = ''
    queimadas = []

    query = f"""
        SELECT 
            cnuc
        FROM metricas_acoes_ucs_tratado
        WHERE  nome_da_uc == '{uc}'
    """
    with engine.connect() as connection:
        result = connection.execute(query)
        for row in result:
            cnuc = row[0]

    query2 = f"""
        SELECT 
            area_queimada_em_2019,
            area_queimada_em_2018,
            area_queimada_em_2017,
            area_queimada_em_2016,
            area_queimada_em_2015,
            area_queimada_em_2014,
            area_queimada_em_2013,
            area_queimada_em_2012
        FROM areas_queimadas_uc
        WHERE codigo_cnuc == '{cnuc}'
    """

    with engine.connect() as connection:
        result = connection.execute(query2)
        for row in result:
            queimadas = row

    print([float(i) if i is not None else 0 for i in queimadas])
    return {
        "type": "bar",
        "y": [float(i) if i is not None else 0 for i in queimadas],
        "x": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    }

@server.route('/getPrecipitacao', methods=["GET"])
def getPrecipitacao():
    cod_uc = request.args.get('cod_uc')
    ano = request.args.get('ano')

    query = f"""
        SELECT 
            `cod_uc`,
            `uc`,
            `mes`,
            `precipitacao_(mm)` as precipitacao 
        FROM precipitacao_ano_mes WHERE `cod_uc` = "{cod_uc}" AND ano = {ano} ORDER BY `ano_mes` ASC
    """

    dados = []

    with engine.connect() as connection:
        result = connection.execute(query)
        #print(result)
        table_keys = result.keys()
        for row in result:
            dados.append(row) 
    
    return {
        "type": "lineplot",
        "x": [row[2] for row in dados],
        "y": [row[3] for row in dados]
    }

@server.route('/management_metrics', methods=["GET"])
def management():
    uc = request.args.get('uc')
    query = f"""
        SELECT 
            nota_pessoal_mean,
            nota_equipamento_mean,
            nota_capacidade_mean,
            nota_recurso_mean,
            nota_apoio_mean,
            calculo_efetividade_mean

        FROM metricas_acoes_ucs_tratado 
        WHERE nome_da_uc = "{uc}"
    """

  
    with engine.connect() as connection:
        result = connection.execute(query)
        data = result.fetchone()

    data = [round(100*d, 2) for d in data]
    return {
        "uc": uc,
        "nota_pessoal_mean": data[0],
        "nota_equipamento_mean":  data[1],
        "nota_capacidade_mean":  data[2],
        "nota_recurso_mean":  data[3],
        "nota_apoio_mean":  data[4],
        "calculo_efetividade_mean":  data[5]
    
    }







@server.route('/getDesmatamentoData', methods=["GET"])
def getDesmatamentoData():
    uc = request.args.get('uc')
    df = pd.read_csv("data/desmatamento_ucs.csv", sep=';')
    df = df.fillna(0)
    x = list(range(2001, 2021))
    years = [str(year) for year in x]
    y = []
    for year in years:
        values = df.loc[df["nome_da_uc"] == uc, year].values
        if len(values) > 0:
            y.append( df.loc[df["nome_da_uc"] == uc, year].values[0])
        else:
            x = []
            y = []
    print(x, y)
    Line_Chart = {
        "x": x,
        "y": y,
        "type": 'scatter'
    }

    Bar_Chart = {
        "x": x,
        "y": y,
        "type": 'bar'
    }
    return {
        "Line Chart": Line_Chart,
        "Bar Chart": Bar_Chart
    }
