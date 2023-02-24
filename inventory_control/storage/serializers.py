from rest_framework import serializers
from .models import *

class GoodsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Goods
        fields = ("title", "content", "photo", "cat", "user")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")
