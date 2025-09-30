from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view
from rest_framework import generics
class ProductCRUDAPI(APIView):
    def  post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Data Added Successfulyy","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,product_id=None):
        try:
            if product_id==None:
                products=ProductTable.objects.all()
                serializer=ProductSerializer(products,many=True)
                return Response({"data":serializer.data},status=status.HTTP_200_OK)
            else:
                product=ProductTable.objects.get(id=product_id)
                serializer=ProductSerializer(product)
                return Response({"data":serializer.data},status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,product_id):
        try:
            if product_id:
                product =   ProductTable.objects.get(id=product_id)
                serializer=ProductSerializer(product,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"Data Updated Successfully", "data":serializer.data})
                else:
                    return Response({"message":"Product id must "})
                
        except Exception as e:
            return Response(str(e))
    def delete(self,request,product_id):
        try:
             if product_id:
                product =   ProductTable.objects.get(id=product_id)
                product.delete()
                return Response({"message":"Data Deleted Successfully"})
             else:
                return Response({"message":"Product id must "})

        except Exception as e:
            return Response(str(e))

@api_view(["POST","GET","PUT"])
def ProductCRUD(request,product_id=None):
    if request.method=="POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Data Added Successfulyy","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="GET":
        try:
            if product_id==None:
                products=ProductTable.objects.all()
                serializer=ProductSerializer(products,many=True)
                return Response({"data":serializer.data},status=status.HTTP_200_OK)
            else:
                product=ProductTable.objects.get(id=product_id)
                serializer=ProductSerializer(product)
                return Response({"data":serializer.data},status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)


class ProductAddandGet(generics.ListCreateAPIView):
    queryset=ProductTable.objects.all()
    serializer_class=ProductSerializer

class ProductUpdateandDelete(generics.RetrieveDestroyAPIView):
    queryset=ProductTable.objects.all()
    serializer_class=ProductSerializer