from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
#from userprofile.models import User
from django.contrib.auth import get_user_model
from userprofile.serializers import UserSerializer
# Also add these imports
User = get_user_model()
from userprofile.permissions import IsLoggedInUserOrAdmin, IsAdminUser,Isloggin

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    # Add this code block
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == 'create':
            permission_classes =[IsAuthenticated] 
            #[AllowAny,Isloggin]
        elif self.action == 'retrieve':
            permission_classes =[IsAuthenticated] 

        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]