from rest_framework import serializers
from django.contrib.auth.models import User
from Blog_app.models import Post,Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','is_staff']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['url','title','user','content']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['content','user']