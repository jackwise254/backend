from django.urls import include, path

from .views import PropertyListView, ListingView

urlpatterns = [
    path('properties/', PropertyListView.as_view(), name='property_list'),
    path('listings/<int:pk>', ListingView.as_view(), name='listings_list'),
]