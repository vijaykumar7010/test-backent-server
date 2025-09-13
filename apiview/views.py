from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apiview.serializers import NewProductsserializer
from .models import NewProducts
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("App is Running!")

class CreatApiView(APIView):
    def post(self,request):
        serializer = NewProductsserializer(data=request.data)
        print(serializer,"sssssssssssssssssssssssssssssssss")
        if serializer.is_valid():
         serializer.save()
         return Response({"success":"Data created Successfully","data":serializer.data})
        else:
            return Response({"error":serializer.errors})
    def get(self,request,product_id):
        product = NewProducts.objects.get(id=product_id)
        serializer = NewProductsserializer(product)
        return Response(serializer.data,status=status.HTTP_201_CREATED)