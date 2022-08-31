from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('all', all_collections, name='all'),
    path('add', add_collection, name='add_collection'),


    path('search', search_view, name='search'),


]
