from django.urls import path
from dashboard import views, plotly_charts, bokeh_charts


urlpatterns = [
        path('', views.home, name='Home'),
        path('plotly_charts', plotly_charts.plotly_charts, name='Plotly-Charts'),
        path('bokeh_charts', bokeh_charts.bokeh_charts, name='Bokeh-Charts'),
        path('dashboard', views.dashboard, name='Dashboard'),
        path('kepler_mapping', views.kepler_mapping, name='Kepler-Mapping'),
        path('openlayers', views.openlayers, name='OpenLayers'),
        path('chartjs', views.chartjs, name='Chartjs'),
        path('d3js', views.d3js, name='D3js'),
        path('echarts', views.echarts, name='ECharts'),
        path('matplotlib_pdf', views.matplotlib_pdf, name='Matplotlib-PDF'),
        path('weasyprint_pdf', views.weasyprint_pdf, name='Weasyprint-PDF'),
        path('jspdf', views.jspdf, name='JsPDF'),
        path('html_table', views.html_table, name='HTML-Table'),
        path('data_table', views.data_table, name='Data-Table'),
        path('leaflet', views.leaflet, name='Leaflet'),
        path('stock_live', views.stock_live, name='Stock-Live'),
        path('sql_explorer', views.sql_explorer, name='SQL-Explorer'),
        path('maplibre', views.maplibre, name='MapLibre'),
]