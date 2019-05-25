from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserForm(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=None)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=1200)
    uuid_main = models.UUIDField()

    def __str__(self):
        return "{} - {}".format(self.created_by, self.uuid_main)

