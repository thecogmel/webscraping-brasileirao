import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

import requests

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
df.columns = ["time", "pontos", "Vitorias", "Empates", "Derrotas", "%"]

tabelaFinal = {}
tabelaFinal["ranking"] = df.to_dict("records")

driver.quit()

js = json.dumps(tabelaFinal)
fp = open("tabela.json", "w")
fp.write(js)
fp.close()
