from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login as user_login, logout as user_logout
from .serializers import UserSerializer


from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponseRedirect
import json




# commented this height 
class SignupView(APIView):
    http_method_names = ['post', 'get']

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        en = User.objects.create(
            type='NORMAL',
            username=data['username'],
            firstname=data['firstname'],
            lastname=data['lastname'],
            email=data['email'],
            gender=data['gender'],
            mobile_number=data['phone'],
            city=data['city'],
            is_staff=0,
            is_active=1,
            current_status=1,
            password=data['password'],
        )
        en.set_password(data["password"])
        en.save()
        return JsonResponse({'status': 'click recorded'})

    def get(self, request):
        return JsonResponse({'status': 'click recorded'})
    

# Create your views here.
class LoginView(APIView):
    http_method_names = ['post', 'get']

    def post(self, request):
        """
        View for user authentication and login.
        """
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            email = data['email']
            password = data['password']
            user = User.objects.get(email=email)
            if user.check_password(password):
                request.session['user_id'] = user.id
                

                serializer = UserSerializer(user)
                context = {
                    "user":serializer.data
                }
                return JsonResponse(context)
            else:
                return JsonResponse({'error': 'Authentication Failed!'}, status=401)
            
        return JsonResponse({'status': 'click recorded'})

    def get(self, request):
        return Response({'success': True})
