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


class FacebookStatus(models.Model):

    class Meta:
        verbose_name_plural = 'Facebook Statuses'
        ordering = ['publish_timestamp']

    STATUS = (
        ('draft', 'Draft'),
        ('approved', 'Approved'),
    )
    status = models.CharField(max_length=255,
        choices=STATUS, default=STATUS[0][0])
    publish_timestamp = models.DateTimeField(null=True, blank=True)
    publish_date = models.DateField(null=True, blank=True)
    publish_time = models.TimeField()
    author = models.ForeignKey(User, on_delete=None)
    message = models.TextField(max_length=255)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.message

