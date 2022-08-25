from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import HttpResponse
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['POST'])
def Login_View():
    return HttpResponse("not valid")