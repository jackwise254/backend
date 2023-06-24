from django.shortcuts import render

from django.http import JsonResponse
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Blog
from .serializers import BlogSerializer
import json
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = PageNumberPagination

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Blog, pk=pk)
        return obj
    
    @action(detail=True, methods=['post', 'get'])
    def data(self, request, pk=None):
        obj = self.get_object() # get the instance of the Property model
        serializer = BlogSerializer(obj) # pass the instance to the serializer
        return JsonResponse({'item': serializer.data})