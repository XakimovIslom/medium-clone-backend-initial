from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from articles.models import Article
from articles.serializers import ArticleCreateSerializer


class ArticlesView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        article = self.get_object()
        serializer = self.get_serializer(article)
        return Response(serializer.data)
