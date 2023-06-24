from django.http import JsonResponse
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Property, Comment
from .serializers import PropertySerializer 
from rest_framework.parsers import MultiPartParser
from .models import privacy, Reactions

import json
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User

class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    pagination_class = PageNumberPagination

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Property, pk=pk)
        return obj
    
    @action(detail=True, methods=['post', 'get'])
    def data(self, request, pk=None):
        obj = self.get_object() # get the instance of the Property model
        serializer = PropertySerializer(obj) # pass the instance to the serializer
        
        return JsonResponse({'item': serializer.data})

class ListingView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return JsonResponse(serializer.data)




class PropertyPost(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        privac= request.data.get('privacy')
        priv = privacy.objects.get(name=privac)
        description = request.data.get('description')
        file = request.data.get('file')
        user1 = request.data.get('user')
        user = User.objects.get(username=user1)

        print(user)
        en = Property(
            description = description,
            privacy = priv,
            coverPhoto=file,
            photos=file,
            agent=user
        )
        print(en)
        en.save()
        return Response({'message': 'Post created'}, status=200)


class ReactionsPost(APIView):
    def post(self, request):
        comment = request.data.get('comment')
        agent = request.data.get('agent')
        property_id = request.data.get('property')
        user = User.objects.get(username=agent)
        property_instance = Property.objects.get(id=property_id)
        
        comment_instance = Comment(name=comment, agent=user,property=property_instance)
        comment_instance.save()
        Reactions.objects.get_or_create(property=property_instance, agent=user)

        reactions_instance, created = Reactions.objects.get_or_create(property=property_instance, agent=user)
        reactions_instance.comments += 1
        reactions_instance.save()

        return JsonResponse({'message': 'success'}, status=200)
