from django.db import models

class Quote(models.Model):
    id = models.IntegerField(primary_key=True)
    quote = models.TextField()
    context = models.CharField(max_length=255)

    class Meta:
        db_table = 'quotes'
        ordering = ['id']
