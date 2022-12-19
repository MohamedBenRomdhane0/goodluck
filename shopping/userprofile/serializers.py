from rest_framework import serializers
from userprofile.models import  UserProfile

from django.contrib.auth import get_user_model
User = get_user_model()
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('title', 'dob', 'address', 'country', 'city', 'zip', 'photo','phone_number','updated_at')

#HyperlinkedModelSerializer
class UserSerializer(serializers.ModelSerializer):
    """
    Bifrost user writable nested serializer
    """
    profile = UserProfileSerializer(required=True)


    class Meta:
        model = User
        #'url',
        fields = ('url','username', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
       # request  = self.context.get('request')
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        # profile=UserProfile.objects.get_or_create(user=request.user, **profile_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()

        profile.title = profile_data.get('title', profile.title)
        profile.dob = profile_data.get('dob', profile.dob)
        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.zip = profile_data.get('zip', profile.zip)
        profile.photo =  profile_data.get('photo', profile.photo)
        #validated_data.get('photo')['file']
        #serializers.ImageField(allow_null=True, use_url=True)
        #profile_data.get('photo', profile.photo)
        profile.save()

        return instance
