'''
MIT License

Copyright (c) 2020 Faviola Molina - dLab - Fundación Ciencia y Vida

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

"""
Los productos que salen del informe de testeo y trazabilidad son:

"""

import pandas as pd
import numpy as np

def prod63_64_65_66_67(fte, producto):
    df = pd.read_csv(fte, dtype={'Codigo region': object, 'Codigo comuna': object})
    df.dropna(how='all', inplace=True)
    df.to_csv(producto + '.csv', index=False)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion']
    variables = [x for x in df.columns if x not in identifiers]
    if '63' in producto:
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                         value_name='Numero notificaciones')
    elif '64' in producto:
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                         value_name='BAC')
    elif '65' in producto:
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                         value_name='Positividad')
    elif '66' in producto:
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                         value_name='Cobertura testeo')
    elif '67' in producto:
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                         value_name='Oportunidad notificacion')
    df_std.to_csv(producto + '_std.csv', index=False)

if __name__ == '__main__':

    print('Generando producto 63')
    prod63_64_65_66_67('../input/InformeTesteoTrazabilidad/NNotificacionPorComuna.csv', '../output/producto63/NNotificacionPorComuna')
    print('Generando producto 64')
    prod63_64_65_66_67('../input/InformeTesteoTrazabilidad/BACPorComuna.csv', '../output/producto64/BACPorComuna')
    print('Generando producto 65')
    prod63_64_65_66_67('../input/InformeTesteoTrazabilidad/PositividadPorComuna.csv', '../output/producto65/PositividadPorComuna')
    print('Generando producto 66')
    prod63_64_65_66_67('../input/InformeTesteoTrazabilidad/CoberturaPorComuna.csv', '../output/producto66/CoberturaPorComuna')
    print('Generando producto 67')
    prod63_64_65_66_67('../input/InformeTesteoTrazabilidad/OportunidadPorComuna.csv', '../output/producto67/OportunidadPorComuna')
