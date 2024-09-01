from django.urls import path
from .views import (
    GetRoutes
)


urlpatterns = [
    path('', GetRoutes.as_view(), name='to-get-all-routes'),


]
