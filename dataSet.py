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

# Grab content from URL (Pegar conteúdo HTML a partir da URL)
##url = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2021"
datasetTicket = pd.read_csv('AnnualTicketSales.csv' )
datasetTicket.describe()
datasetDistri = pd.read_csv('TopDistributors.csv')
datasetDistri.describe()
option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

""" driver.get(dfSkoob)
driver.get(dfSkoob2)
driver.implicitly_wait(10)

element = driver.find_element_by_xpath("//div//table")
html_content = element.get_attribute("outerHTML")

# Parse HTML (Parsear o conteúdo HTML) - BeaultifulSoup
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find(name="table")

# Data Structure Conversion (Estruturar conteúdo em um Data Frame) - Pandas
df_full = pd.read_html(str(table))[0]
df = df_full[["Posição", "PTS", "V", "E", "D", "%"]]
df.columns = ["time", "pontos", "vitorias", "empates", "derrotas", "%"]

tabelaFinal = {}
tabelaFinal = df.to_dict("records")

driver.quit()"""

"""js = json.dumps(tabelaFinal)
fp = open("tabela.json", "w")
fp.write(js)
fp.close()

dfSkoob = pd.read_json("./tabela.json")
# mostra quantidade de amostras
# mostra quantidade de colunas
# mostra os nomes das colunas """
print("*************************************************************************")
print(f"Número de amostras: {datasetTicket.shape[0]}")
print(f"Número de colunas: {datasetTicket.shape[1]}")
print(f"Nomes das colunas: {datasetTicket.columns.values}")
print(f"Tipo de dados: {datasetTicket.info()}")
print(f"Número de amostras: {datasetDistri.shape[0]}")
print(f"Número de colunas: {datasetDistri.shape[1]}")
print(f"Nomes das colunas: {datasetDistri.columns.values}")
print(f"Tipo de dados: {datasetDistri.info()}")

print("*************************************************************************")

anos = datasetTicket["YEAR"].values
senhasVendidas = datasetTicket["TICKETS SOLD"]

"""dados = dfSkoob["%"].values[:5]
pontos = dfSkoob["pontos"].values[:5]
vitorias = dfSkoob["vitorias"].values[:5]
derrota = dfSkoob["derrotas"].values[:5]
print("*************************************************************************")
dados = dfSkoob["%"].values[:5]
pontos = dfSkoob["pontos"].values[:5]
vitorias = dfSkoob["vitorias"].values[:5]
derrota = dfSkoob["derrotas"].values[:5]"""



df = pd.DataFrame(
    {
       "senhas vendidas" :senhasVendidas,
       "anos": anos 
    },
    
)
ax = df.plot.bar(X='senhasVendidas',y='anos', title="Crecimento de vendas de senhas")
plt.show()
"""
dadosRebaixados = dfSkoob["%"].values[-4:]
pontosRebaixados = dfSkoob["pontos"].values[-4:]
vitoriasRebaixados = dfSkoob["vitorias"].values[-4:]
derrotaRebaixados = dfSkoob["derrotas"].values[-4:]

indexRebaixados = ["Grêmio", "Bahia", "Sport", "Chapecoense"]
dfRebaixados = pd.DataFrame(
    {
        "pontos": dadosRebaixados,
        "aproveitamento": pontosRebaixados,
        "vitorias": vitoriasRebaixados,
        "derrota": derrotaRebaixados,
    },
    index=indexRebaixados,
)
fig = dfRebaixados.plot.bar(rot=0, title="Times Rebaixados")"""

