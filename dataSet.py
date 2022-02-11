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
apuradonovo = []
for x in apurado:
    x = x.replace(",", "")
    x = x.replace("$", "")
    apuradonovo.append(int(x, base=10))

df = pd.DataFrame(
    {"anos": anos, "apurado": apuradonovo},
)
ax = df.plot.bar(x="anos", y="apurado", title="Crecimento de vendas de senhas", rot=0)
plt.show()
