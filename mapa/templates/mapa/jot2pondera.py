# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from os.path import exists
import unidecode as ud
from datetime import datetime as dt


def jot2pondera():
    columns = {u'Submission ID': 'id',
               u'Submission Date': 'timestamp',
               u'¿Dónde estás?': 'geo',
               u'Tipo de Reporte': 'tipo',
               u'¿Qué actividades realizará el voluntario?': 'actividad',
               u'Describe brevemente el estado de tu inmueble': 'inmueble',
               u'¿Qué necesitas acopiar?': 'acopio',
               u'¿Qué necesita el hospital?': 'hospital',
               u'Escribe brevemente qué necesitas': 'necesita',
               u'¿Cuántos Voluntarios Necesitas?': 'voluntarios',
               u'Nombre del albergue': 'nombre_albergue',
               u'¿Qué ofrece el albergue?': 'albergue',
               u'Sólo si lo necesitas, escribe un breve comentario': 'comentario',
               }
    dtypes = {u'Submission ID': int,
              u'¿Dónde estás?': str,
              u'Tipo de Reporte': str,
              u'¿Qué actividades realizará el voluntario?': str,
              u'Describe brevemente el estado de tu inmueble': str,
              u'¿Qué necesitas acopiar?': str,
              u'¿Qué necesita el hospital?': str,
              u'Escribe brevemente qué necesitas': str,
              u'¿Cuántos Voluntarios Necesitas?': str,
              u'Nombre del albergue': str,
              u'¿Qué ofrece el albergue?': str,
              u'Sólo si lo necesitas, escribe un breve comentario': str,
              }
    df = pd.read_csv('survey.csv', encoding='utf-8', parse_dates=['Submission Date'], dtype=dtypes,
                     na_values=[''])
    df.rename(columns=columns, inplace=True)
    df.replace(np.nan, ' ')
    cols = ['actividad', 'inmueble', 'acopio', 'hospital', 'necesita',
            'voluntarios', 'albergue', 'comentario']  # , 'nombre_albergue'
    df = df.where((pd.notnull(df)), '')
    for i, row in df.iterrows():
        for c in cols:
            if not isinstance(df.loc[i, c], float):
                df.loc[i, c] = ud.unidecode_expect_nonascii(df.loc[i, c])
    df.loc[:, 'lon'] = df.geo.str.extract('(\d+\.\d+).*(-\d+\.\d+)')[1]
    df.loc[:, 'lat'] = df.geo.str.extract('(\d+\.\d+).*(-\d+\.\d+)')[0]
    df.loc[:, 'store_point'] = 'POINT (' + df.lon + ' ' + df.lat + ')'
    df.loc[:, 'suc'] = ''

    for i, d in df.iterrows():
        s = str(d['timestamp']) + ' '
        if str(d['tipo'].encode('utf-8')) == 'Acopio o Solicitud in situ':
            s += 'Se necesita: ' + ' '.join([str(d['acopio'].encode('utf-8')), str(d['necesita'].encode('utf-8'))])
        elif str(d['tipo'].encode('utf-8')) == 'Acopio Hospital':
            s += 'Se necesita: ' + ' '.join([str(d['hospital']), str(d['necesita'])])
        elif str(d['tipo'].encode('utf-8')) == 'Requiero Voluntarios':
            s += 'Se necesitan ' + str(d['voluntarios']) + \
                ' voluntarios para realizar: ' + str(d['necesita'])
        elif str(d['tipo'].encode('utf-8')) == 'Dar de Alta Albergue':
            s += str(d['nombre_albergue']) + ' - características: ' + str(d['albergue'])
        elif str(d['tipo'].encode('utf-8')) == 'Dar de Alta Derrumbe':
            s += '<br>Derrumbe'
        elif str(d['tipo'].encode('utf-8')) == 'Dar de Alta Daños':
            s += '<br>Daño'
        elif str(d['tipo'].encode('utf-8')) == 'Requiero de Revisión en mi Inmueble':
            s += 'Descripción de daños: ' + str(d['inmueble'])
        s = s.replace('nan', '')
        df.loc[i, 'suc'] = str(df.loc[i, 'suc']).strip(r'\\r') + str(s).strip(r'\\r') + ' ' + str(df.loc[i,'comentario']).strip(r'\\r')
        print "jot2pondera"
        print df.loc[i,'suc']
    df.to_csv('db_jot.csv', encoding='utf-8')
