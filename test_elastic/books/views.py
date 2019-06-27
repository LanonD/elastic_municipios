from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet
from .models import Album
from .search_indexes import AlbumIndex

class AlbumSerializer(HaystackSerializer):
    
    class Meta:
      index_classes = [AlbumIndex]
      fields = [
         "text", "title", "description"
      ]

class AlbumSearchView(HaystackViewSet):
    index_models = [Album]
    serializer_class = AlbumSerializer