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
import csv
import itertools

import pandas as pd
import glob
from utils import *

'''
Aca generamos los productos
53
54
55
56
68
69
70
71
72
73
'''


def prod53(fte, prod):
    print('Generating productos UC')

    # at least we have to process three files: nacional, region y provincia, and eventually, we should also prefix them
    # with a date to show a history. NO DATE NEEDED, confirmed by Alejandro. Just overwrite the files.

    # make a list of files to report what have we processed:
    p53_files = []
    p54_files = []
    p56_files = []
    p55_files = []
    p68_files = []
    p69_files = []
    p70_files = []
    p71_files = []
    p72_files = []
    p73_files = []

    for file in glob.glob(fte + '/*'):
        print('Processing file ' + file)
        filename = file.split('/')
        filename = filename[len(filename) - 1]
        filename = filename.replace(' ', '_')
        head = ''.join(itertools.islice(open(file, encoding='ISO-8859-1'), 5))
        s = csv.Sniffer()
        my_separator = s.sniff(head).delimiter
        print('Found separator: ' + my_separator)

        df = pd.read_csv(file, sep=my_separator)

        # Comunal
        if 'comuna' in file:
            df.rename(columns={'comuna': 'Codigo comuna'}, inplace=True)
            df.rename(columns={'codigo_comuna': 'Codigo comuna'}, inplace=True)
            df.drop('comuna_residencia', axis=1, inplace=True)
            print(df.columns)
            df = normalizaNombreCodigoRegionYCodigoComuna(df)
            regionName(df)
            if 'Positividad' in file:
                p55_files.append(file)
                df.to_csv(prod.replace('53', '55') + '/' + filename, index=False)
            if 'tasa test semanal' in file:
                p68_files.append(file)
                df.to_csv(prod.replace('53', '68') + '/' + filename, index=False)

        # Provincial
        if 'provincia' in file:
            # print(df.columns)
            # standardize
            df.rename(columns={'codigo_provincia': 'provincia'}, inplace=True)
            df = normalizaNombreCodigoRegionYProvincia(df)
            if 'region' in df.columns:
                df.drop(columns=['region'], inplace=True)
            if 'provincia' in df.columns:
                df.drop(columns=['provincia'], inplace=True)
            regionName(df)
            # write
            if 'confirmados_' in file:
                p53_files.append(file)
                df.to_csv(prod + '/' + filename, index=False)
            if 'r.' in file:
                p54_files.append(file)
                df.to_csv(prod.replace('53', '54') + '/' + filename, index=False)
            if 'Positividad' in file:
                p55_files.append(file)
                df.to_csv(prod.replace('53', '55') + '/' + filename, index=False)
            if 'prob48' in file:
                p56_files.append(file)
                df.to_csv(prod.replace('53', '56') + '/' + filename, index=False)
            if 'tasa test semanal' in file:
                p68_files.append(file)
                df.to_csv(prod.replace('53', '68') + '/' + filename, index=False)
            if 'carga.' and 'ajustada' in file:
                p69_files.append(file)
                df.to_csv(prod.replace('53', '69') + '/' + filename, index=False)
            if 'total72.' in file:
                p70_files.append(file)
                df.to_csv(prod.replace('53', '70') + '/' + filename, index=False)
            if 'not48.' in file:
                p71_files.append(file)
                df.to_csv(prod.replace('53', '71') + '/' + filename, index=False)
            if 'lab24.' in file:
                p72_files.append(file)
                df.to_csv(prod.replace('53', '72') + '/' + filename, index=False)

        # Regional
        if 'region' in file:
            # print(df.columns)
            df.rename(columns={'codigo_region': 'region'}, inplace=True)
            df = normalizaNombreCodigoRegion(df)
            df.drop(columns=['region'], inplace=True)
            regionName(df)
            if 'confirmados_' in file:
                p53_files.append(file)
                df.to_csv(prod + '/' + filename, index=False)
            if 'r.' in file:
                p54_files.append(file)
                df.to_csv(prod.replace('53', '54') + '/' + filename, index=False)
            if 'Positividad' in file:
                p55_files.append(file)
                df.to_csv(prod.replace('53', '55') + '/' + filename, index=False)
            if 'prob48' in file:
                p56_files.append(file)
                df.to_csv(prod.replace('53', '56') + '/' + filename, index=False)
            if 'tasa test semanal' in file:
                p68_files.append(file)
                df.to_csv(prod.replace('53', '68') + '/' + filename, index=False)
            if 'carga' and 'ajustada' in file:
                p69_files.append(file)
                df.to_csv(prod.replace('53', '69') + '/' + filename, index=False)
            if 'total72.' in file:
                p70_files.append(file)
                df.to_csv(prod.replace('53', '70') + '/' + filename, index=False)
            if 'not48.' in file:
                p71_files.append(file)
                df.to_csv(prod.replace('53', '71') + '/' + filename, index=False)
            if 'lab24.' in file:
                p72_files.append(file)
                df.to_csv(prod.replace('53', '72') + '/' + filename, index=False)
            if 'incidencia_edad' in file:
                p73_files.append(file)
                df.to_csv(prod.replace('53', '73') + '/' + filename, index=False)

        # Nacional
        if 'nacional' in file:
            # print(df.columns)
            if 'confirmados_' in file:
                p53_files.append(file)
                df.to_csv(prod + '/' + filename, index=False)
            if 'r.' in file:
                p54_files.append(file)
                df.to_csv(prod.replace('53', '54') + '/' + filename, index=False)
            if 'Positividad' in file:
                p55_files.append(file)
                df.to_csv(prod.replace('53', '55') + '/' + filename, index=False)
            if 'prob48' in file:
                p56_files.append(file)
                df.to_csv(prod.replace('53', '56') + '/' + filename, index=False)
            if 'tasa test semanal' in file:
                p68_files.append(file)
                df.to_csv(prod.replace('53', '68') + '/' + filename, index=False)
            if 'carga.' and 'ajustada' in file:
                p69_files.append(file)
                df.to_csv(prod.replace('53', '69') + '/' + filename, index=False)
            if 'total72.' in file:
                p70_files.append(file)
                df.to_csv(prod.replace('53', '70') + '/' + filename, index=False)
            if 'not48.' in file:
                p71_files.append(file)
                df.to_csv(prod.replace('53', '71') + '/' + filename, index=False)
            if 'lab24.' in file:
                p72_files.append(file)
                df.to_csv(prod.replace('53', '72') + '/' + filename, index=False)
            if 'incidencia_edad' in file:
                p73_files.append(file)
                df.to_csv(prod.replace('53', '73') + '/' + filename, index=False)
        ## SS
        if 'ss.csv' or 'ss.ajustada.csv' in file:
            if 'confirmados_' in file:
                p53_files.append(file)
                df.to_csv(prod + '/' + filename, index=False)
            if 'r.' in file:
                p54_files.append(file)
                df.to_csv(prod.replace('53', '54') + '/' + filename, index=False)
            if 'carga.'  and 'ajustada' in file:
                p69_files.append(file)
                df.to_csv(prod.replace('53', '69') + '/' + filename, index=False)


    ## Report what we've done
    print('Producto 53 files: ' + str(p53_files))
    print('Producto 54 files: ' + str(p54_files))
    print('Producto 55 files: ' + str(p55_files))
    print('Producto 56 files: ' + str(p56_files))
    print('Producto 68 files: ' + str(p68_files))
    print('Producto 69 files: ' + str(p69_files))
    print('Producto 70 files: ' + str(p70_files))
    print('Producto 71 files: ' + str(p71_files))
    print('Producto 72 files: ' + str(p72_files))
    print('Producto 73 files: ' + str(p73_files))

    not_processed = [x for x in glob.glob(fte + '/*') if x not in (p53_files +
                                                                   p54_files +
                                                                   p55_files +
                                                                   p56_files +
                                                                   p68_files +
                                                                   p69_files +
                                                                   p70_files +
                                                                   p71_files +
                                                                   p72_files +
                                                                   p73_files)
                     ]
    print('Not processed: ' + str(not_processed))

if __name__ == '__main__':
    prod53('../input/UC', '../output/producto53')
