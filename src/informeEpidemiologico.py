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
Los productos que salen del informe epidemiologico son:
1
2
6
15
16
18
19
21
22
25
28
34
35
38
39
45
"""

import utils
import pandas as pd
from shutil import copyfile
import glob
import re
import numpy as np
from utils import *


def prod1(fte, producto):
    # Generando producto 1
    print('Generando producto 1')
    df = pd.read_csv(fte, dtype={'Codigo region': object, 'Codigo comuna': object})
    df.dropna(how='all', inplace=True)
    utils.regionName(df)
    # Drop filas de totales por region
    todrop = df.loc[df['Comuna'] == 'Total']
    df.drop(todrop.index, inplace=True)
    df.to_csv(producto + '.csv', index=False)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion']
    variables = [x for x in df.columns if x not in identifiers]
    variables.remove('Tasa')
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha', value_name='Casos confirmados')
    df_std.to_csv(producto + '_std.csv', index=False)


def prod2(fte, producto):
    print('Generando producto 2')
    df = pd.read_csv(fte, dtype={'Codigo region': object, 'Codigo comuna': object})
    df.dropna(how='all', inplace=True)
    utils.regionName(df)
    # Drop filas de totales por region
    todrop = df.loc[df['Comuna'] == 'Total']
    df.drop(todrop.index, inplace=True)
    # print(df.columns)
    dates = []
    for eachColumn in df.columns:
        if '2020' in eachColumn:
            dates.append(eachColumn)
        if '2021' in eachColumn:
            dates.append(eachColumn)
    # print('las fechas son ' + str(dates))
    for eachdate in dates:
        filename = eachdate + '-CasosConfirmados.csv'
        print('escribiendo archivo ' + filename)
        aux = df[['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion', eachdate]]
        aux.rename(columns={eachdate: 'Casos Confirmados'}, inplace=True)
        aux.to_csv(producto + filename, index=False)


def prod15(fte, prod):
    data_2020 = []
    data_2021 = []
    for file in glob.glob(fte + '/*FechaInicioSintomas.csv'):
        print(file)
        if file != fte + 'FechaInicioSintomas.csv':
            date = re.search("\d{4}-\d{2}-\d{2}", file).group(0)
            if '2020' in date:
                df = pd.read_csv(file, sep=",", encoding="utf-8", dtype={'Codigo region': object, 'Codigo comuna': object})
                df.dropna(how='all', inplace=True)
                # Drop filas de totales por region
                todrop = df.loc[df['Comuna'] == 'Total']
                df.drop(todrop.index, inplace=True)
                # Hay semanas epi que se llam S en vez de SE
                for eachColumn in list(df):
                    if re.search("S\d{2}", eachColumn):
                        print("Bad name " + eachColumn)
                        df.rename(columns={eachColumn: eachColumn.replace('S', 'SE')}, inplace=True)
                # insert publicacion as column 5
                # df['Publicacion'] = date
                df.insert(loc=5, column='Publicacion', value=date)
                data_2020.append(df)
            else:
                df = pd.read_csv(file, sep=",", encoding="utf-8",
                                 dtype={'Codigo region': object, 'Codigo comuna': object})
                df.dropna(how='all', inplace=True)
                # Drop filas de totales por region
                todrop = df.loc[df['Comuna'] == 'Total']
                df.drop(todrop.index, inplace=True)
                # Hay semanas epi que se llam S en vez de SE
                for eachColumn in list(df):
                    if re.search("S\d{2}", eachColumn):
                        print("Bad name " + eachColumn)
                        df.rename(columns={eachColumn: eachColumn.replace('S', 'SE')}, inplace=True)
                # insert publicacion as column 5
                # df['Publicacion'] = date
                df.insert(loc=5, column='Publicacion', value=date)
                data_2021.append(df)
            

    # normalization 2020
    data_2020 = pd.concat(data_2020)
    data_2020 = data_2020.fillna(0)
    utils.regionName(data_2020)
    data_2020.sort_values(['Publicacion', 'Region'], ascending=[True, True], inplace=True)
    data_2020.to_csv(prod + '_2020.csv', index=False)
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion', 'Publicacion']
    variables = [x for x in data_2020.columns if x not in identifiers]
    df_std = pd.melt(data_2020, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica',
                     value_name='Casos confirmados')
    df_std.to_csv(prod + '_2020_std.csv', index=False)

    # normalization 2021
    data_2021 = pd.concat(data_2021)
    data_2021 = data_2021.fillna(0)
    utils.regionName(data_2021)
    data_2021.sort_values(['Publicacion', 'Region'], ascending=[True, True], inplace=True)
    data_2021.to_csv(prod + '_2021.csv', index=False)
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion', 'Publicacion']
    variables = [x for x in data_2021.columns if x not in identifiers]
    df_std = pd.melt(data_2021, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica',
                     value_name='Casos confirmados')
    df_std.to_csv(prod + '_2021_std.csv', index=False)
    
    # create old prod 15 from latest adition
    copyfile('../input/InformeEpidemiologico/SemanasEpidemiologicas.csv',
             '../output/producto15/SemanasEpidemiologicas.csv')

    latest = max(data_2021['Publicacion'])
    print(latest)
    latestdf = data_2021.loc[data_2021['Publicacion'] == latest]
    # print(latestdf)
    latestdf.drop(['Publicacion'], axis=1, inplace=True)
    latestdf.to_csv(prod.replace('Historico', '.csv'), index=False)

    df_t = latestdf.T
    df_t.to_csv(prod.replace('Historico', '_T.csv'), header=False)

    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion']
    variables = [x for x in latestdf.columns if x not in identifiers]
    df_std = pd.melt(latestdf, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica',
                     value_name='Casos confirmados')
    df_std.to_csv(prod.replace('Historico', '_std.csv'), index=False)


def prod16(fte, producto):
    print('Generando producto 16')
    copyfile(fte, producto + '.csv')
    df2_t = utils.transpone_csv(producto + '.csv')
    df2_t.to_csv(producto + '_T.csv', header=False)
    df = pd.read_csv(fte)
    identifiers = ['Grupo de edad', 'Sexo']
    variables = [x for x in df.columns if x not in identifiers]
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                     value_name='Casos confirmados')
    df_std.to_csv(producto + '_std.csv', index=False)

def prod16_etapa_clinica(fte, producto):
    print('Generando producto 16, con etapas clinicas')

    df = pd.read_csv(fte)
    df.to_csv(producto + '.csv', index=False)

    df_T = df.T
    df_T.to_csv(producto + '_t.csv', index=False)

    identifiers = ['Grupo de edad', 'Sexo', 'Etapa clinica']
    variables = [x for x in df.columns if x not in identifiers]
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                     value_name='Casos confirmados')
    df_std.to_csv(producto + '_std.csv', header=False)

def prod18(fte, producto):
    df = pd.read_csv(fte, dtype={'Codigo region': object, 'Codigo comuna': object})
    df.dropna(how='all', inplace=True)
    df.to_csv(producto + '.csv', index=False)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion']
    variables = [x for x in df.columns if x not in identifiers]
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                     value_name='Tasa de incidencia')
    df_std.to_csv(producto + '_std.csv', index=False)


def prod19_25_38(fte, producto):
    df = pd.read_csv(fte, dtype={'Codigo region': object, 'Codigo comuna': object})
    df.dropna(how='all', inplace=True)
    df.to_csv(producto + '.csv', index=False)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion']
    variables = [x for x in df.columns if x not in identifiers]
    if '19' in producto:
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                         value_name='Casos activos')
    elif '25' in producto:
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                         value_name='Casos actuales')
    elif '38' in producto:
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                         value_name='Casos fallecidos')
    df_std.to_csv(producto + '_std.csv', index=False)


def prod21_22(fte, producto):
    HospitalizadosEtario_T = utils.transpone_csv(producto + '.csv')
    HospitalizadosEtario_T.to_csv(producto + '_T.csv', header=False)
    df = pd.read_csv(fte)
    df = df.replace('-', '', regex=True)
    df.to_csv(producto + '.csv', index=False)
    if '21' in producto:
        print('prod21')
        identifiers = ['Sintomas']
        variables = [x for x in df.columns if x not in identifiers]
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='fecha', value_name='numero')
        df_std.to_csv(producto + '_std.csv', index=False)
    if '22' in producto:
        print('prod22')
        if 'Sexo' in df.columns:
            identifiers = ['Grupo de edad', 'Sexo']
        else:
            identifiers = ['Grupo de edad']
        variables = [x for x in df.columns if x not in identifiers]
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='fecha', value_name='numero')
        df_std.to_csv(producto + '_std.csv', index=False)


def prod21Nuevo(fte, producto):
    df = pd.read_csv(fte)
    df = df.replace('-', '', regex=True)
    df.to_csv(producto + '.csv', index=False)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    print('prod21Nuevo')
    identifiers = ['Sintomas', 'Hospitalización']
    variables = [x for x in df.columns if x not in identifiers]
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='fecha', value_name='numero')
    df_std.to_csv(producto + '_std.csv', index=False)


def prod28(fte, prod):
    data = []
    for file in glob.glob(fte + '/*FechaInicioSintomas_reportadosSEREMI.csv'):
        if file != fte + 'FechaInicioSintomas_reportadosSEREMI.csv':
            date = re.search("\d{4}-\d{2}-\d{2}", file).group(0)
            print("reading " + file)
            df = pd.read_csv(file, sep=",", encoding="utf-8", dtype={'Codigo region': object})
            df.dropna(how='all', inplace=True)

            # Hay semanas epi que se llam S en vez de SE
            for eachColumn in list(df):
                if re.search("S\d{2}", eachColumn):
                    print("Bad name " + eachColumn)
                    df.rename(columns={eachColumn: eachColumn.replace('S', 'SE')}, inplace=True)
            # insert publicacion as column 5
            # df['Publicacion'] = date
            df.insert(loc=2, column='Publicacion', value=date)
            data.append(df)

    # normalization
    data = pd.concat(data)
    data = data.fillna(0)

    if 'SEREMI notificacion' in (data.columns):
        data.rename(columns={'SEREMI notificacion': 'Region'}, inplace=True)
    # print(list(data))
    utils.regionName(data)
    data.to_csv(prod + '.csv', index=False)
    identifiers = ['Region', 'Codigo region', 'Publicacion']
    variables = [x for x in data.columns if x not in identifiers]
    df_std = pd.melt(data, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica',
                     value_name='Casos confirmados')
    df_std.to_csv(prod + '_std.csv', index=False)

    # create old prod 15 from latest adition
    latest = max(data['Publicacion'])
    print(latest)
    latestdf = data.loc[data['Publicacion'] == latest]

    latestdf.drop(['Publicacion'], axis=1, inplace=True)
    latestdf.to_csv(prod.replace('Historico', '.csv'), index=False)

    df_t = latestdf.T
    df_t.to_csv(prod.replace('Historico', '_T.csv'), header=False)

    identifiers = ['Region', 'Codigo region']
    variables = [x for x in latestdf.columns if x not in identifiers]
    df_std = pd.melt(latestdf, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica',
                     value_name='Casos confirmados')
    df_std.to_csv(prod.replace('Historico', '_std.csv'), index=False)


def prod35(fte, producto):
    df = pd.read_csv(fte)

    identifiers = ['Comorbilidad', 'Hospitalización']
    variables = [x for x in df.columns if x not in identifiers]

    NumSHosp = df.loc[df['Comorbilidad'] == 'Número Casos sin Hospitalización', variables]
    NumHosp = df.loc[df['Comorbilidad'] == 'Número Casos Hospitalizados', variables]

    idxNum = NumSHosp.columns.get_loc('2020-06-12')
    NumeroSinHosp = NumSHosp.iloc[0][NumSHosp.columns[0:idxNum]]
    NumeroHosp = NumHosp.iloc[0][NumHosp.columns[0:idxNum]]

    todrop = df.loc[df['Comorbilidad'] == 'Número Casos sin Hospitalización']
    df.drop(todrop.index, inplace=True)
    todrop = df.loc[df['Comorbilidad'] == 'Número Casos Hospitalizados']
    df.drop(todrop.index, inplace=True)

    idx = df.columns.get_loc('2020-06-12')

    temp1 = round(df.iloc[0:11][df.columns[2:idx]].divide(100) * NumeroSinHosp)
    temp2 = round(df.iloc[11:22][df.columns[2:idx]].divide(100) * NumeroHosp)

    temp3 = df.iloc[0:11][df.columns[idx:]]
    temp4 = df.iloc[11:22][df.columns[idx:]]

    df2 = pd.concat([temp1, temp2], axis=0)
    df2 = pd.concat([df['Comorbilidad'], df['Hospitalización'], df2], axis=1)

    df3 = pd.concat([temp3, temp4], axis=0)
    df3 = pd.concat([df2, df3], axis=1)

    df3.to_csv(producto + '.csv', index=False)

    df3_t = utils.transpone_csv(producto + '.csv')
    df3_t.to_csv(producto + '_T.csv', header=False)

    df_std = pd.melt(df3, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                     value_name='Casos confirmados')
    df_std.to_csv(producto + '_std.csv', index=False)


def prod39(fte, producto):
    copyfile(fte, producto + '.csv')
    df = pd.read_csv(fte)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    identifiers = ['Categoria','Serie']
    variables = [x for x in df.columns if x not in identifiers]
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha', value_name='Casos')
    df_std.to_csv(producto + '_std.csv', index=False)


def prod45(fte, fte2, prod):
    data_2020 = []
    data_2021 = []
    for file in glob.glob(fte + '/*Casos' + fte2 + 'PorComuna.csv'):
        print(file)
        if file != fte + 'Casos' + fte2 + 'PorComuna.csv':
            date = re.search("\d{4}-\d{2}-\d{2}", file).group(0)
            if '2020' in date:
                df = pd.read_csv(file, sep=",", encoding="utf-8", dtype={'Codigo region': object, 'Codigo comuna': object})
                df.dropna(how='all', inplace=True)
                # Drop filas de totales por region
                todrop = df.loc[df['Comuna'] == 'Total']
                df.drop(todrop.index, inplace=True)
                # Hay semanas epi que se llam S en vez de SE
                for eachColumn in list(df):
                    if re.search("S\d{2}", eachColumn):
                        print("Bad name " + eachColumn)
                        df.rename(columns={eachColumn: eachColumn.replace('S', 'SE')}, inplace=True)
                # insert publicacion as column 5
                # df['Publicacion'] = date
                df.insert(loc=5, column='Publicacion', value=date)
                data_2020.append(df)
            else:
                df = pd.read_csv(file, sep=",", encoding="utf-8",
                                 dtype={'Codigo region': object, 'Codigo comuna': object})
                df.dropna(how='all', inplace=True)
                # Drop filas de totales por region
                todrop = df.loc[df['Comuna'] == 'Total']
                df.drop(todrop.index, inplace=True)
                # Hay semanas epi que se llam S en vez de SE
                for eachColumn in list(df):
                    if re.search("S\d{2}", eachColumn):
                        print("Bad name " + eachColumn)
                        df.rename(columns={eachColumn: eachColumn.replace('S', 'SE')}, inplace=True)
                # insert publicacion as column 5
                # df['Publicacion'] = date
                df.insert(loc=5, column='Publicacion', value=date)
                data_2021.append(df)
                
    name = fte2.lower()

    if name == 'nonotificados':
        name = 'no notificados'

    # normalization 2020
    data_2020 = pd.concat(data_2020)
    data_2020 = data_2020.fillna(0)
    utils.regionName(data_2020)
    data_2020.sort_values(['Publicacion', 'Region'], ascending=[True, True], inplace=True)
    data_2020.to_csv(prod + '_2020.csv', index=False)
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion', 'Publicacion']
    variables = [x for x in data_2020.columns if x not in identifiers]
    df_std = pd.melt(data_2020, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica',
                     value_name='Casos ' + name)
    df_std.to_csv(prod + '_2020_std.csv', index=False)

    # normalization 2021
    data_2021 = pd.concat(data_2021)
    data_2021 = data_2021.fillna(0)
    utils.regionName(data_2021)
    data_2021.sort_values(['Publicacion', 'Region'], ascending=[True, True], inplace=True)
    data_2021.to_csv(prod + '_2021.csv', index=False)
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion', 'Publicacion']
    variables = [x for x in data_2021.columns if x not in identifiers]
    df_std = pd.melt(data_2021, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica',
                     value_name='Casos ' + name)
    df_std.to_csv(prod + '_2021_std.csv', index=False)

    copyfile('../input/InformeEpidemiologico/SemanasEpidemiologicas.csv',
             '../output/producto45/SemanasEpidemiologicas.csv')

    # create old prod 45 from latest adition
    latest = max(data_2021['Publicacion'])
    print(latest)
    latestdf = data_2021.loc[data_2021['Publicacion'] == latest]
    # print(latestdf)
    latestdf.drop(['Publicacion'], axis=1, inplace=True)
    latestdf.to_csv(prod.replace('Historico', '.csv'), index=False)

    df_t = latestdf.T
    df_t.to_csv(prod.replace('Historico', '_T.csv'), header=False)

    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion']
    variables = [x for x in latestdf.columns if x not in identifiers]
    df_std = pd.melt(latestdf, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica',
                     value_name='Casos ' + name)
    df_std.to_csv(prod.replace('Historico', '_std.csv'), index=False)

def prod57(fte, prod):
    print("Generando producto 57")
    df = pd.read_csv(fte, encoding='utf-8')

    df.rename(columns={'fecha_fallecimiento': 'Fecha',
                       'region_residencia': 'Region',
                       'hospitalizacion': 'Hospitalizacion'},
              inplace=True)

    regionNameRegex(df)
    regionName(df)
    df['Region'] = df['Region'].str.strip()
    df.to_csv(prod + '.csv', index=False)

    df2 = pd.read_csv(prod + '.csv')
    identifiers = ['Fecha', 'Region', 'Hospitalizacion']
    variables = [x for x in df2.columns if x not in identifiers]
    identifiers.append('Publicacion')

    df_std = pd.DataFrame()
    i = 0
    for publicacion in variables:
        temp = pd.DataFrame()
        temp['Publicacion'] = pd.Series([publicacion]*len(df2[publicacion]))
        temp['Fecha'] = df2['Fecha'].copy()
        temp['Region'] = df2['Region'].copy()
        temp['Hospitalizacion'] = df2['Hospitalizacion'].copy()
        temp['Fallecidos'] = df2[publicacion].copy()

        dates_rep = temp['Fecha'].unique()
        flag = 0
        for day in dates_rep:
            if flag == 0:
                if day > publicacion:
                    print(day,publicacion)
                    flag = 1
                    todrop = temp.loc[temp['Fecha'] > publicacion]
                    temp.drop(todrop.index, inplace = True)

        if i == 0:
            df_std = temp.copy()
            i += 1
        else:
            df_std = pd.concat([df_std, temp], axis = 0)

    df_std.to_csv(prod + '_std.csv', index=False)


def prod59_60_62(fte, prod):
    print("Generando producto 59, 60, 62")
    df = pd.read_csv(fte, encoding='utf-8')
    df.to_csv(prod + '.csv', index=False)

def prod61(fte, prod):
    print("Generando producto 61")
    df = pd.read_csv(fte, encoding='utf-8')

    df.rename(columns={'comuna': 'Comuna',
                       'cie_10': 'CIE 10',
                       'casos': 'Casos',
                       'region': 'Region'},
              inplace=True)

    regionNameRegex(df)
    regionName(df)
    df['Region'] = df['Region'].str.strip()
    df.to_csv(prod + '.csv', index=False)



if __name__ == '__main__':
    prod1('../input/InformeEpidemiologico/CasosAcumuladosPorComuna.csv', '../output/producto1/Covid-19')

    prod2('../input/InformeEpidemiologico/CasosAcumuladosPorComuna.csv', '../output/producto2/')

    print('Generando producto 6')
    exec(open('bulk_producto2.py').read())

    print('Generando producto 15')
    prod15('../input/InformeEpidemiologico/', '../output/producto15/FechaInicioSintomasHistorico')

    prod16('../input/InformeEpidemiologico/CasosGeneroEtario.csv', '../output/producto16/CasosGeneroEtario')

    prod16_etapa_clinica('../input/InformeEpidemiologico/CasosGeneroEtarioEtapaClinica.csv', '../output/producto16/CasosGeneroEtarioEtapaClinica')

    print('Generando producto 18')
    prod18('../input/InformeEpidemiologico/TasaDeIncidencia.csv', '../output/producto18/TasaDeIncidencia')

    print('Generando producto 19')
    prod19_25_38('../input/InformeEpidemiologico/CasosActivosPorComuna.csv',
                 '../output/producto19/CasosActivosPorComuna')

    print('Generando producto 21')
    prod21_22('../input/InformeEpidemiologico/SintomasCasosConfirmados.csv',
              '../output/producto21/SintomasCasosConfirmados')
    prod21_22('../input/InformeEpidemiologico/SintomasHospitalizados.csv',
              '../output/producto21/SintomasHospitalizados')
    prod21Nuevo('../input/InformeEpidemiologico/Sintomas.csv', '../output/producto21/Sintomas')

    print('Generando producto 22')
    prod21_22('../input/InformeEpidemiologico/HospitalizadosGeneroEtario_Acumulado.csv',
              '../output/producto22/HospitalizadosEtario_Acumulado')
    prod21_22('../input/InformeEpidemiologico/HospitalizadosUCI_Acumulado.csv',
              '../output/producto22/HospitalizadosUCI_Acumulado')

    print('Generando producto 25')
    prod19_25_38('../input/InformeEpidemiologico/CasosActualesPorComuna.csv',
                 '../output/producto25/CasosActualesPorComuna')

    print('Generando producto 28')
    prod28('../input/InformeEpidemiologico/', '../output/producto28/FechaInicioSintomas_reportadosSEREMIHistorico')

    print('Generando producto 35')
    prod35('../input/InformeEpidemiologico/Comorbilidad.csv', '../output/producto35/Comorbilidad')

    print('Generando producto 38')
    prod19_25_38('../input/InformeEpidemiologico/CasosFallecidosPorComuna.csv',
                 '../output/producto38/CasosFallecidosPorComuna')

    print('Generando producto 39')
    prod39('../input/InformeEpidemiologico/NotificacionInicioSintomas.csv',
           '../output/producto39/NotificacionInicioSintomas')

    print('Generando producto 45')
    prod45('../input/InformeEpidemiologico/', 'Confirmados', '../output/producto45/CasosConfirmadosPorComunaHistorico')
    prod45('../input/InformeEpidemiologico/', 'NoNotificados',
           '../output/producto45/CasosNoNotificadosPorComunaHistorico')
    prod45('../input/InformeEpidemiologico/', 'Probables', '../output/producto45/CasosProbablesPorComunaHistorico')

    prod57('../input/InformeEpidemiologico/fallecidos_hospitalizados.csv', '../output/producto57/fallecidos_hospitalizados')

    prod59_60_62('../input/InformeEpidemiologico/casos_nuevos_acumulados_por_fecha.csv', '../output/producto62/casos_nuevos_acumulados_por_fecha')

    prod59_60_62('../input/InformeEpidemiologico/etapa_clinica_por_fecha_notificacion.csv',
              '../output/producto59/etapa_clinica_por_fecha_notificacion')
    prod59_60_62('../input/InformeEpidemiologico/etapa_clinica_por_fis.csv',
              '../output/producto60/etapa_clinica_por_fis')
    prod61('../input/InformeEpidemiologico/serie_fallecidos_comuna.csv',
              '../output/producto61/serie_fallecidos_comuna')

