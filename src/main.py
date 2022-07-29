import os
from math import sqrt

import pandas as pd
from pandas.api.types import is_string_dtype

import numpy as np

import seaborn as sns

from sklearn.metrics import f1_score, precision_score, recall_score, mean_absolute_error, mean_squared_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

from matplotlib import pyplot as plt


def tratar_dataset(dataset):
    
    for coluna in dataset.columns:
        if is_string_dtype(dataset[coluna]):
            dataset[coluna] = dataset[coluna].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
            dataset[coluna] = dataset[coluna].str.upper()
            
    dataset.columns = map(str.upper, dataset.columns)
    
    return dataset


def localizar_modelo(dataset, lista_estados, dicionario):
    for estado in lista_estados:
        df_modelo_uf = dataset.query('UF == @estado')[["LEADS", "COD_MODELO_VEICULO"]].groupby(by=["COD_MODELO_VEICULO"]).sum().sort_values(by="LEADS", ascending=False).head()
        
        dicionario["UF"].append(estado)

        for indice, (modelo, lead) in enumerate(df_modelo_uf.iterrows()):
            dicionario[f"TOP {indice + 1}"].append([modelo, lead.LEADS])

    return pd.DataFrame(dicionario)
    

def localizar_marca(dataset, lista_estados, dicionario):
    for estado in lista_estados:
        df_marca_uf = dataset.query('UF == @estado')[["LEADS", "COD_MARCA_VEICULO"]].groupby(by=["COD_MARCA_VEICULO"]).sum().sort_values(by="LEADS", ascending=False).head()
        
        dicionario["UF"].append(estado)

        for indice, (marca, lead) in enumerate(df_marca_uf.iterrows()):
            dicionario[f"TOP {indice + 1}"].append([marca, lead.LEADS])

    return pd.DataFrame(dicionario)


pd.options.display.max_columns = None

dataset = pd.read_csv("../datasets/Case 1 - dados.csv", sep=",")

tratar_dataset(dataset)

dataset.fillna(dataset.median(), inplace=True)

dataset[["UF", "CIDADE"]] = dataset["UF_CIDADE"].str.split("_", expand=True)

dataset = dataset[dataset["UF"] != "N/A"]

dataset_modelo = dataset[["LEADS", "COD_MODELO_VEICULO"]].groupby(by=["COD_MODELO_VEICULO"]).sum()

dataset_marca = dataset[["LEADS", "COD_MARCA_VEICULO"]].groupby(by=["COD_MARCA_VEICULO"]).sum()

dataset_uf = dataset[["LEADS", "UF"]].groupby(by=["UF"]).sum()

dataset_cidade = dataset[["LEADS", "CIDADE"]].groupby(by=["CIDADE"]).sum()

df_modelo = {
    "UF": [],
    "TOP 1": [],
    "TOP 2": [],
    "TOP 3": [],
    "TOP 4": [],
    "TOP 5": [],
}

df_marca = {
    "UF": [],
    "TOP 1": [],
    "TOP 2": [],
    "TOP 3": [],
    "TOP 4": [],
    "TOP 5": [],
}

lista_estados = ["SP", "RJ", "MG", "PR", "SC"]

df_modelo = localizar_modelo(dataset, lista_estados, df_modelo)
df_marca = localizar_marca(dataset, lista_estados, df_marca)

dataset["APRESENTA_LEAD"] = np.where(dataset["LEADS"] > 0, 1, 0)

encoder = LabelEncoder()

dataset["UF"] = encoder.fit_transform(dataset["UF"])
dataset["RODASLIGA"] = encoder.fit_transform(dataset["RODASLIGA"])
dataset["ARCONDIC"] = encoder.fit_transform(dataset["ARCONDIC"])
dataset["CAMBIO"] = encoder.fit_transform(dataset["CAMBIO"])

dados_normalizados = dataset[["COD_MODELO_VEICULO", "COD_MARCA_VEICULO"]]
min_max_scaler = MinMaxScaler()
dados_normalizados = min_max_scaler.fit_transform(dados_normalizados)
df = pd.DataFrame(dados_normalizados)

dataset["COD_MODELO_VEICULO"], dataset["COD_MARCA_VEICULO"] = list(zip(*dados_normalizados))

X = dataset[["UF", "COD_MODELO_VEICULO", "COD_MARCA_VEICULO"]]
y = dataset["APRESENTA_LEAD"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

random_forest = RandomForestClassifier(random_state=1)
random_forest.fit(X_train, y_train)
predicao = random_forest.predict(X_test)

recall_forest = recall_score(y_test, predicao)
precisao_forest = precision_score(y_test, predicao)
f1_forest = f1_score(y_test, predicao)

print(recall_decision, precisao_decision, f1_decision)
