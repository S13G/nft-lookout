from django.urls import path

from .views import *

urlpatterns = [
    
    
    path('search-drops',search_drops_view, name='search-drops'),
    path('search-drops-date', search_by_date, name='search-drops-date'),





    path('calendar', limited_drops,  name='calendar'),
    path('calendar/drops/<day>', all_drops_by_days,  name='calendar-days'),

    path('add-calendar', add_calendar, name='add_calendar'),
]

