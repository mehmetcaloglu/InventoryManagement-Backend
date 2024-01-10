from django.shortcuts import render

from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from uygulama_adi.models import Stock
from uygulama_adi.serializers import StockSerializer
from rest_framework.decorators import api_view, permission_classes
from uygulama_adi.permissions import IsAuthenticated,IsStoreManager, IsCentralOfficeEmployee, IsWarehouseEmployee

@api_view(['GET'])
@permission_classes([IsStoreManager, IsCentralOfficeEmployee, IsWarehouseEmployee])
def stock_list(request):
    """
    List all stock information.
    """
    if request.method == 'GET':
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsStoreManager, IsCentralOfficeEmployee, IsWarehouseEmployee])
def get_stock_detail(request, depotId):
    """
    Retrieve stock information for a specific depot.
    """
    try:
        stocks = Stock.objects.filter(depot_id=depotId)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StockSerializer(stocks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsStoreManager, IsCentralOfficeEmployee, IsWarehouseEmployee])
def get_stock_product_detail(request, depotId, productId):
    """
    Retrieve stock information for a specific product in a specific depot.
    """
    try:
        stock = Stock.objects.get(depot_id=depotId, product_id=productId)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StockSerializer(stock)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsCentralOfficeEmployee])
def stock_create(request):
    """
    Create a new stock information.
    """
    if request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsCentralOfficeEmployee])
def stock_update(request, id):
    """
    Update a specific stock information.
    """
    try:
        stock = Stock.objects.get(pk=id)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = StockSerializer(stock, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsCentralOfficeEmployee])
def stock_delete(request, id):
    """
    Delete a specific stock information.
    """
    try:
        stock = Stock.objects.get(pk=id)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    stock.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)