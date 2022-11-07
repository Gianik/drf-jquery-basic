
from django.views.generic import TemplateView


class ArticleList(TemplateView):
    template_name = 'articles/home.html'


class ArticlePost(TemplateView):
    template_name = 'articles/post_form.html'


class ArticleDetail(TemplateView):
    template_name = 'articles/post_detail.html'


class ArticleDetailUpdate(TemplateView):
    template_name = 'articles/post_update_form.html'


class ArticleDetailDelete(TemplateView):
    template_name = 'articles/post_delete.html'


# class ArticleDetails(APIView):

#     def get_object(self, id):
#         try:
#             return Article.objects.get(id=id)
#         except:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     def put(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return JsonResponse(status=status.HTTP_204_NO_CONTENT)


# class AritcleAPIView(TemplateView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
