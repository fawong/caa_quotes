from caaquotes.quotes.models import Quote
from django.views.generic import ListView

class ListQuotes(ListView):
    queryset = Quote.objects.all()
    template_name = 'quote_list.html'
