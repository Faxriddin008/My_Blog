from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
# ///////


# import uuid
# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# class CustomUser(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     is_teacher = models.BooleanField('teacher status', default=False)
#
#     def __str__(self):
#         return self.username
#
