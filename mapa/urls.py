from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
        url(r'^$', views.index),
        url(r'^mapa/', TemplateView.as_view(template_name="mapa/mapa.html"),
                   name='mapa'),
        url(r'^heatmap/', TemplateView.as_view(template_name="mapa/heatmap.html"),
                   name='heatmap'),
    ]
