import re

from django.db import models

# note that these regexes are pretty basic
TIMESTAMP_REGEX = r'(\[\d{2}:\d{2}(:\d{2})?\] )'
NICK_REGEX = r'(<\S+> )'
ACTION_REGEX = r'( \* \S+)'

def concatenate_list(items, every_n=1):
    ret = []
    last_val = ''
    for i, item in enumerate(items):
        if i and i % every_n == 0:
            ret.append(last_val)
            last_val = ''
        if item:
            last_val = "%s%s" % (last_val, item)
    if len(last_val):
        ret.append(last_val)
    return ret
    

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
        splitted = []
        if self.has_timestamps():
            splitted = re.split(TIMESTAMP_REGEX, self.quote)[1:]
            splitted = concatenate_list(splitted, 3)
        elif self.has_nicks():
            splitted = re.split(NICK_REGEX, self.quote)[1:]
            splitted = concatenate_list(splitted, 2)
        else:
            splitted = [self.quote]

        # split the line if there is an action in it
        split_by_action = []
        for fragment in splitted:
            if re.search(ACTION_REGEX, fragment):
                action_splitted = re.split(ACTION_REGEX, fragment)
                # the first part of the fragment is just line before the action
                split_by_action.append(action_splitted[0])
                split_by_action.extend(concatenate_list(action_splitted[1:], 2))
            else:
                split_by_action.append(fragment)
        splitted = split_by_action

        return splitted

    class Meta:
        db_table = 'quotes'
        ordering = ['-id']
