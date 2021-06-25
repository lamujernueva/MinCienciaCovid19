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

from utils import *

def prod57(fte, prod):
    # find separator:
    # load the first few lines, to guess the CSV dialect
    head = ''.join(itertools.islice(open(fte, encoding='ISO-8859-1'), 5))
    s = csv.Sniffer()
    my_separator = s.sniff(head).delimiter
    print('Found separator: ' + my_separator)

    df = pd.read_csv(fte, sep=my_separator, encoding='ISO-8859-1')

    df.rename(columns={'fecha_fallecimiento': 'Fecha',
                       'region_residencia': 'Region',
                       'fallecidos': 'Total',
                       'hospitalizacion': 'Hospitalizacion'},
              inplace=True)

    regionNameRegex(df)
    regionName(df)
    df.to_csv(prod + '_t.csv', index=False)

if __name__ =='__main__':
    prod57('../input/FallecidosRegional/fallecidos_hosp_region.csv', '../output/producto57/fallecidos_regionales')