from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class ask(models.Model):
    Id = models.AutoField(primary_key=True)  # خودکار تولید شود
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=300)
    caption = models.TextField(max_length=2000, null=False)
    Created = models.DateTimeField()

    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوال ها"

class CommentAsk(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    ask = models.ForeignKey(ask, on_delete=models.CASCADE)
    Id = models.IntegerField(primary_key=True)
    text = models.TextField(max_length=2000, null=False)
    Created = models.DateTimeField()

    class Meta:
        verbose_name = "جواب سوالات"
        verbose_name_plural = "جواب ها"