'''
MIT License

Copyright (c) 2020 Sebastian Cornejo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
import sys
import pandas as pd
from utils import *
import datetime as dt

def prod51(url, prod):
    print('Generando prod 51')
    df = pd.read_csv(url)


    # drop empty columns
    df.dropna(axis=1, how='all', inplace=True)

    #Standardize column names
    df.columns = map(str.capitalize, df.columns)
    df.columns = df.columns.str.replace('_', ' ')
    df = normalizaNombreCodigoRegionYComuna(df)
    regionName(df)

    #get each week Monday as date
    df['Fecha'] = df['Week'].apply(lambda w: "{}-W{}-1".format(2020 + w//52, w%52))
    df['Fecha'] = pd.to_datetime(df['Fecha'], format="%Y-W%W-%w")

    ## This is the std product
    df.to_csv(prod + '/ISCI_std.csv', index=False)


def prod82(url, prod, output_name):
    print('Generando producto {}'.format(prod))
    df = pd.read_csv(url)
    df.columns = ['region', 'semana', 'paso', 'nom_comuna', 'comuna', 'fecha_inicio', 'fecha_termino', 'var_salidas',
                'var_salidas_cota_inferior', 'var_salidas_cota_superior']
    print(os.listdir('../output/'))
    if not prod in os.listdir('../output/'):
        os.mkdir('../output/{}'.format(prod))
    df.to_csv('../output/{}/{}.csv'.format(prod, output_name), index=False)
    
if __name__ == '__main__':
    url = 'https://matiascerda.carto.com/api/v2/sql?format=CSV&filename=datos-movilidad-isci.csv&q=select%20*%20from%20data_variacion'
    prod51(url, '../output/producto51')
    url = 'https://nodejs.isci.cl/api/visor-movilidad/week'
    prod82(url, 'producto82', 'ISCI_weeks')
    url = 'https://nodejs.isci.cl/api/visor-movilidad/weekend'
    prod82(url, 'producto82', 'ISCI_weekends')
