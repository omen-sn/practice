import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *

class GoodsSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Goods
        fields = ("title", "content", "photo", "cat", "user")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")



'''
class GoodsModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content
'''
'''
class GoodsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Goods.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance
'''
'''
def encode():
    model = GoodsModel('melnyk oleh', 'Content: melnyk oleh')
    model_sr = GoodsSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"title":"melnyk oleh", "content":"Content: melnyk oleh"}')
    data = JSONParser().parse(stream)
    serialiser = GoodsSerializer(data = data)
    serialiser.is_valid()
    print(serialiser.validated_data)
'''