import folium
from folium.features import CustomIcon
from shapely.wkt import loads
import pandas as pd
import geopandas as gpd


tmp_df = pd.read_csv('db_all_db.csv', dtype={
                     'store_point': str, 'geometry': str})
#tmp_df.geometry = tmp_df.geometry.map(lambda x: loads(x))


#tmp_df.store_point = tmp_df.store_point.map(lambda x: loads(x))
#geometry = tmp_df['store_point'].map(loads)
#tmp_df = tmp_df.drop('store_point', axis=1)
#crs = {'init': 'epsg:4326'}
#xolo_gdf = gpd.GeoDataFrame(tmp_df, crs=crs, geometry=tmp_df.geometry)

crs = {'init': 'epsg:4326'}

#xolo_gdf = gpd.GeoDataFrame(tmp_df, crs=crs, geometry=tmp_df.geometry)


c_coords = (19.419762, -99.188076)

m = folium.Map(location=c_coords, zoom_start=11)

#folium.GeoJson(xolo_gdf).add_to(m)

#logo = CustomIcon('wax_logo.png', icon_size=(20, 20))

for id, r in tmp_df.iterrows():
    if r['id'] == 'Derrumbe':
        color = 'red'
    elif r['id'] == 'Acopio':
        color = 'blue'
    elif r['id'] == 'Albergue':
        color = 'lightgreen'
    elif r['id'] == 'Danos':
        color = 'yellow'
    elif r['id'] == 'Dano mayor':
        color = 'orange'
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
m.save('mapa_t1.html')
