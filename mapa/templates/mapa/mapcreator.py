import folium
from folium.features import CustomIcon
from shapely.wkt import loads
import pandas as pd
import geopandas as gpd
from os.path import exists

tmp_df = pd.read_csv('db_all_db.csv', dtype={
                     'store_point': str, 'geometry': str}, encoding='utf-8')
#tmp_df.geometry = tmp_df.geometry.map(lambda x: loads(x))

tmp_df.store_point = tmp_df.store_point.str.decode('utf-8')
#tmp_df.store_point = tmp_df.store_point.map(lambda x: loads(x))
#geometry = tmp_df['store_point'].map(loads)
#tmp_df = tmp_df.drop('store_point', axis=1)
#crs = {'init': 'epsg:4326'}
#xolo_gdf = gpd.GeoDataFrame(tmp_df, crs=crs, geometry=tmp_df.geometry)

crs = {'init': 'epsg:4326'}

#xolo_gdf = gpd.GeoDataFrame(tmp_df, crs=crs, geometry=tmp_df.geometry)


c_coords = (19.006626, -98.801924)

m = folium.Map(location=c_coords, zoom_start=9)

#folium.GeoJson(xolo_gdf).add_to(m)

#logo = CustomIcon('wax_logo.png', icon_size=(20, 20))

for id_, r in tmp_df.iterrows():
    color = 'white'
    if r['tipo'] == 'Derrumbe':
        color = 'red'
    elif r['tipo'] == 'Dano mayor':
        color = 'orange'
    elif r['tipo'] == 'Danos':
        color = 'lightred'
    elif r['tipo'] == 'Acopio':
        color = 'blue'
    elif r['tipo'] == 'Albergue':
        color = 'green'
    elif r['tipo'] == 'AcopioN':
        color = 'black'
    elif r['tipo'] == 'Urgente':
        color = 'white'
    elif r['id'] == 'AcopioM':
        color = 'lightblue'

    else:
        color = 'white'
    icon = folium.Icon(color=color,icon='none')
    marker = folium.Marker([r['lat'], r['lon']], popup=r[
                           'suc'].title(),
                           icon=icon,
                           )

    m.add_child(marker)
#
# folium.LayerControl().add_to(m)
m.save('mapa.html')
