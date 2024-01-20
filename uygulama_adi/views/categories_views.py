from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from uygulama_adi.models import Category
from uygulama_adi.serializers import CategorySerializer
from rest_framework.decorators import api_view, permission_classes
from uygulama_adi.permissions import IsAuthenticated,IsStoreManager, IsCentralOfficeEmployee, IsWarehouseEmployee


# def create_category(request):
#     serializer = CategorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def update_category(request, category):
#     serializer = CategorySerializer(category, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def delete_category(request, category):
#     category.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsStoreManager, IsCentralOfficeEmployee, IsWarehouseEmployee])
def get_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)