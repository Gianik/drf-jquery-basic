
from rest_framework import status
from .serializers import ArticleListSerializer, ArticlePostSerializer
from .models import Article
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response

# ArticleViewset Can combine all category viewsets just change the urls.


class ArticleListView(viewsets.ViewSet):

    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    def create(self, request):
        serializer = ArticlePostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleListSerializer(article)
        return JsonResponse(serializer.data, safe=False, status=200)

    def update(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticlePostSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDeleteView(viewsets.ViewSet):

    def destroy(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
