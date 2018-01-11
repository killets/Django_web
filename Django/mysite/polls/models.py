from django.db import models
from django.utils import timezone

# Create your models here.

class Msg(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="请输入公告内容")

    def one_week_expire():
        return timezone.now() + timezone.timedelta(days=7)

    expire_date = models.DateTimeField(default=one_week_expire)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

