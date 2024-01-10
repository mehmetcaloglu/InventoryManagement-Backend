from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    """
    User login and return JWT token.
    """
    serializer = TokenObtainPairSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except TokenError as e:
        raise InvalidToken(e.args[0])

    return Response(serializer.validated_data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_logout(request):
    """
    User logout.
    """
    if not request.user.is_authenticated:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    user = request.user
    logout(request)

    return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)