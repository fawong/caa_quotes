import re

from django.db import models

LINE_PREFIX_REGEX = r' ?((?:\[\d{2}:\d{2}(?::\d{2})?\] )?(?:(?:\* )|(?:<\S+> )))'

class Quote(models.Model):
    id = models.IntegerField(primary_key=True)
    quote = models.TextField()
    context = models.CharField(max_length=255)

    def lines(self):
        splitted = re.split(LINE_PREFIX_REGEX, self.quote)
        first = splitted.pop(0)
        next = map((lambda x,y: x + y), splitted[0::2], splitted[1::2])
        return next if not len(first) else [first] + next

    class Meta:
        db_table = 'quotes'
        ordering = ['-id']
