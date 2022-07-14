import folium
from utils.data import PandasData
from utils.functoins import color_picker, change_radius

if __name__ == '__main__':
    map = folium.Map(location=[49.41963408010136, 31.45696761268942], tiles="OpenStreetMap", zoom_start=6.5)
    fg = folium.FeatureGroup(name='My map')

    for lt, ln, pop in zip(PandasData.LAT, PandasData.LNG, PandasData.POPULATION):
        fg.add_child(folium.CircleMarker(location=[lt, ln], radius=change_radius(pop), popup=f"Population: {pop}",
                    fill=True, fill_color=color_picker(pop), color='grey', fill_opacity=0.7))


    map.add_child(fg)

    map.save("map.html")