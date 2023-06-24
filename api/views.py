from rest_framework import viewsets
from .models import Book, Reaction
from .serializers import BookSerializer, ReactionSerializer
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def heart_clicks(self, request, pk=None):
        book = self.get_object()
        book.heart_clicks += 1
        print('Here we are')
        book.save()
        return JsonResponse({'status': 'click recorded'})
    

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer

    @action(detail=True, methods=['post', 'get'])
    def heart_clicks(self, request, pk=None):
        if request.method == 'POST':
            print(f'''request: {request}''')
        reaction = self.get_object()
        reaction.counts += 1
        reaction.user_id = 12
        reaction.action = 'heart'
        reaction.save()
        data = {
            'status': 'click recorded',
            'counts': reaction.counts,
        }
        return JsonResponse(data)