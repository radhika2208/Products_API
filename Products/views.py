from django.shortcuts import render
from .models import Products
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
def Index(request):
    """
    A sample function to render the template as home page.
    """
    return render(request, 'Index.html')

class ProductViewSet(viewsets.ModelViewSet):
    """
    class viewset which defines various CRUD Opeartions
    """
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductSerializer
    def list(self, request, *args, **kwargs):
        """
        list all the products
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        """
        Get a single instance of Product
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """
        Add New Product
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        """
        Update the existing Product
        """
        product = self.get_object()
        serializer = self.get_serializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        """
        delete an instance of Product
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Product successfully Deleted!", status=status.HTTP_200_OK)
    
