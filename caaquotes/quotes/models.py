import re

from django.db import models

LINE_PREFIX_REGEX = r' ?((?:\[\d{2}:\d{2}(?::\d{2})?\] )?(?:(?:\* )|(?:<\S+> )))'

class Quote(models.Model):
    id = models.IntegerField(primary_key=True)
    quote = models.TextField()
    context = models.CharField(max_length=255)

    def has_regex(self, regex):
        matched = re.search(regex, self.quote)
        return matched is not None

    def has_timestamps(self):
        return self.has_regex(TIMESTAMP_REGEX)

    def has_nicks(self):
        return self.has_regex(NICK_REGEX)

    def lines(self):
        splitted = re.split(LINE_PREFIX_REGEX, self.quote)[1:]
        return map((lambda x,y: x + y), splitted[0::2], splitted[1::2])

    class Meta:
        db_table = 'quotes'
        ordering = ['-id']
