from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser
from .models import Listing
class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('id', 'title')             


# make sure THAT I IMPORT Listing, Image, Message, Category, ListingCategory QUIT FORGETTING

# class ListingSerializer(serializers.ModelSerializer):
#     seller = serializers.StringRelatedField()
#     images = serializers.StringRelatedField(many=True)
#     categories = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Listing
#         fields = ('id', 'title', 'bio', 'location', 'contact_id', 'is_active', 'seller', 'images', 'categories')


# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ('id', 'img', 'listing')


# class MessageSerializer(serializers.ModelSerializer):
#     sender = serializers.StringRelatedField()
#     recipient = serializers.StringRelatedField()
#     listing = serializers.StringRelatedField()

#     class Meta:
#         model = Message
#         fields = ('id', 'text', 'viewed', 'date_time_sent', 'sender', 'recipient', 'listing')


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name')


# class ListingCategorySerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#     listing = serializers.StringRelatedField()

#     class Meta:
#         model = ListingCategory
#         fields = ('id', 'category', 'listing')


