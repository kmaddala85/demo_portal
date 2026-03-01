from django.shortcuts import render
import pandas as pd
import pygwalker as pyg
import geopandas as gpd
import shapely.geometry as geom
from keplergl import KeplerGl
import pydeck as pdk
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import os
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from django.http import FileResponse
from plotly.io import to_image
import json
from pyproj import Geod
import numpy as np

# WGS84 ellipsoid (default for lat/lon)
geod = Geod(ellps="WGS84")


def home(request):

    return render(request, 'dashboard/home.html', {
        'title': 'Welcome!',
        'page_header': 'Demo Project',
    })



# Create your views here.
def dashboard(request):

    # Create sample data for PyGWalker
    data = {
        'date': pd.date_range(start='1/1/2023', periods=100),
        'category': np.random.choice(['A', 'B', 'C'], 100),
        'value': np.random.randn(100).cumsum(),
        'lat': np.random.uniform(50, 53, 100),
        'lon': np.random.uniform(3, 7, 100)
    }
    df = pd.DataFrame(data)
    
    # Generate the PyGWalker HTML   
    pyg_html = pyg.to_html(df)
   
    return render(request, 'dashboard/dashboard.html',  {'title': 'Dashboard', 'page_header': 'Dashboard', 'pyg_html': pyg_html})


# Create your views here.
def kepler_mapping(request):

    # Create sample data for Kepler (London Coordinates)
    # London approx: Lat 51.5074, Lon -0.1278
    data = {
        'latitude': np.random.uniform(51.4, 51.6, 100),
        'longitude': np.random.uniform(-0.3, 0.1, 100),
        'value': np.random.randint(1, 100, 100)
    }
    df = pd.DataFrame(data)

    kepler_map = create_kepler_map()

    # Add data to the map
    kepler_map.add_data( data=df, name="London Demo")

    # Render the map to HTML string
    # We use center_map=True to ensure it centers on the data
    map_html = kepler_map._repr_html_(center_map=True).decode('utf-8')
    
    return render(request, 'dashboard/kepler_mapping.html', {
        'title': 'Kepler', 
        'page_header': 'Kepler', 
        'map_html': map_html
    })


def create_kepler_map():
    # Initialize Kepler map with a default height
    # We will override this with CSS in the template
    kepler_map = KeplerGl(height=600)

    # Set OpenStreetMap as the basemap style
    kepler_map.config = {
        'version': 'v1',
        'config': {
            'visState': {
                'filters': [],
                'layers': [],
                'interactionConfig': {}
            },
            'mapStyle': {
                'version': 8,
                'sources': {
                    'osm': {
                        'type': 'raster',
                        'tiles': ['https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'],
                        'tileSize': 256
                    }
                },
                'layers': [{
                    'id': 'osm-basemap',
                    'type': 'raster',
                    'source': 'osm',
                    'minzoom': 0,
                    'maxzoom': 19
                }]
            }
            # Removed hardcoded mapState so center_map=True works dynamically
        }
    }

    # Return the map object
    return kepler_map


# Create your views here.
def openlayers(request):

    # Create sample GeoJSON data for OpenLayers
    features = []
    for i in range(50):
        # Generate random points across the US
        lng = np.random.uniform(-120.0, -75.0)
        lat = np.random.uniform(30.0, 45.0)
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lng, lat]
            },
            "properties": {
                "name": f"Point {i+1}",
                "value": np.random.randint(1, 100)
            }
        })
    
    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'dashboard/openlayers.html', {
        'title': 'OpenLayers',
        'page_header': 'OpenLayers Map',
        'map_data': json.dumps(geojson_data)
    })

def chartjs(request):
    return render(request, 'dashboard/chartjs.html', {
        'title': 'Chart.js',
        'page_header': 'Chart.js Charts',
    })

def d3js(request):
    return render(request, 'dashboard/d3js.html', {
        'title': 'D3.js',
        'page_header': 'D3.js Charts',
    })

def echarts(request):
    return render(request, 'dashboard/echarts.html', {
        'title': 'ECharts',
        'page_header': 'Apache ECharts',
    })

def matplotlib_pdf(request):
    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax.set_title('Simple Plot')

    # Save the figure to a PDF buffer
    buffer = io.BytesIO()
    with PdfPages(buffer) as pdf:
        pdf.savefig(fig)
    
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='matplotlib_report.pdf')

def weasyprint_pdf(request):
    html_string = render_to_string('dashboard/pdf_template.html', {'title': 'WeasyPrint PDF'})
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()
    
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="weasyprint_report.pdf"'
    return response

def jspdf(request):
    return render(request, 'dashboard/jspdf.html', {
        'title': 'JsPDF',
        'page_header': 'JsPDF Report',
    })

def html_table(request):
    data = [
        {'id': 1, 'name': 'Item 1', 'value': 100},
        {'id': 2, 'name': 'Item 2', 'value': 200},
        {'id': 3, 'name': 'Item 3', 'value': 300},
    ]
    return render(request, 'dashboard/html_table.html', {
        'title': 'HTML Table',
        'page_header': 'HTML Table',
        'data': data
    })

def data_table(request):
    data = [
        {'id': 1, 'name': 'Item 1', 'value': 100},
        {'id': 2, 'name': 'Item 2', 'value': 200},
        {'id': 3, 'name': 'Item 3', 'value': 300},
        {'id': 4, 'name': 'Item 4', 'value': 400},
        {'id': 5, 'name': 'Item 5', 'value': 500},
    ]
    return render(request, 'dashboard/data_table.html', {
        'title': 'Data Table',
        'page_header': 'Data Table',
        'data': data
    })

def leaflet(request):
    return render(request, 'dashboard/leaflet.html', {
        'title': 'Leaflet',
        'page_header': 'Leaflet Map',
    })

def stock_live(request):
    return render(request, 'dashboard/stock_live.html', {
        'title': 'Stock Live',
        'page_header': 'Stock Live Data',
    })

def sql_explorer(request):
    return render(request, 'dashboard/sql_explorer.html', {
        'title': 'SQL Explorer',
        'page_header': 'SQL Explorer',
    })

def maplibre(request):
    # Generate sample GeoJSON data for MapLibre
    features = []
    for i in range(50):
        # Generate random points across the US
        lng = np.random.uniform(-120.0, -75.0)
        lat = np.random.uniform(30.0, 45.0)
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lng, lat]
            },
            "properties": {
                "title": f"Point {i+1}",
                "description": f"Location: {lat:.2f}, {lng:.2f}"
            }
        })
    
    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'dashboard/maplibre.html', {
        'title': 'MapLibre',
        'page_header': 'MapLibre Map',
        'map_data': json.dumps(geojson_data)
    })
