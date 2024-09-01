from django.urls import path
from .views import (
    QulaificatonsListView,
    CountriesListView,
    StateListView
    )

urlpatterns = [
    path('countries-list/', CountriesListView.as_view(), name='countries-list'),
    path('states-list/', StateListView.as_view(), name='states-list'),
    path('qualifications-list/', QulaificatonsListView.as_view(), name='qualifications-list')
]
