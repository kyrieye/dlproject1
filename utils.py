import requests
import pandas as pd
import logging
import requests, time, datetime
import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

logging.captureWarnings(True)


def get_data():
    url = 'https://www.imf.org/external/datamapper//export/excel.php?indicator=NGDPD'
    response = requests.get(url, verify=False)
    open("GDP.xls", 'wb').write(response.content)
    data_gdp = pd.read_excel("GDP.xls")
    url2 = 'https://www.imf.org/external/datamapper//export/excel.php?indicator=LP'
    response = requests.get(url2, verify=False)
    open("Population.xls", 'wb').write(response.content)
    data_popu = pd.read_excel("Population.xls")
    index = data_gdp.columns[0]
    data_gdp.dropna(thresh=1, inplace=True)  # 去空行
    data_gdp.set_index('GDP, current prices (Billions of U.S. dollars)', inplace=True)  # 国家列为索引
    data_gdp.dropna(thresh=1, inplace=True)  # 去最后一行
    for i in data_gdp.columns:
        data_gdp[i].mask(data_gdp[i] == 'no data', np.nan, inplace=True)  # 处理no data
    data_gdp = data_gdp.astype(float).reset_index()  # 数据转为float
    #print(data_gdp)
    index = data_popu.columns[0]
    data_popu.dropna(thresh=1, inplace=True)  # 去空行
    data_popu.set_index('Population (Millions of people)', inplace=True)  # 国家列为索引
    data_popu.dropna(thresh=1, inplace=True)  # 去最后一行
    for i in data_popu.columns:
        data_popu[i].mask(data_popu[i] == 'no data', np.nan, inplace=True)  # 处理no data
    data_popu = data_popu.astype(float).reset_index()  # 数据转为float
    #print(data_popu)
    return data_gdp, data_popu


get_data()
