from django.urls import path, re_path
from . import views

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='index'),
    path('consultar/', views.consultar, name='consultar')
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$',
            serve, {
                'document_root': settings.MEDIA_ROOT,
            }),
    ]