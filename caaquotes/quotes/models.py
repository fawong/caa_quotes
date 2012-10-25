import re

from django.db import models

class Quote(models.Model):
    id = models.IntegerField(primary_key=True)
    quote = models.TextField()
    context = models.CharField(max_length=255)

    def lines(self):
        lines = re.split(r'(<\S+>)', self.quote)
        return ["%s%s" % (x, y) for (x, y) in zip(lines[1::2], lines[2::2])]

    class Meta:
        db_table = 'quotes'
        ordering = ['id']
