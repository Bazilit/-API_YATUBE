from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from posts.models import Post, Group
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        queryset = post.comments.all()
        return queryset


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
     def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        
class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        def get_queryset(self):
        queryset = self.request.user.follower.all()
        return queryset
