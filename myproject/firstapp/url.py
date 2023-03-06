from operator import index
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('vs/', views.vs, name='vs')
    # path('search/', views.search, name='search'),
    # initial or root path
]
