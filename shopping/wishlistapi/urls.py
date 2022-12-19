from django.conf.urls import url, include
from rest_framework import routers
from .views import WishViewSet,LineViewSet
from django.urls import  path
from .views import AddtoWishListItemsView,WishListItemApiViewSet,Logout
router = routers.DefaultRouter()
router.register(r'wishlists', WishViewSet)
router.register(r'linelist',LineViewSet)
router.register(r'list',WishListItemApiViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
  #  url(r'^auth/', include('rest_auth.urls')),
   path('addwishlistitems/<int:pk>', AddtoWishListItemsView.as_view(),name='add-to-wishlist'),
       path('logout/', Logout.as_view(),name='logout'),
]