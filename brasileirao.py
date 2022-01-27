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
url = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2021"

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)
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

driver.quit()

js = json.dumps(tabelaFinal)
fp = open("tabela.json", "w")
fp.write(js)
fp.close()

dfSkoob = pd.read_json("C:/Users/Erick/Documents/GitHub/webscraping/tabela.json")
# mostra quantidade de amostras
# mostra quantidade de colunas
# mostra os nomes das colunas
print("*************************************************************************")
print(f"Número de amostras: {dfSkoob.shape[0]}")
print(f"Número de colunas: {dfSkoob.shape[1]}")
print(f"Nomes das colunas: {dfSkoob.columns.values}")
print("*************************************************************************")

dados = dfSkoob["%"].values[:5]
pontos = dfSkoob["pontos"].values[:5]

index = ["Atlético Mineiro", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians"]
df = pd.DataFrame({"pontos": pontos, "aproveitamento": dados}, index=index)
ax = df.plot.bar(rot=0, title="Times com melhores aproveitamento")

dadosRebaixados = dfSkoob["%"].values[-4:]
pontosRebaixados = dfSkoob["pontos"].values[-4:]

indexRebaixados = ["Grêmio", "Bahia", "Sport", "Chapecoense"]
dfRebaixados = pd.DataFrame(
    {"pontos": dadosRebaixados, "aproveitamento": pontosRebaixados},
    index=indexRebaixados,
)
fig = dfRebaixados.plot.bar(rot=0, title="Times Rebaixados")
plt.show()
