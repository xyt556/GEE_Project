# geemap

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://gishub.org/geemap-colab)
[![image](https://binder.pangeo.io/badge_logo.svg)](https://gishub.org/geemap-pangeo)
[![image](https://mybinder.org/badge_logo.svg)](https://gishub.org/geemap-binder)
[![image](https://img.shields.io/pypi/v/geemap.svg)](https://pypi.python.org/pypi/geemap)
[![image](https://img.shields.io/conda/vn/conda-forge/geemap.svg)](https://anaconda.org/conda-forge/geemap)
[![image](https://pepy.tech/badge/geemap)](https://pepy.tech/project/geemap)
[![image](https://readthedocs.org/projects/geemap/badge/?version=latest)](https://geemap.org/geemap)
[![image](https://img.shields.io/badge/YouTube-GEE%20Tutorials-red)](https://gishub.org/geemap)
[![image](https://img.shields.io/twitter/follow/giswqs?style=social)](https://twitter.com/giswqs)
[![image](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## YouTube Channel

More video tutorials for geemap and Earth Engine are available on my [YouTube channel](https://www.youtube.com/c/QiushengWu). If you can't access YouTube in your country, you can try [西瓜视频](http://gishub.org/xigua) or [哔哩哔哩](https://space.bilibili.com/527404442)。

[![Earth Engine Tutorials on YouTube](https://wetlands.io/file/images/youtube.png)](https://www.youtube.com/c/QiushengWu)

## Tutorials

1. [Introducing the geemap Python package for interactive mapping with Google Earth Engine](#1-introducing-the-geemap-python-package-for-interactive-mapping-with-google-earth-engine) ([video](https://youtu.be/h0pz3S6Tvx0) | [gif](https://i.imgur.com/pI39k7v.gif) | [notebook](https://geemap.org/notebooks/01_geemap_intro))
2. [Using basemaps in geemap and ipyleaflet for interactive mapping with Google Earth Engine](#2-using-basemaps-in-geemap-and-ipyleaflet-for-interactive-mapping-with-google-earth-engine) ([video](https://youtu.be/6J5ZCIUPXfI) | [gif](https://i.imgur.com/P5B2f7p.gif) | [notebook](https://geemap.org/notebooks/02_using_basemaps))
3. [Introducing the Inspector tool for Earth Engine Python API](#3-introducing-the-inspector-tool-for-earth-engine-python-api) ([video](https://youtu.be/k477ksjkaXw) | [gif](https://i.imgur.com/8d77gtI.gif) | [notebook](https://geemap.org/notebooks/03_inspector_tool))
4. [Creating a split-panel map for visualizing Earth Engine data](#4-creating-a-split-panel-map-for-visualizing-earth-engine-data) ([video](https://youtu.be/9EUTX8j-YVM) | [gif](https://i.imgur.com/kql7pC3.gif) | [notebook](https://geemap.org/notebooks/04_split_panel_map))
5. [Using drawing tools to interact with Earth Engine data](#5-using-drawing-tools-to-interact-with-earth-engine-data) ([video](https://youtu.be/N7rK2aV1R4c) | [gif](https://i.imgur.com/Lm5pDUr.gif) | [notebook](https://geemap.org/notebooks/05_drawing_tools))
6. [Creating an interactive map with a marker cluster](#6-creating-an-interactive-map-with-a-marker-cluster) ([video](https://youtu.be/4HycJPrwpuo) | [gif](https://i.imgur.com/GF4cOqh.gif) | [notebook](https://geemap.org/notebooks/06_marker_cluster))
7. [Converting data formats between GeoJSON and Earth Engine](#7-converting-data-formats-between-geojson-and-earth-engine) ([video](https://youtu.be/DbK_SRgrCHw) | [gif](https://i.imgur.com/hVPmUG1.gif) | [notebook](https://geemap.org/notebooks/07_geojson))
8. [Automated conversion from Earth Engine JavaScripts to Python scripts and Jupyter notebooks](#8-automated-conversion-from-earth-engine-javascripts-to-python-scripts-and-jupyter-notebooks) ([video](https://youtu.be/RpIaalFk4H8) | [gif](https://i.imgur.com/BW0zJnN.gif) | [notebook](https://geemap.org/notebooks/08_ee_js_to_ipynb))
9. [Interactive plotting of Earth Engine data with minimal coding](#9-interactive-plotting-of-earth-engine-data-with-minimal-coding) ([video](https://youtu.be/PDab8mkAFL0) | [gif](https://i.imgur.com/iGMRnRb.gif) | [notebook](https://geemap.org/notebooks/09_plotting))
10. [Using shapefiles with Earth Engine without having to upload data to GEE](#10-using-shapefiles-with-earth-engine-without-having-to-upload-data-to-gee) ([video](https://youtu.be/OlNlqfj4uHo) | [gif](https://i.imgur.com/W3vNSdX.gif) | [notebook](https://geemap.org/notebooks/10_shapefiles))
11. [Exporting Earth Engine Image and ImageCollection as GeoTIFF and Numpy array](#11-exporting-earth-engine-image-and-imagecollection-as-geotiff-and-numpy-array) ([video](https://youtu.be/_6JOA-iiEGU) | [gif](https://i.imgur.com/RonLr0j.gif) | [notebook](https://geemap.org/notebooks/11_export_image))
12. [Computing zonal statistics with Earth Engine and exporting results as CSV or shapefile](#12-computing-zonal-statistics-with-earth-engine-and-exporting-results-as-csv-or-shapefile) ([video](https://youtu.be/ou-Xm3CLitM) | [gif](https://i.imgur.com/8xmUitW.gif) | [notebook](https://geemap.org/notebooks/12_zonal_statistics))
13. [Calculating zonal statistics by group (e.g., analyzing land cover composition of each country/state)](#13-calculating-zonal-statistics-by-group-eg-analyzing-land-cover-composition-of-each-countrystate) ([video](https://youtu.be/cORcGGH03gg) | [gif](https://i.imgur.com/LxD2em9.gif) | [notebook](https://geemap.org/notebooks/13_zonal_statistics_by_group))
14. [Adding a customized legend for Earth Engine data](#14-adding-a-customized-legend-for-earth-engine-data) ([video](https://youtu.be/NwnW_qOkNRw) | [gif](https://i.imgur.com/idkZHQp.gif) | [notebook](https://geemap.org/notebooks/14_legends))
15. [Converting Earth Engine JavaScripts to Python code directly within Jupyter notebook](#15-converting-earth-engine-javascripts-to-python-code-directly-within-jupyter-notebook) ([video](https://youtu.be/nAzZjKKd4w0) | [gif](https://i.imgur.com/aGCBWSV.gif) | [notebook](https://geemap.org/notebooks/15_convert_js_to_py))
16. [Adding animated text to GIF images generated from Earth Engine data](#16-adding-animated-text-to-gif-images-generated-from-earth-engine-data) ([video](https://youtu.be/fDnDVuM_Ke4) | [gif](https://i.imgur.com/MSde1om.gif) | [notebook](https://geemap.org/notebooks/16_add_animated_text))
17. [Adding colorbar and images to GIF animations generated from Earth Engine data](#17-adding-colorbar-and-images-to-gif-animations-generated-from-earth-engine-data) ([video](https://youtu.be/CpT3LQPNKJs) | [gif](https://i.imgur.com/13tFMSI.gif) | [notebook](https://geemap.org/notebooks/17_add_colorbar_to_gif))
18. [Creating Landsat timelapse animations with animated text using Earth Engine](#18-creating-landsat-timelapse-animations-with-animated-text-using-earth-engine) ([video](https://youtu.be/OwjSJnGWKJs) | [gif](https://i.imgur.com/XOHOeXk.gif) | [notebook](https://geemap.org/notebooks/18_create_landsat_timelapse))
19. [How to search and import datasets from Earth Engine Data Catalog](#19-how-to-search-and-import-datasets-from-earth-engine-data-catalog) ([video](https://youtu.be/lwtgzrHrXj8) | [gif](https://i.imgur.com/E09p64F.gif) | [notebook](https://geemap.org/notebooks/19_search_places_and_datasets))
20. [Using timeseries inspector to visualize landscape changes over time](#20-using-timeseries-inspector-to-visualize-landscape-changes-over-time) ([video](https://youtu.be/0CZ7Aj8hCyo) | [gif](https://i.imgur.com/61wbRjK.gif) | [notebook](https://geemap.org/notebooks/20_timeseries_inspector))
21. [Exporting Earth Engine maps as HTML files and PNG images](#21-exporting-earth-engine-maps-as-html-files-and-png-images) ([video](https://youtu.be/GWMvaNQz3kY) | [gif](https://i.imgur.com/rJuXH4a.gif) | [notebook](https://geemap.org/notebooks/21_export_map_to_html_png))
22. [How to import Earth Engine Python scripts into Jupyter notebook?](#22-how-to-import-earth-engine-python-scripts-into-jupyter-notebook) ([video](https://youtu.be/V7CbB9W41w8) | [gif](https://i.imgur.com/WwJoBHF.gif) | [notebook](https://geemap.org/notebooks/22_import_scripts))
23. [How to search Earth Engine API and import assets from GEE personal account?](#23-how-to-search-earth-engine-api-and-import-assets-from-gee-personal-account) ([video](https://youtu.be/c9VJ_uRYSkw) | [gif](https://i.imgur.com/b1auzkr.gif) | [notebook](https://geemap.org/notebooks/22_import_assets))
24. [How to publish interactive Earth Engine maps?](#24-how-to-publish-interactive-earth-engine-maps) ([video](https://youtu.be/NNrrLBIqroY) | [gif](https://i.imgur.com/Hpfzazk.gif) | [notebook](https://geemap.org/notebooks/24_publish_maps))
25. [How to load local raster datasets with geemap?](#25-how-to-load-local-raster-datasets-with-geemap) ([video](https://youtu.be/6XIehAnoazk) | [gif](https://i.imgur.com/nsqEt2O.gif) | [notebook](https://geemap.org/notebooks/25_load_rasters))
26. [How to create and deploy Earth Engine Apps using Python?](https://i.imgur.com/Hpfzazk.gif) ([video](https://youtu.be/nsIjfD83ggA) | [gif](https://i.imgur.com/Hpfzazk.gif) | [notebook](https://geemap.org/notebooks/26_heroku))
27. [How to create an interactive Earth Engine App for creating Landsat timelapse?](https://i.imgur.com/doHfnKp.gif) ([video](https://youtu.be/whIXudC6r_s) | [gif](https://i.imgur.com/doHfnKp.gif) | [notebook](https://geemap.org/notebooks/27_timelapse_app))
28. [How to use your local computer as a web server for hosting Earth Engine Apps?](https://i.imgur.com/q0sJSyi.gif) ([video](https://youtu.be/eRDZBVJcNCk) | [gif](https://i.imgur.com/q0sJSyi.gif) | [notebook](https://geemap.org/notebooks/28_voila))
29. [How to use pydeck for rendering Earth Engine data](https://i.imgur.com/HjFB95l.gif) ([video](https://youtu.be/EIkEH4okFF4) | [gif](https://i.imgur.com/HjFB95l.gif) | [notebook](https://geemap.org/notebooks/29_pydeck))
30. [How to get image basic properties and descriptive statistics](https://i.imgur.com/3B6YhkI.gif) ([video](https://youtu.be/eixBPPWgWs8) | [gif](https://i.imgur.com/3B6YhkI.gif) | [notebook](https://geemap.org/notebooks/30_image_props_stats))
31. [Machine Learning with Earth Engine - Unsupervised Classification](https://i.imgur.com/uNQfrFx.gif) ([video](https://youtu.be/k9MEy2awVJQ) | [gif](https://i.imgur.com/uNQfrFx.gif) | [notebook](https://geemap.org/notebooks/31_unsupervised_classification))
32. [Machine Learning with Earth Engine - Supervised Classification](https://i.imgur.com/jJ2Xiu6.gif) ([video](https://youtu.be/qWaEfgWi21o) | [gif](https://i.imgur.com/jJ2Xiu6.gif) | [notebook](https://geemap.org/notebooks/32_supervised_classification))
33. [Machine Learning with Earth Engine - Performing Accuracy Assessment for Image Classification](https://i.imgur.com/1JkIrF3.gif) ([video](https://youtu.be/JYptiw-I8dc) | [gif](https://i.imgur.com/1JkIrF3.gif) | [notebook](https://geemap.org/notebooks/33_accuracy_assessment))
34. [Interactive extraction of pixel values and interactive region reduction](https://i.imgur.com/LXRqSTu.gif) ([video](https://t.co/D0NC63KgF3) | [gif](https://i.imgur.com/LXRqSTu.gif) | [notebook](https://geemap.org/notebooks/34_extract_values))
35. How to use geemap and Earth Engine in Google Colab ([video](https://youtu.be/fG6kx9vq7hs) | [gif](https://i.imgur.com/OJCasMe.gif) | [notebook](https://geemap.org/notebooks/35_geemap_colab))
36. How to find out the greenest day of the year ([video](https://youtu.be/9KEaW4Ks5fQ) | [gif](https://i.imgur.com/eLDeb4t.gif) | [notebook](https://geemap.org/notebooks/36_quality_mosaic))
37. How to use Earth Engine with pydeck for 3D terrain visualization ([video](https://youtu.be/4E3zOP3-md8) | [gif](https://i.imgur.com/Gx7Y015.gif) | [notebook](https://geemap.org/notebooks/37_pydeck_3d))
38. How to use Cloud Optimized GeoTIFF with Earth Engine ([video](https://youtu.be/2P2PGSMj-wM) | [gif](https://i.imgur.com/z2mfrrZ.gif) | [notebook](https://geemap.org/notebooks/38_cloud_geotiff))
39. How to create Landsat timelapse animations without coding ([video](https://youtu.be/ab0oUhnd_7U) | [gif](https://i.imgur.com/7eyMcZQ.gif) | [notebook](https://geemap.org/notebooks/39_timelapse))
40. How to add interactive widgets to the map ([video](https://youtu.be/KsIxGq6cHtw) | [gif](https://i.imgur.com/peRZZjj.gif) | [notebook](https://geemap.org/notebooks/40_ipywidgets))
41. How to develop an Earth Engine app for mapping surface water dynamics ([video](https://youtu.be/fHdwV3LEMYo) | [gif](https://i.imgur.com/GUWSVZs.gif) | [notebook](https://geemap.org/notebooks/41_water_app))
42. How to upload data to Earth Engine Apps using ipywidgets ([video](https://youtu.be/4-WeaiObj84) | [gif](https://i.imgur.com/INLzqdw.gif) | [notebook](https://geemap.org/notebooks/42_upload_data))
43. How to extract pixel values from an Earth Engine image using a point shapefile ([video](https://youtu.be/UbQ8jyc4VP4) | [gif](https://i.imgur.com/pbt6neQ.gif) | [notebook](https://geemap.org/notebooks/43_extract_values_to_points))
44. How to use Cloud Optimized GeoTIFF (COG) and SpatioTemporal Asset Catalog (STAC) ([video](https://youtu.be/yLlYoy01RxA) | [gif](https://i.imgur.com/XjG3zYq.gif) | [notebook](https://geemap.org/notebooks/44_cog_stac))
45. How to load a virtual mosaic of Cloud Optimized GeoTIFFs (COG) ([video](https://youtu.be/jDUaopr0Dhg) | [gif](https://i.imgur.com/My8Ksh7.gif) | [notebook](https://geemap.org/notebooks/45_cog_mosaic))
46. How to use locally trained machine learning models with Earth Engine ([video](https://youtu.be/nq_Ro7E0b6E) | [gif](https://i.imgur.com/muwDfkC.gif) | [notebook](https://geemap.org/notebooks/46_local_rf_training))
47. How to download image thumbnails from Earth Engine ([video](https://youtu.be/qwXZDSbfyE8) | [gif](https://i.imgur.com/gqr7CNz.gif) | [notebook](https://geemap.org/notebooks/47_image_thumbnails))
48. How to add a draggable legend to folium maps ([video](https://youtu.be/-rO1MztlLMo) | [gif](https://i.imgur.com/i2Bye9X.gif) | [notebook](https://geemap.org/notebooks/48_folium_legend))
49. How to add a colorbar to the map ([video](https://youtu.be/qiKns09X1Ao) | [gif](https://i.imgur.com/VpMq8M9.gif) | [notebook](https://geemap.org/notebooks/49_colorbar))
50. How to create publication quality maps using cartoee ([video](https://youtu.be/t24_lpYA1ko) | [gif](https://i.imgur.com/fwCzZTi.gif) | [notebook](https://geemap.org/notebooks/50_cartoee_quickstart))
51. How to create publication quality maps with custom projections ([video](https://youtu.be/3dS2EkAuAxM) | [gif](https://i.imgur.com/vvvF94j.gif) | [notebook](https://geemap.org/notebooks/51_cartoee_projections))
52. How to create timelapse animations with custom projection, scale bar, and north arrow ([video](https://youtu.be/ejuugljSut4) | [gif](https://i.imgur.com/MVQFyHN.gif) | [notebook](https://geemap.org/notebooks/52_cartoee_gif))
53. How to change layer visualization interactively with a GUI ([video](https://youtu.be/4E7gg6yaHBg) | [gif](https://i.imgur.com/VqqlMSK.gif) | [notebook](https://geemap.org/notebooks/53_layer_vis))
54. Visualizing Earth Engine vector data interactively with a GUI ([video](https://youtu.be/SIMnvbn8d-4) | [gif](https://youtu.be/F7xa5OaweY0) | [notebook](https://geemap.org/notebooks/54_vector_vis))
55. Visualizing Earth Engine raster data interactively with a GUI ([video](https://youtu.be/2R3933NFIa0) | [gif](https://youtu.be/6HFGvyXOXJM) | [notebook](https://geemap.org/notebooks/55_raster_vis))
56. Loading local vector and raster data to geemap without coding ([video](https://youtu.be/Zhwz0uS4Xi0) | [gif](https://youtu.be/SWLpnYnsqMw) | [notebook](https://geemap.org/notebooks/56_local_data))
57. Creating publication-quality maps with multiple Earth Engine layers ([video](https://youtu.be/v-FWj9dAMJ8) | [gif](https://youtu.be/85Cu3cVLmOY) | [notebook](https://geemap.org/notebooks/57_cartoee_blend))
58. Loading vector data (e.g., shp, kml, geojson) to the map without coding ([video](https://youtu.be/10KA7uhEWUM) | [gif](https://youtu.be/UsmigaIDNpE) | [notebook](https://geemap.org/notebooks/58_add_vector))
59. Using whitebox with geemap ([video](https://youtu.be/n8ODeZpuyCE) | gif | [notebook](https://geemap.org/notebooks/59_whitebox))
60. Visualizing Earth Engine data with over 200 colormaps through dot notation ([video](https://youtu.be/RBCf7wgK3Cg) | gif | [notebook](https://geemap.org/notebooks/60_colormaps))
61. Adding a scale bar to a cartoee map (video | gif | [notebook](https://geemap.org/notebooks/61_cartoee_scalebar))
62. Using the time slider for visualizing Earth Engine time-series images ([video](https://youtu.be/w_nWkNz8fyI) | gif | [notebook](https://geemap.org/notebooks/62_time_slider))
63. Creating interactive charts from Earth Engine data (video | [gif](https://youtu.be/e-GTdUUc8N8) | [notebook](https://geemap.org/notebooks/63_charts))
64. Accessing the Earth Engine Data Catalog via dot notation with autocompletion (video | [gif](https://youtu.be/hGbs2cl7otk) | [notebook](https://geemap.org/notebooks/64_data_catalog))
65. Styling Earth Engine vector data (video | gif | [notebook](https://geemap.org/notebooks/65_vector_styling))
66. Adding a legend to publication quality maps using cartoee (video | gif | [notebook](https://geemap.org/notebooks/66_cartoee_legend))
67. Creating training samples for machine learning and supervised image classification (video | [gif](https://youtu.be/VWh5PxXPZw0) | [notebook](https://geemap.org/notebooks/67_training_samples))
68. Converting NetCDF to Earth Engine Image (video | gif | [notebook](https://geemap.org/notebooks/68_netcdf_to_ee))
69. Plotting Earth Engine vector data with cartoee (video | [gif](https://youtu.be/Gr6GBuBWnnk) | [notebook](https://geemap.org/notebooks/69_cartoee_vector))
70. Creating linked maps with a few lines of code (video | [gif](https://youtu.be/AFUGje3VWM8) | [notebook](https://geemap.org/notebooks/70_linked_maps))
71. Creating Landsat timelapse animations with a few clicks (video | [gif](https://youtu.be/mA21Us_3m28) | [notebook](https://geemap.org/notebooks/71_timelapse))
72. Creating time-series cloud-free composites with a few clicks (video | [gif](https://youtu.be/kEltQkNia6o) | [notebook](https://geemap.org/notebooks/72_time_slider_gui))
73. Generating transects along lines with Earth Engine without coding (video | [gif](https://youtu.be/0TNXSs6fwrg) | [notebook](https://geemap.org/notebooks/73_transect))
74. Creating points from CSV without coding (video | gif | [notebook](https://geemap.org/notebooks/74_csv_to_points))
75. Visualizing land cover change with inteactive Sankey diagrams (video | gif | [notebook](https://geemap.org/notebooks/74_sankee))
76. Downloading and visualizing OpenStreetMap data (video | gif | [notebook](https://geemap.org/notebooks/76_osm_to_ee))
77. Adding Planet global monthly and quarterly mosaic (video | gif | [notebook](https://geemap.org/notebooks/77_planet_imagery))
78. Using timeseries inspector with one click (video | [gif](https://i.imgur.com/s1GoEOV.gif) | [notebook](https://geemap.org/notebooks/78_ts_inspector))

### 1. Introducing the geemap Python package for interactive mapping with Google Earth Engine

![Intro geemap](https://i.imgur.com/pI39k7v.gif)

### 2. Using basemaps in geemap and ipyleaflet for interactive mapping with Google Earth Engine

![basemaps](https://i.imgur.com/P5B2f7p.gif)

### 3. Introducing the Inspector tool for Earth Engine Python API

![Inspector tool](https://i.imgur.com/8d77gtI.gif)

### 4. Creating a split-panel map for visualizing Earth Engine data

![Split panel](https://i.imgur.com/kql7pC3.gif)

### 5. Using drawing tools to interact with Earth Engine data

![Drawing tools](https://i.imgur.com/Lm5pDUr.gif)

### 6. Creating an interactive map with a marker cluster

![Marker cluster](https://i.imgur.com/GF4cOqh.gif)

### 7. Converting data formats between GeoJSON and Earth Engine

![GeoJSON](https://i.imgur.com/hVPmUG1.gif)

### 8. Automated conversion from Earth Engine JavaScripts to Python scripts and Jupyter notebooks

![Conversion](https://i.imgur.com/BW0zJnN.gif)

### 9. Interactive plotting of Earth Engine data with minimal coding

![Plotting](https://i.imgur.com/iGMRnRb.gif)

### 10. Using shapefiles with Earth Engine without having to upload data to GEE

![shapefile](https://i.imgur.com/W3vNSdX.gif)

### 11. Exporting Earth Engine Image and ImageCollection as GeoTIFF and Numpy array

![exporting](https://i.imgur.com/RonLr0j.gif)

### 12. Computing zonal statistics with Earth Engine and exporting results as CSV or shapefile

![zonal](https://i.imgur.com/8xmUitW.gif)

### 13. Calculating zonal statistics by group (e.g., analyzing land cover composition of each country/state)

![zonal by group](https://i.imgur.com/LxD2em9.gif)

### 14. Adding a customized legend for Earth Engine data

![legend](https://i.imgur.com/idkZHQp.gif)

### 15. Converting Earth Engine JavaScripts to Python code directly within Jupyter notebook

![js-py](https://i.imgur.com/aGCBWSV.gif)

### 16. Adding animated text to GIF images generated from Earth Engine data

![animated text](https://i.imgur.com/MSde1om.gif)

### 17. Adding colorbar and images to GIF animations generated from Earth Engine data

![logo](https://i.imgur.com/13tFMSI.gif)

### 18. Creating Landsat timelapse animations with animated text using Earth Engine

![timelapse](https://i.imgur.com/XOHOeXk.gif)

### 19. How to search and import datasets from Earth Engine Data Catalog

![search](https://i.imgur.com/E09p64F.gif)

### 20. Using timeseries inspector to visualize landscape changes over time

![ts inspector](https://i.imgur.com/61wbRjK.gif)

### 21. Exporting Earth Engine maps as HTML files and PNG images

![export html](https://i.imgur.com/rJuXH4a.gif)

### 22. How to import Earth Engine Python scripts into Jupyter notebook?

![import scripts](https://i.imgur.com/WwJoBHF.gif)

### 23. How to search Earth Engine API and import assets from GEE personal account?

![import assets](https://i.imgur.com/b1auzkr.gif)

### 24. How to publish interactive Earth Engine maps?

![publish maps](https://i.imgur.com/Hpfzazk.gif)

### 25. How to load local raster datasets with geemap?

![load rasters](https://i.imgur.com/nsqEt2O.gif)
