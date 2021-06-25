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

import sys
import tweepy
import pandas as pd
import datetime



def tweeting(consumer_key, consumer_secret, my_access_token, my_access_token_secret, carrier):

    # Authentication
    my_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    my_auth.set_access_token(my_access_token, my_access_token_secret)
    my_api = tweepy.API(my_auth)


    # tweet
    if carrier == 'reportediario':
        my_positividad = pd.read_csv('../output/producto49/Positividad_Diaria_Media_T.csv')
        my_positividad_ag = pd.read_csv('../output/producto49/Positividad_Diaria_Media_Ag_T.csv')
        my_mediamovil = pd.read_csv('../output/producto75/MediaMovil_casos_nuevos_T.csv')
        my_casos_nuevos_totales = pd.read_csv('../output/producto5/TotalesNacionales_T.csv')
        casos_nuevos_totales = int(pd.to_numeric(my_casos_nuevos_totales.iloc[my_casos_nuevos_totales.index.max()][7]))
        casos_nuevos_antigeno = int(pd.to_numeric(my_casos_nuevos_totales.iloc[my_casos_nuevos_totales.index.max()][19]))
        mediamovil_nacional = int(pd.to_numeric(my_mediamovil.iloc[my_mediamovil.index.max()][17]))
        variacion_nacional = float(100*(pd.to_numeric(my_mediamovil.iloc[my_mediamovil.index.max()][17]) - pd.to_numeric(
            my_mediamovil.iloc[my_mediamovil.index.max() - 7][17]))/pd.to_numeric(my_mediamovil.iloc[my_mediamovil.index.max()][17]))
        positividad_nacional = float(100*pd.to_numeric(my_positividad.iloc[my_positividad.index.max()][5]))
        variacion_positividad = float(100*(pd.to_numeric(my_positividad.iloc[my_positividad.index.max()][5]) - pd.to_numeric(
            my_positividad.iloc[my_positividad.index.max() - 7][5]))/pd.to_numeric(my_positividad.iloc[my_positividad.index.max()][5]))
        positividad_nacional = ("%.2f" % positividad_nacional)
        positividad = float(100*pd.to_numeric(my_positividad.iloc[my_positividad.index.max()][4]))
        positividad_hoy = ("%.2f" % positividad)
        casos_nuevos = str(int(my_positividad.iloc[my_positividad.index.max()][2]))
        muestras = str(int(my_positividad.iloc[my_positividad.index.max()][1]))
        tests_antigeno = str(int(my_positividad_ag.iloc[my_positividad_ag.index.max()][1]))
        positividad_ag = float(100 * pd.to_numeric(my_positividad_ag.iloc[my_positividad_ag.index.max()][4]))
        positividad_ag_hoy = ("%.2f" % positividad_ag)

        # create update elements
        tweet_text = '🤖Actualicé el reporte diario del @ministeriosalud de hoy 💫 Gracias a la Subsecretaría de Salud Pública y de Redes Asistenciales. Hay '+str(mediamovil_nacional)+' casos nuevos promedio en los últimos 7 días, con positividad de '+str(positividad_nacional)+'%. Más detalles en los productos en la imagen.  https://github.com/MinCiencia/Datos-COVID19'
        reply2_text = '🤖El total de casos confirmados hoy es '+str(casos_nuevos_totales)+', de los cuales '+str(casos_nuevos_antigeno)+' fueron confirmados con test de antígeno y '+casos_nuevos+' con PCR+. De las '+muestras+' muestras que se analizaron en las últimas 24 horas en laboratorios nacionales, un '+positividad_hoy+'% resultó positivo.'
        reply3_text = '🤖Además, de los '+str(tests_antigeno)+ ' tests de antígeno realizados en el territorio nacional durante las últimas 24h, un '+positividad_ag_hoy+'% resultó positivo.'
        if variacion_nacional >= 0 and variacion_positividad >= 0:
            variacion_nacional = ("%.2f" % variacion_nacional)
            variacion_positividad = ("%.2f" % variacion_positividad)
            reply1_text = '🤖 En comparación con la semana anterior, la media móvil de los últimos 7 días para casos nuevos creció en '+str(variacion_nacional)+'% y la positividad en '+str(variacion_positividad)+'% a nivel nacional. Detalles a nivel regional en: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto75 y https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto49'

        elif variacion_nacional >= 0 and variacion_positividad < 0:
            variacion_nacional = ("%.2f" % variacion_nacional)
            variacion_positividad = ("%.2f" % variacion_positividad)
            reply1_text = '🤖 En comparación con la semana anterior, la media móvil de los últimos 7 días para casos nuevos creció en '+str(variacion_nacional)+'% y la positividad bajó en '+str(variacion_positividad)+'% a nivel nacional. Detalles a nivel regional en: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto75 y https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto49'

        elif variacion_nacional < 0 and variacion_positividad < 0:
            variacion_nacional = ("%.2f" % variacion_nacional)
            variacion_positividad = ("%.2f" % variacion_positividad)
            reply1_text = '🤖 En comparación con la semana anterior, la media móvil de los últimos 7 días para casos nuevos bajó en '+str(variacion_nacional)+'% y la positividad en '+str(variacion_positividad)+'% a nivel nacional. Detalles a nivel regional en: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto75 y https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto49'

        elif variacion_nacional < 0 and variacion_positividad >= 0:
            variacion_nacional = ("%.2f" % variacion_nacional)
            variacion_positividad = ("%.2f" % variacion_positividad)
            reply1_text = '🤖 En comparación con la semana anterior, la media móvil de los últimos 7 días para casos nuevos bajó en ' + str(
                variacion_nacional) + '% y la positividad aumentó en ' + str(
                variacion_positividad) + '% a nivel nacional. Detalles a nivel regional en: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto75 y https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto49'

        # Generate text tweet with media (image)
        media1= my_api.media_upload('./img/Datos covid_Bot_A_g1.png')
        media2= my_api.media_upload('./img/Datos covid_Bot_A_g2.png')
        media3= my_api.media_upload('./img/Datos covid_Bot_A_g3.png')
        media4= my_api.media_upload('./img/Datos covid_Bot_A_g4.png')
        tweet = my_api.update_status(status=tweet_text, media_ids=[media1.media_id,media2.media_id,media3.media_id,media4.media_id])
        tweet2 = my_api.update_status(status=reply1_text, in_reply_to_status_id=tweet.id)
        tweet3 = my_api.update_status(status=reply2_text, in_reply_to_status_id=tweet2.id)
        tweet3 = my_api.update_status(status=reply3_text, in_reply_to_status_id=tweet3.id)

    elif carrier == 'mmamp':
        # create update elements
        tweet_text = '🤖Actualicé los datos de calidad del aire en todo el territorio nacional, desde las estaciones del SINCA del @MMAChile 💫. Mira específicamente qué actualicé en la imagen y clona el GitHub https://github.com/MinCiencia/Datos-COVID19'
        media1= my_api.media_upload('./img/Datos covid_Bot_G_g1.png')
        # media2= my_api.media_upload('./img/Datos covid_Bot_A_g2.png')
        # media3= my_api.media_upload('./img/Datos covid_Bot_A_g3.png')
        # media4= my_api.media_upload('./img/Datos covid_Bot_A_g4.png')

        # Generate text tweet with media (image)
        my_api.update_status(status=tweet_text, media_ids=[media1.media_id])

    elif carrier == 'informeepi':
        my_epi= pd.read_csv('../output/producto1/Covid-19_T.csv')
        fecha_informe = my_epi.iloc[my_epi.index.max()-1][0]


        # create update elements
        tweet_text = '🤖Actualicé los datos del Informe Epidemiológico publicado por @ministeriosalud de hoy 💫, con los datos correspondientes al '+fecha_informe+'. Gracias al equipo de especialistas en epidemiología. Mira qué actualicé en la imagen y clona el GitHub https://github.com/MinCiencia/Datos-COVID19'
        reply1_text = '🤖A partir de este momento, todas mis respuestas sobre comunas del país 🇨🇱, corresponden al último informe. Más detalles en https://github.com/MinCiencia/Datos-COVID19'
        media1= my_api.media_upload('./img/Datos covid_Bot_B_g1.png')
        media2= my_api.media_upload('./img/Datos covid_Bot_B_g2.png')
        media3= my_api.media_upload('./img/Datos covid_Bot_B_g3.png')
        media4= my_api.media_upload('./img/Datos covid_Bot_B_g4.png')

        # Generate text tweet with media (image)
        tweet = my_api.update_status(status=tweet_text, media_ids=[media1.media_id,media2.media_id,media3.media_id,media4.media_id])
        my_api.update_status(status=reply1_text, in_reply_to_status_id=tweet.id)

    elif carrier == 'vacunacion':
        now = datetime.datetime.now()
        my_vacunacion = pd.read_csv('../output/producto76/vacunacion_t.csv')
        vacunados = int(pd.to_numeric(my_vacunacion.iloc[my_vacunacion.index.max()][1]))
        vacunados_pauta_completa = int(pd.to_numeric(my_vacunacion.iloc[my_vacunacion.index.max()][2])) + int(pd.to_numeric(my_vacunacion.iloc[my_vacunacion.index.max()][3]))
        my_vacunacion_avance = 100*vacunados/15200840
        my_vacunacion_avance_pauta_completa = 100*vacunados_pauta_completa/15200840
        my_vacunacion_avance = ("%.2f" % my_vacunacion_avance)
        my_vacunacion_avance_pauta_completa = ("%.2f" % my_vacunacion_avance_pauta_completa)
        dosis_dia = vacunados+vacunados_pauta_completa - (pd.to_numeric(my_vacunacion.iloc[my_vacunacion.index.max()-1][1]) + pd.to_numeric(my_vacunacion.iloc[my_vacunacion.index.max()-1][2]) + + pd.to_numeric(my_vacunacion.iloc[my_vacunacion.index.max()-1][3]))

        my_vacunacion = my_vacunacion[1:]
        my_vacunacion['total_dosis'] = pd.to_numeric(my_vacunacion['Total']) + pd.to_numeric(my_vacunacion['Total.1']) + pd.to_numeric(my_vacunacion['Total.2'])
        new = my_vacunacion.iloc[:my_vacunacion.index.max(), 35:]
        new.reset_index(drop=True, inplace=True)
        my_vacunacion['total_manana'] = new['total_dosis']
        my_vacunacion.reset_index(drop=True, inplace=True)
        my_vacunacion['avance_diario'] = my_vacunacion['total_manana'].fillna(0) - my_vacunacion['total_dosis']
        my_vacunacion['mediamovil'] = my_vacunacion['avance_diario'].rolling(7).mean().round(4)
        promedio_semanal = int(pd.to_numeric(my_vacunacion.iloc[my_vacunacion.index.max()-1][55]))

        # create update elements
        tweet_text = '🤖Actualicé los datos que muestran el avance en la campaña de vacunación #YoMeVacuno de hoy 💫, gracias a APS y DIPLAS, @ministeriosalud. Van '+str(vacunados)+' vacunados con primera dosis en 🇨🇱. Mira específicamente qué actualicé en la imagen y clona el github https://github.com/MinCiencia/Datos-COVID19'
        reply1_text = '🤖Además, un total de ' + str(vacunados_pauta_completa) + ' personas tienen pauta completa. En 🇨🇱, un ' + my_vacunacion_avance + '% tiene al menos una dosis, y un ' + my_vacunacion_avance_pauta_completa + '% completó su pauta de vacunación. Detalles en https://github.com/MinCiencia/Datos-COVID19'
        reply2_text = '🤖A las 9pm del '+my_vacunacion.iloc[my_vacunacion.index.max()][0]+', un total de '+str(int(dosis_dia))+' recibieron la vacuna contra COVID-19. Detalles por comuna, edad, fabricante y prioridad en https://github.com/MinCiencia/Datos-COVID19'
        reply3_text = '🤖En los últimos 7 días, un promedio de '+str(promedio_semanal)+' personas han recibido su vacuna en Chile🇨🇱 diariamente. A partir de ahora mis respuestas consideran estos datos'

        media1= my_api.media_upload('./img/Datos covid_Bot_C_g1.png')
        # media2= my_api.media_upload('./img/Datos covid_Bot_A_g2.png')
        # media3= my_api.media_upload('./img/Datos covid_Bot_A_g3.png')
        # media4= my_api.media_upload('./img/Datos covid_Bot_A_g4.png')

        # Generate text tweet with media (image)
        tweet = my_api.update_status(status=tweet_text, media_ids=[media1.media_id])
        tweet2 = my_api.update_status(status=reply1_text, in_reply_to_status_id=tweet.id)
        tweet3 = my_api.update_status(status=reply2_text, in_reply_to_status_id=tweet2.id)
        my_api.update_status(status=reply3_text, in_reply_to_status_id=tweet3.id)

    elif carrier == 'testeo':
        tweet_text = "Actualicé los datos del informe de testeo y trazabilidad del @ministeriosalud de hoy 💫, ¡gracias @HdFaviola! Mira específicamente qué actualicé en la imagen, y clónate el github https://github.com/MinCiencia/Datos-COVID19"
        media1 = my_api.media_upload('./img/Datos covid_Bot_D_g1.png')
        # media2= my_api.media_upload('./img/Datos covid_Bot_A_g2.png')
        # media3= my_api.media_upload('./img/Datos covid_Bot_A_g3.png')
        # media4= my_api.media_upload('./img/Datos covid_Bot_A_g4.png')

        # Generate text tweet with media (image)
        my_api.update_status(status=tweet_text, media_ids=[media1.media_id
                                                           # media2.media_id,
                                                           # media3.media_id,
                                                           # media4.media_id
                                                           ])

    elif carrier == 'isci':

        # create update elements
        tweet_text = '🤖Actualicé los datos de movilidad en todo el territorio nacional, gracias a @centroISCI y @EntelOcean 💫. Mira qué actualicé en la imagen y clona el GitHub https://github.com/MinCiencia/Datos-COVID19'
        media1 = my_api.media_upload('./img/Datos covid_Bot_I_g1.png')

        # Generate text tweet with media (image)
        my_api.update_status(status=tweet_text, media_ids=[media1.media_id])

    elif carrier == 'udd':
        # create update elements
        tweet_text = '🤖Actualicé los datos de movilidad en todo el territorio nacional que produce el Instituto de Data Science de @UDD_cl junto a @TelefonicaCL 💫. Mira específicamente qué actualicé en la imagen y clona el GitHub https://github.com/MinCiencia/Datos-COVID19'
        media1 = my_api.media_upload('./img/Datos covid_Bot_E_g1.png')

        # Generate text tweet with media (image)
        my_api.update_status(status=tweet_text, media_ids=[media1.media_id])

if __name__ == '__main__':

    if len(sys.argv) == 6:
        consumer_key = sys.argv[1]
        consumer_secret_key = sys.argv[2]
        my_access_token = sys.argv[3]
        my_access_token_secret = sys.argv[4]
        carrier = sys.argv[5]

        tweeting(consumer_key, consumer_secret_key, my_access_token, my_access_token_secret, carrier)
