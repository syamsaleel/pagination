#from rest_framework.response import Response 
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   # def post(self, request,*args,**kwargs):
   #     super().post(request,*args,**kwargs)
   #     return Response({}"message":"Book craeted"},status=200)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
