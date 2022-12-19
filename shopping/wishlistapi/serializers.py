from dataclasses import field
from pyexpat import model
from oscarapi.serializers.product import ProductSerializer
from oscar.core.loading import get_model
from rest_framework import serializers
WishList = get_model('wishlists', 'WishList')
Line = get_model('wishlists', 'Line')
#Product = get_model("catalogue", "Product")
from .models import WishListItems
from userprofile.serializers import UserSerializer



class WishListSerilizers (serializers.ModelSerializer):
    queryset = WishList.objects.all()
    class Meta:
        fields = ('name',)
        model = WishList


class LinestSerilizers (serializers.ModelSerializer):
    queryset = Line.objects.all()
    product = ProductSerializer(required=True)

    class Meta:
        fields =['quantity','product',]
        model = Line


    def create(self, validated_data):
        request  = self.context.get('request')
        product_data = validated_data.pop('product')
        lines = Line(**validated_data)
        profwishlistsile,_=Line.objects.get_or_create(user=request.user, **product_data)
        profwishlistsile.save()
        return lines





class WishListItemsTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItems
        fields = ['id','item']
        depth = 2




class WishAllItemsSerializer(serializers.ModelSerializer):

    owner = UserSerializer(required=True)
    item = ProductSerializer()

    class Meta:
        model = WishListItems
        fields=['id','item','owner']




