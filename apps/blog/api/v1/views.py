from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from apps.blog.models import Blog
from .serializers import BlogSerializer

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDestroyAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer