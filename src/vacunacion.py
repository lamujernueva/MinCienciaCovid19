'''
MIT License

Copyright (c) 2020 Minciencia

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
import requests
import utils
import pandas as pd
import datetime as dt
import numpy as np
from itertools import groupby


class vacunacion:
    def __init__(self,output,indicador):
        self.output = output
        self.indicador = indicador
        self.my_files = {
            'vacunacion_fabricante':
                'https://raw.githubusercontent.com/juancri/covid19-vaccination/master/output/chile-vaccination-type.csv',
            'vacunacion_region':
                'https://raw.githubusercontent.com/juancri/covid19-vaccination/master/output/chile-vaccination.csv',
            'vacunacion_edad':
                'https://github.com/juancri/covid19-vaccination/raw/master/output/chile-vaccination-ages.csv',
            'vacunacion_grupo':
                'https://github.com/juancri/covid19-vaccination/raw/master/output/chile-vaccination-groups.csv',
        }
        self.path = '../input/Vacunacion'

    def get_last(self):
        ## baja el archivo que corresponde
        if self.indicador == 'fabricante':
            print('Retrieving files')
            print('vacunacion_fabricante')
            r = requests.get(self.my_files['vacunacion_fabricante'])
            content = r.content
            csv_file = open(self.path + '/' + 'vacunacion_fabricante' + '.csv', 'wb')
            csv_file.write(content)
            csv_file.close()

        elif self.indicador == 'campana':
            print('Retrieving files')
            print('vacunacion_region')
            r = requests.get(self.my_files['vacunacion_region'])
            content = r.content
            csv_file = open(self.path + '/' + 'vacunacion_region' + '.csv', 'wb')
            csv_file.write(content)
            csv_file.close()

        elif self.indicador == 'edad':
            print('Retrieving files')
            print('vacunacion_edad')
            r = requests.get(self.my_files['vacunacion_edad'])
            content = r.content
            csv_file = open(self.path + '/' + 'vacunacion_edad' + '.csv', 'wb')
            csv_file.write(content)
            csv_file.close()

        elif self.indicador == 'caracteristicas_del_vacunado':
            print('Retrieving files')
            print('vacunacion_grupo')
            r = requests.get(self.my_files['vacunacion_grupo'])
            content = r.content
            csv_file = open(self.path + '/' + 'vacunacion_grupo' + '.csv', 'wb')
            csv_file.write(content)
            csv_file.close()

        ## selecciona el archivo que corresponde
        if self.indicador == 'fabricante':
            print('reading files')
            print('vacunacion_fabricante')
            self.last_added = pd.read_csv('../input/Vacunacion/vacunacion_fabricante.csv')

        elif self.indicador == 'campana':
            print('reading files')
            print('vacunacion_region')
            self.last_added = pd.read_csv('../input/Vacunacion/vacunacion_region.csv')

        elif self.indicador == 'edad':
            print('reading files')
            print('vacunacion_edad')
            self.last_added = pd.read_csv('../input/Vacunacion/vacunacion_edad.csv')

        elif self.indicador == 'caracteristicas_del_vacunado':
            print('reading files')
            print('vacunacion_grupo')
            self.last_added = pd.read_csv('../input/Vacunacion/vacunacion_grupo.csv')


        elif self.indicador == 'vacunas_region':
            print('reading files')
            print('vacunacion por region por dia')
            aux = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_1.csv', sep=';', encoding='ISO-8859-1')
            aux_2 = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_1_2.csv', sep=';', encoding='ISO-8859-1')
            self.last_added = pd.concat([aux, aux_2], ignore_index=True)


        elif self.indicador == 'vacunas_comuna':
            print('reading files')
            print('vacunacion por comuna por dia')
            aux = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_1.csv', sep=';', encoding='ISO-8859-1')
            aux_2 = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_1_2.csv', sep=';', encoding='ISO-8859-1')
            self.last_added = pd.concat([aux, aux_2], ignore_index=True)

        elif self.indicador == 'vacunas_edad_region':
            print('reading files')
            print('vacunacion por region por edad')
            aux = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_2.csv', sep=';', encoding='ISO-8859-1')
            aux_2 = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_2_2.csv', sep=';', encoding='ISO-8859-1')
            self.last_added = pd.concat([aux, aux_2], ignore_index=True)

        elif self.indicador == 'vacunas_edad_sexo':
            print('reading files')
            print('vacunacion por sexo por edad')
            aux = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_3.csv', sep=';', encoding='ISO-8859-1')
            aux_2 = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_3_2.csv', sep=';', encoding='ISO-8859-1')
            self.last_added = pd.concat([aux, aux_2], ignore_index=True)

            print('vacunacion por sexo por edad y FECHA')
            aux = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_6.csv', sep=';', encoding='ISO-8859-1')
            aux_2 = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_6_2.csv', sep=';', encoding='ISO-8859-1')
            self.last_edad_fecha = pd.concat([aux, aux_2], ignore_index=True)

        elif self.indicador == 'vacunas_prioridad':
            print('reading files')
            print('vacunacion por grupos prioritarios')
            self.last_added  = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_8.csv', sep=';', encoding='ISO-8859-1')
            # aux_2 = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_8_2.csv', sep=';', encoding='ISO-8859-1')
            # self.last_added = pd.concat([aux, aux_2], ignore_index=True)

        elif self.indicador == 'vacunas_comuna_edad':
            print('reading files')
            print('vacunacion por comuna por edad')
            aux = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_2.csv', sep=';', encoding='ISO-8859-1')
            aux_2 = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_2_2.csv', sep=';', encoding='ISO-8859-1')
            self.last_added = pd.concat([aux, aux_2], ignore_index=True)

        elif self.indicador == 'vacunas_establecimiento':
            print('reading files')
            print('vacunacion por establecimiento')
            aux = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_7.csv', sep=';', encoding='ISO-8859-1')
            aux_2 = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_7_2.csv', sep=';', encoding='ISO-8859-1')
            self.last_added = pd.concat([aux, aux_2], ignore_index=True)

        elif self.indicador == 'vacunas_fabricante':
            print('reading files')
            print('vacunacion por fabricante y fecha')
            aux = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_7.csv', sep=';', encoding='ISO-8859-1')
            aux_2 = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_7_2.csv', sep=';', encoding='ISO-8859-1')
            self.last_added = pd.concat([aux, aux_2], ignore_index=True)

        elif self.indicador == 'vacunas_fabricante_edad':
            print('reading files')
            print('vacunacion por fabricante y edad')
            aux = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_9.csv', sep=';', encoding='ISO-8859-1')
            aux_2 = pd.read_csv('../input/Vacunacion/WORK_ARCHIVO_9_2.csv', sep=';', encoding='ISO-8859-1')
            self.last_added = pd.concat([aux, aux_2], ignore_index=True)



    def last_to_csv(self):
        if self.indicador == 'fabricante':
            ## campana por fabricante

            self.last_added.rename(columns={'Dose': 'Dosis'}, inplace=True)
            self.last_added.rename(columns={'Type': 'Fabricante'}, inplace=True)

            self.last_added["Dosis"] = self.last_added["Dosis"].replace({"First": "Primera",
                                                                         "Second": "Segunda"
                                                                         })

            identifiers = ['Fabricante', 'Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Fecha'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)

        elif self.indicador == 'campana':
            ## campana por region

            self.last_added.rename(columns={'Dose': 'Dosis'}, inplace=True)
            utils.regionName(self.last_added)

            self.last_added["Dosis"] = self.last_added["Dosis"].replace({"First": "Primera",
                                                                         "Second": "Segunda"
                                                                         })

            identifiers = ['Region', 'Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Fecha'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)

        elif self.indicador == 'edad':
            ## campana por edad

            self.last_added.rename(columns={'Dose': 'Dosis',
                                            'Age':'Rango_etario'}, inplace=True)

            self.last_added["Dosis"] = self.last_added["Dosis"].replace({"First": "Primera",
                                                                         "Second": "Segunda"
                                                                         })

            identifiers = ['Rango_etario', 'Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Fecha'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)

        elif self.indicador == 'caracteristicas_del_vacunado':
            ## campana por caracter del vacunado

            self.last_added.rename(columns={'Dose': 'Dosis',
                                            'Group':'Grupo'}, inplace=True)

            self.last_added["Dosis"] = self.last_added["Dosis"].replace({"First": "Primera",
                                                                         "Second": "Segunda"
                                                                         })

            identifiers = ['Grupo', 'Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Fecha'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)

        elif self.indicador == 'vacunas_region':
            self.last_added.rename(columns={'REGION_CORTO': 'Region',
                                            'COD_COMUNA_FINAL': 'Comuna',
                                            'FECHA_INMUNIZACION': 'Fecha',
                                            'SUM_of_SUM_of_2aDOSIS': 'Segunda_comuna',
                                            'SUM_of_SUM_of_1aDOSIS': 'Primera_comuna',
                                            'SUM_of_ÚnicaDOSIS':'Unica_comuna'}, inplace=True)
            self.last_added = self.last_added.dropna(subset=['Fecha'])
            self.last_added['Fecha'] = pd.to_datetime(self.last_added['Fecha'],format='%d/%m/%Y').dt.strftime("%Y-%m-%d")
            self.last_added.sort_values(by=['Region','Fecha'], inplace=True)
            utils.regionName(self.last_added)
            regiones = pd.DataFrame(self.last_added['Region'].unique())


            #transformar
            ## agrupar por comuna
            self.last_added['Primera'] = self.last_added.groupby(['Region','Fecha'])['Primera_comuna'].transform('sum')
            self.last_added['Segunda'] = self.last_added.groupby(['Region','Fecha'])['Segunda_comuna'].transform('sum')
            self.last_added['Unica'] = self.last_added.groupby(['Region', 'Fecha'])['Unica_comuna'].transform('sum')
            self.last_added = self.last_added[['Region','Fecha','Primera','Segunda','Unica']]
            self.last_added.drop_duplicates(inplace=True)

            ##llenar fechas para cada region y crear total
            idx = pd.date_range(self.last_added['Fecha'].min(), self.last_added['Fecha'].max())
            df = pd.DataFrame()
            total = pd.DataFrame(columns=['Region','Fecha','Primera','Segunda','Unica'])
            total = utils.fill_in_missing_dates(total, 'Fecha', 0, idx)
            total["Region"] = total["Region"].replace({0: 'Total'})
            for region in regiones[0]:
                df_region = self.last_added.loc[self.last_added['Region'] == region]
                df_region = utils.fill_in_missing_dates(df_region,'Fecha',0,idx)
                df_region["Region"] = df_region["Region"].replace({0:region})
                total['Primera'] = df_region['Primera'] + total['Primera']
                total['Segunda'] = df_region['Segunda'] + total['Segunda']
                total['Unica'] = df_region['Unica'] + total['Unica']
                df = df.append(df_region, ignore_index=True)
            total = total.append(df,ignore_index=True)
            total['Fecha'] = total['Fecha'].dt.strftime("%Y-%m-%d")
            self.last_added = total

            ##sumar totales
            self.last_added['Primera'] = pd.to_numeric(self.last_added['Primera'])
            self.last_added['Segunda'] = pd.to_numeric(self.last_added['Segunda'])
            self.last_added['Unica'] = pd.to_numeric(self.last_added['Unica'])
            self.last_added['Primera'] = self.last_added.groupby(['Region'])['Primera'].transform('cumsum')
            self.last_added['Segunda'] = self.last_added.groupby(['Region'])['Segunda'].transform('cumsum')
            self.last_added['Unica'] = self.last_added.groupby(['Region'])['Unica'].transform('cumsum')
            #self.last_added['Total'] = self.last_added.sum(numeric_only=True, axis=1)

            ##transformar en input
            df = pd.DataFrame()
            regiones = pd.DataFrame(self.last_added['Region'].unique())
            for region in regiones[0]:
                df_region = self.last_added.loc[self.last_added['Region'] == region]
                df_region.set_index('Fecha',inplace=True)
                df_region = df_region[['Primera','Segunda','Unica']].T
                df_region.reset_index(drop=True, inplace=True)
                df = df.append(df_region, ignore_index=True)


            new_col = ['Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica','Primera', 'Segunda','Unica']
            df.insert(0, column='Dosis', value=new_col)
            new_col = pd.DataFrame()
            for region in regiones[0]:
                col = [region,region,region]
                new_col = new_col.append(col, ignore_index=True)
            df.insert(0, column='Region', value=new_col)
            self.last_added = df




            identifiers = ['Region', 'Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Fecha'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)
            df_std.to_json(self.output + '.json',orient='values',force_ascii=False)

        elif self.indicador == 'vacunas_edad_region':
            self.last_added.rename(columns={'NOMBRE_REGION': 'Region',
                                            'COD_COMUNA': 'Comuna',
                                            'EDAD_ANOS': 'Edad',
                                            'POBLACION':'Poblacion',
                                            '2aDOSIS_RES': 'Segunda_comuna',
                                            '1aDOSIS_RES': 'Primera_comuna',
                                            'ÚnicaDOSIS':'Unica_comuna'}, inplace=True)
            self.last_added.sort_values(by=['Region', 'Edad'], inplace=True)
            utils.regionName(self.last_added)
            regiones = pd.DataFrame(self.last_added['Region'].unique())

            # transformar
            ## agrupar por comuna
            self.last_added['Primera'] = self.last_added.groupby(['Region', 'Edad'])['Primera_comuna'].transform('sum')
            self.last_added['Segunda'] = self.last_added.groupby(['Region', 'Edad'])['Segunda_comuna'].transform('sum')
            self.last_added['Unica'] = self.last_added.groupby(['Region', 'Edad'])['Unica_comuna'].transform('sum')
            self.last_added['Poblacion'] = self.last_added.groupby(['Region','Edad'])['Poblacion'].transform('sum')
            self.last_added = self.last_added[['Region', 'Edad', 'Poblacion','Primera', 'Segunda','Unica']]
            self.last_added.drop_duplicates(inplace=True)

            ##crear total
            df = pd.DataFrame()
            total = pd.DataFrame(columns=['Region', 'Edad','Poblacion','Primera', 'Segunda','Unica'])
            total['Edad'] = list(range(15, 81))
            total["Region"] = total["Region"].fillna('Total')
            for region in regiones[0]:
                df_region = self.last_added.loc[self.last_added['Region'] == region]
                df_region.reset_index(drop=True, inplace=True)
                total['Primera'] = total.Primera.fillna(0) + df_region.Primera.fillna(0)
                total['Segunda'] = total.Segunda.fillna(0) + df_region.Segunda.fillna(0)
                total['Unica'] = total.Unica.fillna(0) + df_region.Unica.fillna(0)
                total['Poblacion'] = total.Poblacion.fillna(0) + df_region.Poblacion.fillna(0)
                df = df.append(df_region, ignore_index=True)
            edad = total
            total = total.append(df, ignore_index=True)
            self.last_added = total

            ##transformar en input
            df = pd.DataFrame()
            regiones = pd.DataFrame(self.last_added['Region'].unique())
            for region in regiones[0]:
                df_region = self.last_added.loc[self.last_added['Region'] == region]
                df_region.set_index('Edad', inplace=True)
                df_region = df_region[['Primera', 'Segunda','Unica']].T
                df_region.reset_index(drop=True, inplace=True)
                df = df.append(df_region, ignore_index=True)

            new_col = ['Primera', 'Segunda', 'Unica','Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica',
                       'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica',
                       'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica',
                       'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica',
                       'Primera', 'Segunda', 'Unica', 'Primera', 'Segunda', 'Unica']
            df.insert(0, column='Dosis', value=new_col)
            new_col = pd.DataFrame()
            for region in regiones[0]:
                col = [region, region,region]
                new_col = new_col.append(col, ignore_index=True)
            df.insert(0, column='Region', value=new_col)
            self.last_added = df

            identifiers = ['Region','Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Edad'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)
            df_std.to_json(self.output + '.json',orient='values',force_ascii=False)

        elif self.indicador == 'vacunas_edad_sexo':

            #Por región, totales
            self.last_added.rename(columns={'NOMBRE_REGION': 'Region',
                                            'SEXO': 'Sexo',
                                            'EDAD_ANOS': 'Edad',
                                            'POBLACION':'Poblacion',
                                            'SUM_of_1aDOSIS': 'Primera',
                                            'SUM_of_2aDOSIS': 'Segunda',
                                            'SUM_of_ÚnicaDOSIS':'Unica'}, inplace=True)
            self.last_added.sort_values(by=['Sexo','Edad'], inplace=True)
            self.last_added = self.last_added[['Sexo','Edad','Primera','Segunda','Unica']]
            sexo = pd.DataFrame(self.last_added['Sexo'].unique())

            ##crear total
            df = pd.DataFrame()
            for sex in sexo[0]:
                total = pd.DataFrame(columns=['Sexo', 'Edad', 'Primera', 'Segunda','Unica'])
                total['Edad'] = list(range(self.last_added.Edad.min(), self.last_added.Edad.max() + 1))
                df_sex = self.last_added.loc[self.last_added['Sexo'] == sex]
                df_sex.reset_index(drop=True, inplace=True)
                df_sex.index = df_sex['Edad']
                total.index = total['Edad']
                total['Sexo'] = total.Sexo.fillna(sex)
                total['Primera'] = total.Primera.fillna(0) + df_sex.Primera.fillna(0)
                total['Segunda'] = total.Segunda.fillna(0) + df_sex.Segunda.fillna(0)
                total['Unica'] = total.Unica.fillna(0) + df_sex.Unica.fillna(0)
                df = df.append(total, ignore_index=True)
            self.last_added = df

            ##transformar en input
            df = pd.DataFrame()
            sexo = pd.DataFrame(self.last_added['Sexo'].unique())
            for sex in sexo[0]:
                df_sex = self.last_added.loc[self.last_added['Sexo'] == sex]
                df_sex.set_index('Edad', inplace=True)
                df_sex = df_sex[['Primera', 'Segunda','Unica']].T
                df_sex.reset_index(drop=True, inplace=True)
                df = df.append(df_sex, ignore_index=True)

            new_col = ['Primera', 'Segunda','Unica', 'Primera', 'Segunda','Unica', 'Primera', 'Segunda','Unica', 'Primera', 'Segunda','Unica']
            df.insert(0, column='Dosis', value=new_col)
            new_col = pd.DataFrame()
            for sex in sexo[0]:
                col = [sex, sex,sex]
                new_col = new_col.append(col, ignore_index=True)
            df.insert(0, column='Sexo', value=new_col)
            self.last_added = df

            identifiers = ['Sexo','Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Edad'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)
            df_std.to_json(self.output + '.json', orient='values', force_ascii=False)

            # Por fecha, totales
            self.last_edad_fecha.rename(columns={'FECHA_INMUNIZACION': 'Fecha',
                                            'EDAD_ANOS': 'Edad',
                                            'SUM_of_1aDOSIS': 'Primera',
                                            'SUM_of_2aDOSIS': 'Segunda',
                                            'SUM_of_SUM_of_ÚnicaDOSIS': 'Unica'}, inplace=True)
            self.last_edad_fecha['Fecha'] = pd.to_datetime(self.last_edad_fecha['Fecha'], format='%d/%m/%Y').dt.strftime("%Y-%m-%d")
            self.last_edad_fecha.sort_values(by=['Fecha', 'Edad'], inplace=True)
            self.last_edad_fecha.reset_index(drop=True,inplace=True)
            self.last_edad_fecha.dropna(subset=['Fecha'],inplace=True)
            columns_name = self.last_edad_fecha.columns.values
            maxSE = self.last_edad_fecha[columns_name[0]].max()
            minSE = self.last_edad_fecha[columns_name[0]].min()

            print(minSE, maxSE)
            lenSE = (pd.to_datetime(maxSE) - pd.to_datetime(minSE)).days + 1
            startdate = pd.to_datetime(minSE)
            date_list = pd.date_range(startdate, periods=lenSE).tolist()
            date_list = [dt.datetime.strftime(x, "%Y-%m-%d") for x in date_list]
            print(date_list)
            self.last_edad_fecha['Total'] = self.last_edad_fecha['Primera'].fillna(0) + self.last_edad_fecha['Segunda'].fillna(0) + self.last_edad_fecha['Unica'].fillna(0)



            for k in [2, 3, 4,5]:
                edades = self.last_edad_fecha[columns_name[1]].unique()
                edades = edades[~np.isnan(edades)]
                edades = np.sort(edades)
                df = pd.DataFrame(np.zeros((len(edades), lenSE)))
                df.insert(0, 'Edad', edades)
                df.set_index('Edad',inplace=True)
                dicts = {}
                keys = range(lenSE)

                for i in keys:
                    dicts[i] = date_list[i]

                df.rename(columns=dicts, inplace=True)
                for index, row in self.last_edad_fecha.iterrows():
                    df[row['Fecha']][row['Edad']] = row[k]
                df.reset_index(inplace=True)


                if k == 2:
                    name = '../output/producto78/vacunados_edad_fecha' + '_1eraDosis.csv'
                    df.to_csv(name, index=False)
                    dft = df.T
                    dft.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Edad']
                    variables = [x for x in df.columns if x not in identifiers]
                    outputDF2_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                                            value_name='Primera Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

                if k == 3:
                    name = '../output/producto78/vacunados_edad_fecha' + '_2daDosis.csv'
                    df.to_csv(name, index=False)
                    dft = df.T
                    dft.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Edad']
                    variables = [x for x in df.columns if x not in identifiers]
                    outputDF2_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                                            value_name='Segunda Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

                if k == 4:
                    name = '../output/producto78/vacunados_edad_fecha' + '_UnicaDosis.csv'
                    df.to_csv(name, index=False)
                    dft = df.T
                    dft.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Edad']
                    variables = [x for x in df.columns if x not in identifiers]
                    outputDF2_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                                            value_name='Unica Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

                if k == 5:
                    name = '../output/producto78/vacunados_edad_fecha' + '_total.csv'
                    df.to_csv(name, index=False)
                    dft = df.T
                    dft.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Edad']
                    variables = [x for x in df.columns if x not in identifiers]
                    outputDF2_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                                            value_name='Total vacunados')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

        elif self.indicador == 'vacunas_prioridad':
            self.last_added.rename(columns={'CRITERIO': 'Grupo',
                                            'SUB_CRITERIO': 'Subgrupo',
                                            '1aDOSIS1': 'Primera',
                                            '2aDOSIS1': 'Segunda'}, inplace=True)
            self.last_added.sort_values(by=['Grupo', 'Subgrupo'], inplace=True)
            self.last_added = self.last_added[['Grupo', 'Subgrupo', 'Primera', 'Segunda']]
            self.last_added['Primera'] = self.last_added.groupby(['Grupo', 'Subgrupo'])['Primera'].transform('sum')
            self.last_added['Segunda'] = self.last_added.groupby(['Grupo', 'Subgrupo'])['Segunda'].transform('sum')
            self.last_added = self.last_added[['Grupo', 'Subgrupo', 'Primera', 'Segunda']]
            self.last_added.drop_duplicates(inplace=True)


            ##transformar en input
            df = pd.DataFrame()
            grupos = pd.DataFrame(self.last_added['Grupo'].unique())
            for grupo in grupos[0]:
                df_grupo = self.last_added.loc[self.last_added['Grupo'] == grupo]
                df_grupo.set_index('Subgrupo', inplace=True)
                df_grupo = df_grupo[['Primera', 'Segunda']].T
                df_grupo.reset_index(drop=True, inplace=True)
                df = df.append(df_grupo, ignore_index=True)

            new_col = ['Primera', 'Segunda', 'Primera', 'Segunda', 'Primera', 'Segunda', 'Primera', 'Segunda',
                       'Primera', 'Segunda', 'Primera', 'Segunda']
            df.insert(0, column='Dosis', value=new_col)
            new_col = pd.DataFrame()
            for grupo in grupos[0]:
                col = [grupo, grupo]
                new_col = new_col.append(col, ignore_index=True)
            df.insert(0, column='Grupo', value=new_col)
            self.last_added = df

            identifiers = ['Grupo', 'Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Subgrupo'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)
            df_std.to_json(self.output + '.json',orient='values',force_ascii=False)

        elif self.indicador == 'vacunas_comuna':
            ##template por comuna
            df_base = pd.read_csv('../input/DistribucionDEIS/baseFiles/DEIS_template.csv')
            df_base['Codigo region'] = df_base['Codigo region'].fillna(0)
            df_base['Codigo comuna'] = df_base['Codigo comuna'].fillna(0)
            df_base['Comuna'] = df_base['Comuna'].fillna(0)
            todrop = df_base.loc[df_base['Comuna'] == 0]
            df_base.drop(todrop.index, inplace=True)
            df_base['Codigo region'] = df_base['Codigo region'].astype(int)
            df_base['Codigo comuna'] = df_base['Codigo comuna'].astype(int)

            desconocido = df_base['Codigo comuna'] != 0
            df_base['Codigo comuna'].where(desconocido, '', inplace=True)

            Comp = df_base.loc[df_base['Comuna'] != 'Total']
            Comp.reset_index(inplace=True)
            utils.desconocidoName(Comp)
            for k in range(len(Comp)):
                if Comp.loc[k, 'Codigo region'] < 10:
                    Comp.loc[k, 'Codigo region'] = '0' + str(Comp.loc[k, 'Codigo region'])
                else:
                    Comp.loc[k, 'Codigo region'] = str(Comp.loc[k, 'Codigo region'])

                if Comp.loc[k, 'Codigo comuna'] != '':
                    if Comp.loc[k, 'Codigo comuna'] < 10000:
                        Comp.loc[k, 'Codigo comuna'] = '0' + str(Comp.loc[k, 'Codigo comuna'])
                    else:
                        Comp.loc[k, 'Codigo comuna'] = str(Comp.loc[k, 'Codigo comuna'])

            comuna = Comp['Comuna']

            self.last_added.rename(columns={'REGION_CORTO': 'region_residencia',
                                            'COD_COMUNA_FINAL': 'Codigo comuna',
                                            'FECHA_INMUNIZACION': 'Fecha',
                                            'SUM_of_SUM_of_2aDOSIS': 'Segunda_comuna',
                                            'SUM_of_SUM_of_1aDOSIS': 'Primera_comuna',
                                            'SUM_of_ÚnicaDOSIS':'Unica_comuna'}, inplace=True)
            self.last_added = self.last_added.dropna(subset=['Fecha'])
            self.last_added['Fecha'] = pd.to_datetime(self.last_added['Fecha'],format='%d/%m/%Y').dt.strftime("%Y-%m-%d")
            self.last_added.sort_values(by=['region_residencia','Fecha'], inplace=True)
            utils.regionDEISName(self.last_added)

            for k in range(len(self.last_added)):
               if self.last_added.loc[k, 'Codigo comuna'] != '':
                    if self.last_added.loc[k, 'Codigo comuna'] < 10000:
                        self.last_added.loc[k, 'Codigo comuna'] = '0' + str(self.last_added.loc[k, 'Codigo comuna'])
                    else:
                        self.last_added.loc[k, 'Codigo comuna'] = str(self.last_added.loc[k, 'Codigo comuna'])

            df_sup = Comp[['Codigo comuna', 'Comuna']]
            df_sup['Codigo comuna'] = df_sup['Codigo comuna'].replace('', 0)
            self.last_added = self.last_added.merge(df_sup, on="Codigo comuna", how="left")
            self.last_added.set_index('Comuna', inplace=True)

            columns_name = self.last_added.columns.values

            maxSE = self.last_added[columns_name[2]].max()
            minSE = self.last_added[columns_name[2]].min()

            print(minSE, maxSE)
            lenSE = (pd.to_datetime(maxSE) - pd.to_datetime(minSE)).days + 1
            startdate = pd.to_datetime(minSE)
            date_list = pd.date_range(startdate, periods=lenSE).tolist()
            date_list = [dt.datetime.strftime(x, "%Y-%m-%d") for x in date_list]
            print(date_list)


            SE_comuna = self.last_added[columns_name[2]]

            def edad2rango(df, comuna):
                cols = df.columns.tolist()
                df2 = pd.DataFrame(columns=cols)
                p = 0
                for row in comuna:
                    aux = df.loc[df.index == row]
                    aux2 = aux.groupby(['Fecha']).sum()
                    aux2['Comuna'] = row
                    aux2.set_index(['Comuna'], inplace=True)

                    identifiers = ['region_residencia', 'Codigo comuna', 'Fecha']
                    temp = aux[identifiers].copy()
                    temp.drop_duplicates(keep='first', inplace=True)
                    temp2 = pd.concat([temp, aux2], axis=1)

                    if p == 0:
                        df2 = temp2
                        p += 1
                    else:
                        df2 = pd.concat([df2, temp2], axis=0)

                return df2

            dfv = edad2rango(self.last_added, comuna)
            for k in [3,4,5]:
                df = pd.DataFrame(np.zeros((len(comuna), lenSE)))

                dicts = {}
                keys = range(lenSE)
                # values = [i for i in range(lenSE)]

                for i in keys:
                    dicts[i] = date_list[i]

                df.rename(columns=dicts, inplace=True)
                value_comuna = dfv[columns_name[k]]
                value_comuna.fillna(0,inplace=True)
                SE_comuna = dfv['Fecha'].copy()
                i=0
                for row in dfv.index:
                    idx = comuna.loc[comuna == row].index.values
                    if idx.size > 0:
                        col = SE_comuna[i]
                        df[col][idx] = value_comuna[i].astype(int)


                    i += 1


                df_output = pd.concat([Comp, df], axis=1)
                df_output.drop(columns=['index'], axis=1, inplace=True)

                nComunas = [len(list(group)) for key, group in groupby(df_output['Codigo region'])]

                identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                variables = [x for x in df_output.columns if x not in identifiers]

                begRow = 0

                for i in range(len(nComunas)):

                    endRow = begRow + nComunas[i]

                    firstList = df_output[identifiers].iloc[endRow - 1].values.tolist()
                    firstList[2] = 'Total'
                    firstList[3] = ''

                    valuesTotal = df_output[variables][begRow:endRow].sum(axis=0).tolist()

                    regionTotal = pd.DataFrame((firstList + valuesTotal), index=df_output.columns.values).transpose()

                    if i < len(nComunas) - 1:
                        blank_line = pd.Series(np.empty((len(regionTotal), 0)).tolist())

                        regionTotal = pd.concat([regionTotal, blank_line], axis=0)
                        regionTotal.drop(columns=0, axis=1, inplace=True)

                    temp = pd.concat([df_output.iloc[begRow:endRow], regionTotal], axis=0)
                    if i == 0:
                        outputDF2 = temp
                    else:
                        outputDF2 = pd.concat([outputDF2, temp], axis=0)

                    if i < len(nComunas) - 1:
                        begRow = endRow

                outputDF2.reset_index(inplace=True)
                outputDF2.drop(columns=['index'], axis=1, inplace=True)
                outputDF2[variables] = outputDF2[variables].dropna()  # .astype(int)

                print(outputDF2.head(20))

                outputDF2.dropna(how='all', inplace=True)
                todrop = outputDF2.loc[outputDF2['Comuna'] == 'Total']
                outputDF2.drop(todrop.index, inplace=True)


                if k == 3:
                    name = self.output + '_1eraDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                    outputDF2.drop(columns=['Poblacion'],inplace=True)
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                                            value_name='Primera Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)
                elif k == 4:
                    name = self.output +'_2daDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                    outputDF2.drop(columns=['Poblacion'], inplace=True)
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                                            value_name='Segunda Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

                elif k == 5:
                    name = self.output +'_UnicaDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                    outputDF2.drop(columns=['Poblacion'], inplace=True)
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                                            value_name='Unica Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

        elif self.indicador == 'vacunas_comuna_edad':
            ##template por comuna
            df_base = pd.read_csv('../input/DistribucionDEIS/baseFiles/DEIS_template.csv')
            df_base['Codigo region'] = df_base['Codigo region'].fillna(0)
            df_base['Codigo comuna'] = df_base['Codigo comuna'].fillna(0)
            df_base['Comuna'] = df_base['Comuna'].fillna(0)
            todrop = df_base.loc[df_base['Comuna'] == 0]
            df_base.drop(todrop.index, inplace=True)
            df_base['Codigo region'] = df_base['Codigo region'].astype(int)
            df_base['Codigo comuna'] = df_base['Codigo comuna'].astype(int)

            desconocido = df_base['Codigo comuna'] != 0
            df_base['Codigo comuna'].where(desconocido, '', inplace=True)

            Comp = df_base.loc[df_base['Comuna'] != 'Total']
            Comp.reset_index(inplace=True)
            utils.desconocidoName(Comp)
            for k in range(len(Comp)):
                if Comp.loc[k, 'Codigo region'] < 10:
                    Comp.loc[k, 'Codigo region'] = '0' + str(Comp.loc[k, 'Codigo region'])
                else:
                    Comp.loc[k, 'Codigo region'] = str(Comp.loc[k, 'Codigo region'])

                if Comp.loc[k, 'Codigo comuna'] != '':
                    if Comp.loc[k, 'Codigo comuna'] < 10000:
                        Comp.loc[k, 'Codigo comuna'] = '0' + str(Comp.loc[k, 'Codigo comuna'])
                    else:
                        Comp.loc[k, 'Codigo comuna'] = str(Comp.loc[k, 'Codigo comuna'])

            comuna = Comp['Comuna']

            self.last_added.rename(columns={'NOMBRE_REGION': 'region_residencia',
                                            'COD_COMUNA': 'Codigo comuna',
                                            'EDAD_ANOS': 'Edad',
                                            '2aDOSIS_RES': 'Segunda_comuna',
                                            '1aDOSIS_RES': 'Primera_comuna',
                                            'ÚnicaDOSIS':'Unica_comuna'}, inplace=True)
            utils.regionDEISName(self.last_added)
            self.last_added = self.last_added[['region_residencia','Codigo comuna','Edad','Primera_comuna','Segunda_comuna','Unica_comuna']]

            for k in range(len(self.last_added)):
               if self.last_added.loc[k, 'Codigo comuna'] != '':
                    if self.last_added.loc[k, 'Codigo comuna'] < 10000:
                        self.last_added.loc[k, 'Codigo comuna'] = '0' + str(self.last_added.loc[k, 'Codigo comuna'])
                    else:
                        self.last_added.loc[k, 'Codigo comuna'] = str(self.last_added.loc[k, 'Codigo comuna'])

            df_sup = Comp[['Codigo comuna', 'Comuna']]
            df_sup['Codigo comuna'] = df_sup['Codigo comuna'].replace('', 0)
            self.last_added = self.last_added.merge(df_sup, on="Codigo comuna", how="left")
            self.last_added.set_index('Comuna', inplace=True)

            columns_name = self.last_added.columns.values

            maxSE = self.last_added[columns_name[2]].max()
            minSE = self.last_added[columns_name[2]].min()

            print(minSE, maxSE)
            lenSE = maxSE - minSE + 1
            date_list = list(range(minSE,maxSE+1))
            print(date_list)


            SE_comuna = self.last_added[columns_name[2]]

            for k in [3,4,5]:
                df = pd.DataFrame(np.zeros((len(comuna), lenSE)))

                dicts = {}
                keys = range(lenSE)
                # values = [i for i in range(lenSE)]

                for i in keys:
                    dicts[i] = date_list[i]

                df.rename(columns=dicts, inplace=True)
                value_comuna = self.last_added[columns_name[k]]
                value_comuna.fillna(0,inplace=True)
                i=0
                for row in self.last_added.index:
                    idx = comuna.loc[comuna == row].index.values
                    if idx.size > 0:
                        col = SE_comuna[i]
                        df[col][idx] = value_comuna[i].astype(int)

                    i += 1


                df_output = pd.concat([Comp, df], axis=1)
                df_output.drop(columns=['index'], axis=1, inplace=True)

                nComunas = [len(list(group)) for key, group in groupby(df_output['Codigo region'])]

                identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                variables = [x for x in df_output.columns if x not in identifiers]

                begRow = 0

                for i in range(len(nComunas)):

                    endRow = begRow + nComunas[i]

                    firstList = df_output[identifiers].iloc[endRow - 1].values.tolist()
                    firstList[2] = 'Total'
                    firstList[3] = ''

                    valuesTotal = df_output[variables][begRow:endRow].sum(axis=0).tolist()

                    regionTotal = pd.DataFrame((firstList + valuesTotal), index=df_output.columns.values).transpose()

                    if i < len(nComunas) - 1:
                        blank_line = pd.Series(np.empty((len(regionTotal), 0)).tolist())

                        regionTotal = pd.concat([regionTotal, blank_line], axis=0)
                        regionTotal.drop(columns=0, axis=1, inplace=True)

                    temp = pd.concat([df_output.iloc[begRow:endRow], regionTotal], axis=0)
                    if i == 0:
                        outputDF2 = temp
                    else:
                        outputDF2 = pd.concat([outputDF2, temp], axis=0)

                    if i < len(nComunas) - 1:
                        begRow = endRow

                outputDF2.reset_index(inplace=True)
                outputDF2.drop(columns=['index'], axis=1, inplace=True)
                outputDF2[variables] = outputDF2[variables].dropna()  # .astype(int)

                print(outputDF2.head(20))

                outputDF2.dropna(how='all', inplace=True)
                todrop = outputDF2.loc[outputDF2['Comuna'] == 'Total']
                outputDF2.drop(todrop.index, inplace=True)


                if k == 3:
                    name = self.output + '_1eraDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                    outputDF2.drop(columns=['Poblacion'],inplace=True)
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Edad',
                                            value_name='Primera Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)
                elif k == 4:
                    name = self.output +'_2daDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                    outputDF2.drop(columns=['Poblacion'],inplace=True)
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Edad',
                                            value_name='Segunda Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

                elif k == 5:
                    name = self.output +'_UnicaDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                    outputDF2.drop(columns=['Poblacion'],inplace=True)
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Edad',
                                            value_name='Unica Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

        elif self.indicador == 'vacunas_establecimiento':
            #por establecimiento
            self.last_added.rename(columns={'NOMBRE_ESTAB': 'Establecimiento',
                                            'FECHA_INMUNIZACION':'Fecha',
                                           'SUM_of_2aDOSIS': 'Segunda_comuna',
                                           'SUM_of_1aDOSIS': 'Primera_comuna',
                                           'SUM_of_ÚnicaDOSIS':'Unica_comuna'}, inplace=True)
            self.last_added = self.last_added.dropna(subset=['Fecha'])
            self.last_added['Fecha'] = pd.to_datetime(self.last_added['Fecha'], format='%d/%m/%Y').dt.strftime(
                "%Y-%m-%d")
            self.last_added.sort_values(by=['Establecimiento', 'Fecha'], inplace=True)
            self.last_added = self.last_added.dropna(subset=['Establecimiento'])
            establecimientos = pd.DataFrame(self.last_added['Establecimiento'].unique())

            # transformar
            ## agrupar
            self.last_added['Primera'] = self.last_added.groupby(['Establecimiento','Fecha'])['Primera_comuna'].transform('sum')
            self.last_added['Segunda'] = self.last_added.groupby(['Establecimiento','Fecha'])['Segunda_comuna'].transform('sum')
            self.last_added['Unica'] = self.last_added.groupby(['Establecimiento', 'Fecha'])[
                'Unica_comuna'].transform('sum')
            self.last_added['Personas_vacunadas'] = self.last_added['Primera'] + self.last_added['Segunda'] + self.last_added['Unica']
            self.last_added = self.last_added[['Establecimiento','Fecha','Personas_vacunadas']]
            self.last_added.drop_duplicates(inplace=True)

            ##llenar fechas para cada region y crear total
            idx = pd.date_range(self.last_added['Fecha'].min(), self.last_added['Fecha'].max())
            df = pd.DataFrame()
            total = pd.DataFrame(columns=['Establecimiento','Fecha','Personas_vacunadas'])
            total = utils.fill_in_missing_dates(total, 'Fecha', 0, idx)
            total["Establecimiento"] = total["Establecimiento"].replace({0: 'Total'})
            for establecimiento in establecimientos[0]:
                df_establecimiento = self.last_added.loc[self.last_added['Establecimiento'] == establecimiento]
                df_establecimiento = utils.fill_in_missing_dates(df_establecimiento, 'Fecha', 0, idx)
                df_establecimiento["Establecimiento"] = df_establecimiento["Establecimiento"].replace({0: establecimiento})
                total['Personas_vacunadas'] = df_establecimiento['Personas_vacunadas'] + total['Personas_vacunadas']
                df = df.append(df_establecimiento, ignore_index=True)
            total = total.append(df, ignore_index=True)
            total['Fecha'] = total['Fecha'].dt.strftime("%Y-%m-%d")
            self.last_added = total

            ##transformar en input

            identifiers = ['Establecimiento','Fecha']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Dosis'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)

        elif self.indicador == 'vacunas_fabricante':

            # por fabricante y fecha
            self.last_added.rename(columns={'Laboratorio': 'Fabricante',
                                            'FECHA_INMUNIZACION': 'Fecha',
                                            'SUM_of_2aDOSIS': 'Segunda_comuna',
                                            'SUM_of_1aDOSIS': 'Primera_comuna',
                                            'SUM_of_ÚnicaDOSIS': 'Unica_comuna'}, inplace=True)
            self.last_added = self.last_added.dropna(subset=['Fecha'])
            self.last_added['Fecha'] = pd.to_datetime(self.last_added['Fecha'], format='%d/%m/%Y').dt.strftime(
                "%Y-%m-%d")
            self.last_added.sort_values(by=['Fabricante', 'Fecha'], inplace=True)
            self.last_added = self.last_added.dropna(subset=['Fecha'])
            fabricantes = pd.DataFrame(self.last_added['Fabricante'].unique())

            # transformar
            ## agrupar
            self.last_added['Primera'] = self.last_added.groupby(['Fabricante', 'Fecha'])[
                'Primera_comuna'].transform('sum')
            self.last_added['Segunda'] = self.last_added.groupby(['Fabricante', 'Fecha'])[
                'Segunda_comuna'].transform('sum')
            self.last_added['Unica'] = self.last_added.groupby(['Fabricante', 'Fecha'])[
                'Unica_comuna'].transform('sum')
            self.last_added = self.last_added[['Fabricante', 'Fecha', 'Primera','Segunda','Unica']]
            self.last_added.drop_duplicates(inplace=True)

            columns_name = self.last_added.columns.values

            maxSE = self.last_added[columns_name[1]].max()
            minSE = self.last_added[columns_name[1]].min()

            print(minSE, maxSE)
            lenSE = (pd.to_datetime(maxSE) - pd.to_datetime(minSE)).days + 1
            startdate = pd.to_datetime(minSE)
            date_list = pd.date_range(startdate, periods=lenSE).tolist()
            date_list = [dt.datetime.strftime(x, "%Y-%m-%d") for x in date_list]
            print(date_list)

            def edad2rango(df, fab):
                cols = df.columns.tolist()
                df2 = pd.DataFrame(columns=cols)
                p = 0
                for row in fab:
                    aux = df.loc[df.index == row]
                    aux2 = aux.groupby(['Fecha']).sum()
                    aux2['Fabricante'] = row
                    aux2.set_index(['Fabricante'], inplace=True)

                    identifiers = ['Fecha']
                    temp = aux[identifiers].copy()
                    temp.drop_duplicates(keep='first', inplace=True)
                    temp2 = pd.concat([temp, aux2], axis=1)

                    if p == 0:
                        df2 = temp2
                        p += 1
                    else:
                        df2 = pd.concat([df2, temp2], axis=0)

                return df2

            dffab = self.last_added
            dffab.set_index('Fabricante', inplace=True)
            dfv = edad2rango(dffab, fabricantes[0])

            for k in [2,3,4]:
                df = pd.DataFrame(np.zeros((len(fabricantes), lenSE)))

                dicts = {}
                keys = range(lenSE)
                # values = [i for i in range(lenSE)]

                for i in keys:
                    dicts[i] = date_list[i]

                df.rename(columns=dicts, inplace=True)
                value_comuna = dfv[columns_name[k]]
                value_comuna.fillna(0,inplace=True)
                SE_comuna = dfv['Fecha'].copy()
                i=0
                comuna = fabricantes[0]
                for row in dfv.index:
                    idx = comuna.loc[comuna == row].index.values
                    if idx.size > 0:
                        col = SE_comuna[i]
                        df[col][idx] = value_comuna[i].astype(int)


                    i += 1

                df_output = pd.concat([fabricantes[0], df], axis=1)
                df_output.rename(columns = {0: 'Fabricante'}, inplace = True)
                df_output.replace('Campaña SARS-CoV-2 (CanSino)','CanSino', inplace=True)
                outputDF2 = df_output

                if k == 2:
                    name = '../output/producto83/vacunacion_fabricantes_1eraDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Fabricante']
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                                            value_name='Primera Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)
                elif k == 3:
                    name = '../output/producto83/vacunacion_fabricantes_2daDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Fabricante']
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                                            value_name='Segunda Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

                elif k == 4:
                    name = '../output/producto83/vacunacion_fabricantes_UnicaDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Fabricante']
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                                            value_name='Unica Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

        elif self.indicador == 'vacunas_fabricante_edad':

            # por fabricante y fecha
            self.last_added.rename(columns={'Laboratorio': 'Fabricante',
                                            'EDAD_ANOS': 'Edad',
                                            'SUM_of_2aDOSIS': 'Segunda_comuna',
                                            'SUM_of_1aDOSIS': 'Primera_comuna',
                                            'SUM_of_ÚnicaDOSIS': 'Unica_comuna'}, inplace=True)
            self.last_added = self.last_added.dropna(subset=['Edad'])
            self.last_added.sort_values(by=['Fabricante', 'Edad'], inplace=True)
            fabricantes = pd.DataFrame(self.last_added['Fabricante'].unique())

            # transformar
            ## agrupar
            self.last_added['Primera'] = self.last_added.groupby(['Fabricante', 'Edad'])[
                'Primera_comuna'].transform('sum')
            self.last_added['Segunda'] = self.last_added.groupby(['Fabricante', 'Edad'])[
                'Segunda_comuna'].transform('sum')
            self.last_added['Unica'] = self.last_added.groupby(['Fabricante', 'Edad'])[
                'Unica_comuna'].transform('sum')
            self.last_added = self.last_added[['Fabricante', 'Edad', 'Primera','Segunda','Unica']]
            self.last_added.drop_duplicates(inplace=True)

            columns_name = self.last_added.columns.values

            maxSE = self.last_added[columns_name[1]].max()
            minSE = self.last_added[columns_name[1]].min()

            print(minSE, maxSE)
            lenSE = maxSE - minSE + 1
            date_list = list(range(minSE, maxSE + 1))
            print(date_list)

            def edad2rango(df, fab):
                cols = df.columns.tolist()
                df2 = pd.DataFrame(columns=cols)
                p = 0
                for row in fab:
                    aux = df.loc[df.index == row]
                    aux2 = aux.groupby(['Edad']).sum()
                    aux2['Fabricante'] = row
                    aux2.set_index(['Fabricante'], inplace=True)

                    identifiers = ['Edad']
                    temp = aux[identifiers].copy()
                    temp.drop_duplicates(keep='first', inplace=True)
                    temp2 = pd.concat([temp, aux2], axis=1)

                    if p == 0:
                        df2 = temp2
                        p += 1
                    else:
                        df2 = pd.concat([df2, temp2], axis=0)

                return df2

            dffab = self.last_added
            dffab.set_index('Fabricante', inplace=True)
            dfv = edad2rango(dffab, fabricantes[0])

            for k in [2,3,4]:
                df = pd.DataFrame(np.zeros((len(fabricantes), lenSE)))

                dicts = {}
                keys = range(lenSE)
                # values = [i for i in range(lenSE)]

                for i in keys:
                    dicts[i] = date_list[i]

                df.rename(columns=dicts, inplace=True)
                value_comuna = dfv[columns_name[k]]
                value_comuna.fillna(0,inplace=True)
                SE_comuna = dfv['Edad'].copy()
                i=0
                comuna = fabricantes[0]
                for row in dfv.index:
                    idx = comuna.loc[comuna == row].index.values
                    if idx.size > 0:
                        col = SE_comuna[i]
                        df[col][idx] = value_comuna[i].astype(int)


                    i += 1

                df_output = pd.concat([fabricantes[0], df], axis=1)
                df_output.rename(columns = {0: 'Fabricante'}, inplace = True)
                df_output.replace('Campaña SARS-CoV-2 (CanSino)','CanSino', inplace=True)
                outputDF2 = df_output

                if k == 2:
                    name = '../output/producto88/vacunacion_fabricantes_edad_1eraDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Fabricante']
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Edad',
                                            value_name='Primera Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)
                elif k == 3:
                    name = '../output/producto88/vacunacion_fabricantes_edad_2daDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Fabricante']
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Edad',
                                            value_name='Segunda Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

                elif k == 4:
                    name = '../output/producto88/vacunacion_fabricantes_edad_UnicaDosis.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Fabricante']
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Edad',
                                            value_name='Unica Dosis')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)
if __name__ == '__main__':
    print('Actualizamos campana de vacunacion por region')
    my_vacunas = vacunacion('../output/producto76/vacunacion','vacunas_region')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos total de vacunados por region y edad')
    my_vacunas = vacunacion('../output/producto77/total_vacunados_region_edad','vacunas_edad_region')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos total de vacunados por sexo y edad')
    my_vacunas = vacunacion('../output/producto78/total_vacunados_sexo_edad', 'vacunas_edad_sexo')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos total de vacunados por grupo prioritario')
    my_vacunas = vacunacion('../output/producto79/total_vacunados_prioridad', 'vacunas_prioridad')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos dosis por fabricante')
    my_vacunas = vacunacion('../output/producto76/fabricante','fabricante')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos dosis por edad')
    my_vacunas = vacunacion('../output/producto76/rango_etario','edad')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos dosis por caracteristicas_del_vacunado')
    my_vacunas = vacunacion('../output/producto76/grupo','caracteristicas_del_vacunado')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos camapaña de vacunación por comuna')
    my_vacunas = vacunacion('../output/producto80/vacunacion_comuna','vacunas_comuna')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos camapaña de vacunación por edad y comuna')
    my_vacunas = vacunacion('../output/producto81/vacunacion_comuna_edad', 'vacunas_comuna_edad')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos camapaña de vacunación por establecimiento')
    my_vacunas = vacunacion('../output/producto83/vacunacion_establecimiento', 'vacunas_establecimiento')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos camapaña de vacunación por fabricante y fecha')
    my_vacunas = vacunacion('../output/producto83/vacunacion_fabricantes', 'vacunas_fabricante')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos camapaña de vacunación por fabricante y edad')
    my_vacunas = vacunacion('../output/producto88/vacunacion_fabricantes_edad', 'vacunas_fabricante_edad')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()