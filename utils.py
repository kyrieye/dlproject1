import requests
import pandas as pd
import logging

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
    return data_gdp, data_popu

