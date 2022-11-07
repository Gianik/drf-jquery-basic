from rest_framework import serializers
from articles.models import Article


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email']


class ArticlePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['title', 'author', 'email']


# serializers.Serializer

# title = serializers.CharField(max_length=100)
# author = serializers.CharField(max_length=100)
# email = serializers.EmailField(max_length=100)
# date_created = serializers.DateTimeField()

# def create(self, validated_data):
#     return Article.objects.create(validated_data)

# def update(self, instance, validated_data):
#     instance.title = validated_data.get('title', instance.title)
#     instance.author = validated_data.get('author', instance.author)
#     instance.email = validated_data.get('email', instance.email)
#     instance.date_created = validated_data.get(
#         'title', instance.date_created)
#     instance.save()

#     return instance
