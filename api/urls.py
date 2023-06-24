from django.urls import include, path

from .views import my_api_view, heart_clicks

urlpatterns = [
    path('agency-list', my_api_view),
    path('heart-clicks/', heart_clicks, name='heart_clicks'),
]