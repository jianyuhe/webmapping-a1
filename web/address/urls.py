from django.views.generic import TemplateView
from django.conf.urls import url

from djgeojson.views import GeoJSONLayerView

from .models import shop
from . import views
from django.urls import path

urlpatterns = (
    url(r'^$', TemplateView.as_view(template_name='map.html'), name='home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=shop), name='data1'),
    url(r'^$', views.mapleaf)
)
