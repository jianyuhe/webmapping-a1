
from django.core.serializers import serialize, json
from django.http import HttpResponse
from django.shortcuts import render

from .models import shop


def mapleaf(request):
    dt = serialize('geojson', shop.objects.all())
    return render(request, 'map.html',{'loca': dt})


def data(request):
    points_as_geojson = serialize('geojson', shop.objects.all())
    return HttpResponse(points_as_geojson, content_type='json')



