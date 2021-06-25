'''
MIT License

Copyright (c) 2020 Sebastian Cornejo
             in collaboration with Faviola Molina from dLab - Fundación Ciencia y Vida

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
Los productos que salen del las nuevas definiciones son:
37
"""

import pandas as pd


def prod74(fte,producto):
    print('Generando producto 74')
    df = pd.read_csv(fte)


    identifiers = ['codigo_region', 'region_residencia','codigo_comuna','comuna_residencia','zona']
    variables = [x for x in df.columns if x not in identifiers]
    var_aux = [x for x in df.columns if x not in identifiers]
    sorted_columns = identifiers + var_aux
    df = df[sorted_columns]
    df[variables] = df[variables].fillna(0).astype(int)
    df.to_csv(producto + '.csv', index=False)


    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    #print(df_t)

    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha', value_name='Paso')
    df_std['Paso'] = df_std['Paso'].fillna(0).astype(int)
    #print(df_std)
    df_std.to_csv(producto + '_std.csv', index=False)

if __name__ == '__main__':

    prod74('../input/Paso_a_paso/paso_a_paso.csv', '../output/producto74/paso_a_paso')