from rest_framework import serializers
from posts.models import Post, PostImage, Like, Comment
from posts.geo import get_location, reverse_location


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'text', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ['id','post','image']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    images = PostImageSerializer(many=True, read_only=True)

    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False)

    likes_count = serializers.SerializerMethodField()

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'images', 'uploaded_images', 'created_at', 'location',
                'comments', 'likes_count']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        if validated_data.get('location'):
            validated_data['location'] = get_location(validated_data['location'])

        if 'uploaded_images' in validated_data:
            uploaded_images = validated_data.pop('uploaded_images')
            post = Post.objects.create(**validated_data)
            for image in uploaded_images:
                PostImage.objects.create(post=post, image=image)
        else:
            post = Post.objects.create(**validated_data)

        return post

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['location']:
            data['location'] = reverse_location(data['location'])
        return data

    def get_likes_count(self, obj):
        return obj.likes.count()


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        if Like.objects.filter(user=validated_data['user'], post=validated_data['post']).exists():
            raise serializers.ValidationError('You have already liked this post')

        return super().create(validated_data)
