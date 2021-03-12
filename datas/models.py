from django.db import models


# Create your models here.
class History(models.Model):
    id = models.AutoField(primary_key=True)
    term = models.IntegerField(default=0)
    red1 = models.CharField(max_length=20, blank=True)
    red2 = models.CharField(max_length=20, blank=True)
    red3 = models.CharField(max_length=20, blank=True)
    red4 = models.CharField(max_length=20, blank=True)
    red5 = models.CharField(max_length=20, blank=True)
    red6 = models.CharField(max_length=20, blank=True)
    blue = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 't_history'
