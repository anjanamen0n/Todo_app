# Create your views here.

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.contrib.auth.models import User
from .serializers import UserSerializer



@api_view(['POST'])
def add_profile(request):
    # Your implementation for add_profile
    return JsonResponse({'message': 'Profile added successfully'})

@api_view(['GET'])
def other_views(request):
    # Your implementation for other_views
    return JsonResponse({'message': 'Other views response'})


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        access_token = jwt.encode({'id':user.id}, 'secret', algorithm='HS256') 
        refresh_token = jwt.encode({'id':user.id}, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'token' : access_token
        }

        return response

class UserView(APIView):
    def get(self, request):
        auth = request.headers.get('Authorization') 
        if not auth:
           raise AuthenticationFailed('Unauthenticated!')

        token = auth.split(" ")[1]
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('refresh_token')
        response.data = {
            'message': 'success'
        }

        return response