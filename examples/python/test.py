import geemap
from ipyleaflet import VideoOverlay
geemap.set_proxy(port=7890)

Map = geemap.Map(center=(40, -100), zoom=4)
print(map)
Map.add_basemap('HYBRID')
basemaps = geemap.basemaps
for basemap in basemaps:
    print(basemap)
Map.add_basemap('OpenTopoMap')