from django.db import models


class PostManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        return super(PostManager, self).get_queryset(*args, **kwargs)

    def b(self, *args, **kwargs):
        return self.filter(breaking=True)