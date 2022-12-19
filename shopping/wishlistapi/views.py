from django.shortcuts import render,get_object_or_404
from oscar.core.loading import get_model
from rest_framework import  serializers
from django.db.models import  Q
from .models import WishListItems
from .serializers import WishListItemsTestSerializer,WishAllItemsSerializer
from django.views.generic.edit import CreateView
from rest_framework.generics import CreateAPIView,DestroyAPIView,RetrieveAPIView
WishList = get_model('wishlists', 'WishList')
from rest_framework.permissions import  IsAuthenticated
Line = get_model('wishlists', 'Line')
Product = get_model("catalogue", "Product")
# Create your views here.
from .serializers import WishListSerilizers,LinestSerilizers
from rest_framework import viewsets
class WishViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerilizers


class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LinestSerilizers




class AddtoWishListItemsView(CreateAPIView,DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WishListItems.objects.all()
    serializer_class = WishListItemsTestSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if  user:
            item = get_object_or_404(Product, id=self.kwargs['pk'])
            serializer.save(owner=user, item=item)
        else:                
            raise serializers.ValidationError("This is not a customer account.Please login as customer.")


    def perform_destroy(self, instance):
        instance.delete()




class WishListItemApiViewSet(viewsets.ModelViewSet):
     permission_classes = [IsAuthenticated]
     queryset =WishListItems.objects.all()
     serializer_class=WishAllItemsSerializer

     def get_queryset(self):
         user =self.request.user 
         wishlists = WishListItems.objects.filter(owner=user)
         return wishlists


        

        
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.delete()
        return Response(status=status.HTTP_200_OK)