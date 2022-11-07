from django.urls import path
from .views import ArticleList, ArticlePost, ArticleDetail, ArticleDetailUpdate, ArticleDetailDelete
from .api import ArticleListView, ArticleDetailView, ArticleDeleteView
urlpatterns = [
    path('', ArticleList.as_view(), name='article-home'),
    path('articles/',
         ArticleListView.as_view({
             'get': 'list',
             'post': 'create',
         })),
    path('post/',
         ArticlePost.as_view(), name='post_articles'),
    path('detail/<int:pk>/',
         ArticleDetail.as_view(), name='post_detail'),
    path('update/<int:pk>/',
         ArticleDetailUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>/',
         ArticleDetailDelete.as_view(), name='post_delete'),
    path('details/<int:pk>/',
         ArticleDetailView.as_view({
             'get': 'retrieve',
             'post': 'update',
         }), name='post_details'),
    path('delete/detail/<int:pk>/',
         ArticleDeleteView.as_view({'post': 'destroy'})),
]
