from rest_framework.decorators import api_view
from rest_framework.response import Response
from uygulama_adi.models import Sale
from uygulama_adi.serializers import SaleSerializer
from rest_framework.decorators import api_view, permission_classes
from uygulama_adi.permissions import IsAuthenticated,IsStoreManager, IsCentralOfficeEmployee, IsWarehouseEmployee
from rest_framework.pagination import PageNumberPagination

# @permission_classes([ IsCentralOfficeEmployee])
# @api_view(['GET'])
# def get_sales(request):
#     sales = Sale.objects.all()
#     serializer = SaleSerializer(sales, many=True)
#     return Response(serializer.data)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000


@permission_classes([IsCentralOfficeEmployee, IsStoreManager])
@api_view(['GET'])
def get_sales_by_store(request, store_name, page):
    paginator = StandardResultsSetPagination()

    # Verilen mağaza adına göre satışları filtrele
    sales = Sale.objects.filter(store__name=store_name)

    # Paginator kullanarak sayfalandırma yap
    context = paginator.paginate_queryset(sales, request)
    serializer = SaleSerializer(context, many=True)

    # Verilen sayfa numarasına göre yanıt döndür
    return paginator.get_paginated_response(serializer.data)


@permission_classes([IsCentralOfficeEmployee])
@api_view(['GET'])
def get_sales(request):
    paginator = StandardResultsSetPagination()

    # Tüm satışları al
    sales = Sale.objects.all()

    # Paginator kullanarak sayfalandırma yap
    context = paginator.paginate_queryset(sales, request)
    serializer = SaleSerializer(context, many=True)

    # Yanıtı döndür
    return paginator.get_paginated_response(serializer.data)
