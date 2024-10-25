from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    todo = models.CharField(max_length=10000, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
