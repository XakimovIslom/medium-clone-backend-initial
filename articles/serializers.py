from rest_framework import serializers

from articles.models import Article, Topic, Clap
from users.models import CustomUser


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'avatar')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class ClapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clap
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    topics = TopicSerializer(many=True, read_only=True)
    claps = ClapSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            'id', 'author', 'title', 'summary', 'content', 'status', 'thumbnail', 'topics', 'views_count',
            'reads_count', 'created_at', 'updated_at', 'claps',)

    def to_representation(self, instance):
        instance.views_count += 1
        instance.save()
        return super().to_representation(instance)


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            'id', 'author', 'title', 'summary', 'content', 'status', 'thumbnail', 'views_count', 'reads_count',
            'topics', 'created_at',
            'updated_at')


