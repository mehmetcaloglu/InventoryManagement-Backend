from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from uygulama_adi.models import UserProfile
from django.contrib.auth import authenticate  # Gerekirse ekleyin
# user_views.py

@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration(request):
    """
    Register a new user with a role.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role')  # role bilgisini al
    depotname = request.data.get('depotname')   # depotname bilgisini al

    if not username or not password or not role:
        return Response({'error': 'Missing parameters'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    user_profile.role = role
    user_profile.depotname = depotname
    user_profile.save()

    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)



# @api_view(['POST'])
# @permission_classes([AllowAny])
# def user_login(request):
#     """
#     User login and return JWT token.
#     """
#     serializer = TokenObtainPairSerializer(data=request.data)
#     try:
#         serializer.is_valid(raise_exception=True)
#     except TokenError as e:
#         raise InvalidToken(e.args[0])

#     return Response(serializer.validated_data, status=status.HTTP_200_OK)

# user_views.py

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    """
    User login and return JWT token along with role and depotname.
    """
    serializer = TokenObtainPairSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except TokenError as e:
        raise InvalidToken(e.args[0])

    # Kullanıcıyı getir
    user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
    if user is not None:
        # UserProfile bilgilerini getir
        user_profile = UserProfile.objects.get(user=user)
        role = user_profile.role
        depotname = user_profile.depotname.name if user_profile.depotname else None

        # Yanıt verisine ek bilgileri ekle
        response_data = serializer.validated_data
        response_data['role'] = role
        response_data['depotname'] = depotname

        return Response(response_data, status=status.HTTP_200_OK)

    else:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

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