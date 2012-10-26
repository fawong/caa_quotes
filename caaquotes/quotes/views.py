from caaquotes.quotes.models import Quote
from django.views.generic import DetailView, ListView

class ListQuotes(ListView):
    queryset = Quote.objects.all()
    template_name = 'quote_list.html'
    paginate_by = 50

class QuoteDetail(DetailView):
    queryset = Quote.objects.all()
    template_name = 'quote_detail.html'

class QuoteSearch(ListView):
    template_name = 'quote_search_list.html'
    paginate_by = 50

    def get_queryset(self):
        search_query = self.request.GET.get('query', None)
        if not search_query:
            return []

        return Quote.objects.filter(quote__contains=search_query)

    def get_context_data(self, **kwargs):
        context = super(QuoteSearch, self).get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get('query', '')
        return context

