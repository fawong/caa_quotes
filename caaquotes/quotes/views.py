from caaquotes.quotes.models import Quote
from django.views.generic import DetailView, ListView

class ListQuotes(ListView):
    queryset = Quote.objects.all()
    template_name = 'quote_list.html'

class QuoteDetail(DetailView):
    queryset = Quote.objects.all()
    template_name = 'quote_detail.html'
