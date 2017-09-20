import pandas as pd
import numpy as np
import folium
from folium import plugins
import csv


def export_coordsheatmap(arg):
    d = pd.read_csv('db_all_db.csv.csv')
    c1 = d.id.isin(['Acopio', 'Albergue', 'AcopioN'])
    coords = d[~c1].store_point.str.extract('(-*\d+\.\d+) (-*\d+\.\d+)')
    coords.rename(columns={0: 'lon', 1: 'lat'}, inplace=True)
    coords.to_csv('coordsheat.csv', index=False)


def export_heatmap():
    c = (19.419762, -99.188076)
    heatmap_map = folium.Map(location=c, zoom_start=12)
    f = open('coords.csv', 'r')
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        x = row['lat']
        y = row['lon']
        z = x, y
        data.append(z)

    hm = plugins.HeatMap(data)
    heatmap_map.add_child(hm)
    heatmap_map.save('heatmap.html')
