from haystack import indexes
from .models import Album

class AlbumIndex(indexes.SearchIndex, indexes.Indexable):
   text = indexes.CharField(document=True, use_template=True)
   title = indexes.CharField(model_attr="title")
   description = indexes.CharField(model_attr="description")
   
   def get_model(self):
      return Album

   def index_queryset(self, using=None):
      return self.get_model().objects.filter(
         created__lte=timezone.now()
      )