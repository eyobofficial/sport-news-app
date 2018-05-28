from django.db import models


class PostManager(models.Manager):

    def published(self, *args, **kwargs):
        return self.get_queryset().filter(status=1)
