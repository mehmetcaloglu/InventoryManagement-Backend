# add supplier , get suplier, delete suplier

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from uygulama_adi.models import Supplier  # Supplier modelini ekleyin
from uygulama_adi.serializers import SupplierSerializer  # Supplier modeli için bir serializer ekleyin

@api_view(['GET'])
def get_suppliers(request):
    suppliers = Supplier.objects.all()
    serializer = SupplierSerializer(suppliers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_supplier(request):
    serializer = SupplierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
