import folium
from folium.features import CustomIcon
from shapely.wkt import loads
import pandas as pd
import geopandas as gpd


tmp_df = pd.read_csv('test_db.csv', dtype={
                     'store_point': str, 'geometry': str})
tmp_df.geometry = tmp_df.geometry.map(lambda x: loads(x))


#tmp_df.store_point = tmp_df.store_point.map(lambda x: loads(x))
#geometry = tmp_df['store_point'].map(loads)
#tmp_df = tmp_df.drop('store_point', axis=1)
#crs = {'init': 'epsg:4326'}
#xolo_gdf = gpd.GeoDataFrame(tmp_df, crs=crs, geometry=tmp_df.geometry)

tmp_df['style'] = [
    {'fillColor': '#1f77b4', 'weight': 1, 'color': '#1f77b4', 'fillOpacity': 0.3},
    {'fillColor': '#ff7f0e', 'weight': 1, 'color': '#ff7f0e', 'fillOpacity': 0.3},
    {'fillColor': '#2ca02c', 'weight': 1, 'color': '#2ca02c', 'fillOpacity': 0.3},
    {'fillColor': '#d62728', 'weight': 1, 'color': '#d62728', 'fillOpacity': 0.3},
    {'fillColor': '#9467bd', 'weight': 1, 'color': '#9467bd', 'fillOpacity': 0.3},
    {'fillColor': '#17becf', 'weight': 1, 'color': '#17becf', 'fillOpacity': 0.3},
    {'fillColor': '#bcbd22', 'weight': 1, 'color': '#bcbd22', 'fillOpacity': 0.3},
    {'fillColor': '#c81818', 'weight': 1, 'color': '#9467bd', 'fillOpacity': 0.3},
]

crs = {'init': 'epsg:4326'}

#xolo_gdf = gpd.GeoDataFrame(tmp_df, crs=crs, geometry=tmp_df.geometry)


c_coords = (19.419762, -99.188076)

m = folium.Map(location=c_coords, zoom_start=12)

#folium.GeoJson(xolo_gdf).add_to(m)

#logo = CustomIcon('wax_logo.png', icon_size=(20, 20))

for id, r in tmp_df.iterrows():
    icon = folium.Icon(color='red',icon='none')

    marker = folium.Marker([r['lat'], r['lon']], popup=r[
                           'suc'].title(),
                           icon=icon,
                           )

    m.add_child(marker)
#
# folium.LayerControl().add_to(m)
m.save('mapa_t1.html')
