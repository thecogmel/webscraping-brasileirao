from re import X
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import json

datasetTicket = pd.read_csv("AnnualTicketSales.csv")
datasetTicket.describe()
datasetDistri = pd.read_csv("TopDistributors.csv")
datasetDistri.describe()

""" print("*************************************************************************")
print(f"Número de amostras: {datasetTicket.shape[0]}")
print(f"Número de colunas: {datasetTicket.shape[1]}")
print(f"Nomes das colunas: {datasetTicket.columns.values}")
print(f"Tipo de dados: {datasetTicket.info()}")
print(f"Número de amostras: {datasetDistri.shape[0]}")
print(f"Número de colunas: {datasetDistri.shape[1]}")
print(f"Nomes das colunas: {datasetDistri.columns.values}")
print(f"Tipo de dados: {datasetDistri.info()}")

print("*************************************************************************") """

anos = datasetTicket["YEAR"]
apurado = datasetTicket["TOTAL BOX OFFICE"]

porcentagem = datasetDistri["MARKET SHARE"]
nomes = datasetDistri["DISTRIBUTORS"]

porcentagemFloat = []
for x in porcentagem:
    x = x.replace("%", "")
    porcentagemFloat.append(float(x))

apuradonovo = []
for x in apurado:
    x = x.replace(",", "")
    x = x.replace("$", "")
    apuradonovo.append(int(x, base=10))

profit = []
for x in porcentagemFloat:
    profit.append(round(apuradonovo[0] * (x / 100)))

# data frame do registro dos lucros da indústria cinematográfica


df = pd.DataFrame(
    {"anos": anos, "apurado": apuradonovo},
)
ax = df.plot.bar(x="anos", y="apurado", title="Registro dos lucros 1995-2021", rot=0)

# data frame da distribuição percentual dos lucros por distribuidora de filmes (top 10)

dfPie = pd.DataFrame(
    {"distribuidoras": profit, "radius": profit},
    index=nomes,
)
plot = dfPie.plot.pie(y="distribuidoras")

# data frame do cálculo do faturamento individual no ano de 2020

dfBar = pd.DataFrame(
    {"nomes": nomes, "profit": profit},
)
fx = dfBar.plot.area(x="nomes", title="Valor por distrubuidora", stacked=False)

plt.show()
