from django.urls import include, path

from .views import BlogListView

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),
]