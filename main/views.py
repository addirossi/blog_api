from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


@api_view()
def posts_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True, context={'request': request})
    return Response(data=serializer.data, status=status.HTTP_200_OK)

#TODO: FBV
#TODO: CBV
#TODO: CRUD
#TODO: Viewsets
#TODO: Pagination
#TODO: Search
#TODO: Filtering
#TODO: Permission
#TODO: Get author from request
