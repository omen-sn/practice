from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import *


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'cat__name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    '''def get_queryset(self):
        pk=self.kwargs.get("pk")

        if not pk:
            return Goods.objects.all()[:3]
        else:
            return Goods.objects.filter(pk=pk)'''

    '''@action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})'''

'''class GoodsList(generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
'''
'''
class GoodsAPIList(generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoodsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class GoodsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAdminOrReadOnly,)
'''


'''
class GoodsViewSet(viewsets.ModelViewSet):
    #queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def get_queryset(self):
        pk=self.kwargs.get("pk")

        if not pk:
            return Goods.objects.all()[:3]
        else:
            return Goods.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
'''
'''
class GoodsAPIList(generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

class GoodsAPIUpdate(generics.UpdateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

class GoodsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class GoodsAPIView(APIView):
    def get(self, request):
        w = Goods.objects.all()
        return Response({'posts': GoodsSerializer(w, many=True).data})

    def post(self, request):
        serializer = GoodsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Goods.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = GoodsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        d = Goods.objects.delete(pk=pk)
        d.delete()
        return Response({'post': "delete post" + str(pk)})
'''

"""class GoodsAPIView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer"""