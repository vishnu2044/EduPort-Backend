from django.db import models
import uuid

class Qualification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qualification = models.CharField(max_length=255)
    # specialization = models.CharField(max_length=155)

    def __str__(self):
        return self.qualification