from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product, Category
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer

from .filters import ProductFilter      # Create your views here.
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def get_all_product(request):
    # products = Product.objects.all()
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    count = filterset.qs.count()
    resPage = 3
    paginator = PageNumberPagination()
    paginator.page_size = resPage
    
    queryset = paginator.paginate_queryset(filterset.qs, request)
    # serializer = ProductSerializer(products, many=True)
    serializer = ProductSerializer(queryset, many=True)
    
    return Response({"products": serializer.data, "per page": resPage, "count": count})


@api_view(['GET'])
def get_by_id_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response({"product": serializer.data})