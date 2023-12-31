from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_data(request):
    serializer = UserSerializer(request.user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({"detail":"not found"}, status=status.HTTP_404_NOT_FOUND)
    
    user.prev_login = user.last_login
    user.last_login = timezone.now()
    user.save()
    
    token, created = Token.objects.get_or_create(user=user)
    #serializer = UserSerializer(instance=user)
    return Response({"token": token.key}) #, "user": serializer.data


from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.username))