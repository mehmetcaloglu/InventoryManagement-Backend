from django.shortcuts import render

from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view, permission_classes
from uygulama_adi.permissions import IsAuthenticated,IsStoreManager, IsCentralOfficeEmployee, IsWarehouseEmployee

@api_view(['GET'])
@permission_classes([IsStoreManager, IsCentralOfficeEmployee, IsWarehouseEmployee])
def product_list(request):
    """
    List all products.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_product_detail(request, pk):
    """
    Retrieve a product.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsCentralOfficeEmployee])
def update_product_detail(request, pk):
    """
    Update a product.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsCentralOfficeEmployee])
def delete_product(request, pk):
    """
    Delete a product.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([ IsCentralOfficeEmployee])
def product_create(request):
    """
    Create a new product.
    """
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




