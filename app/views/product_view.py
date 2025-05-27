from rest_framework import generics

from app.models.product import Product, ProductSerializer
from rest_framework import status
from rest_framework.response import Response

from app.renders import CustomAesRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class ProductView(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = [CustomAesRenderer]
    authentication_classes = [BasicAuthentication,TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        pk=kwargs.get('pk')
        if pk:
            try:
                product = Product.objects.get(id=pk)
                serialized_data = ProductSerializer(product)
                return Response(serialized_data.data,status=200)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=404)      
        product_queryset = Product.objects.all()
        serialized_data = ProductSerializer(product_queryset, many=True)
        return Response(serialized_data.data,status=200)
    
    
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        
    def put(self, request, pk, *args, **kwargs):
        pk=kwargs.get('pk')
        product_instance = Product.objects.get(id=pk)
        serialized_data=ProductSerializer(product_instance, data=request.data, partial=True)   
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(serialized_data.data, status=200)
        
    def delete(self, request, pk, *args, **kwargs):
        try:
            pk=kwargs.get('pk')
            proudct_instance=  Product.objects.get(id=pk)
            proudct_instance.delete()
            return Response({'message':"Product Deleted Sucssesfully"}, status=200)
        except:
            return Response({"error": "Product not found"}, status=404)
        
        
        
          
        
        
        
        
        
        
        
        
        
    
    
    