from django.db import models
import uuid

# Create your models here.


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True, # new
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    class Meta:
        indexes = [ # new
                    models.Index(fields=['id'], name='id_index'),
                ]

    def __str__(self):
        return self.title
