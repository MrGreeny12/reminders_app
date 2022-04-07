from django.db import models


class PrivateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Create date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last update date")

    default_manager = models.Manager()

    class Meta:
        abstract = True
