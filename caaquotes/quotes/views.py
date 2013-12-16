from caaquotes.quotes.models import Quote
from django.views.generic import DetailView, ListView
from django.conf import settings
from stemming.lovins import stem

class ListQuotes(ListView):
    queryset = Quote.objects.all()
    template_name = 'quote_list.html'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(ListQuotes, self).get_context_data(**kwargs)
	context["CHANNEL"] = settings.CHANNEL
        return context

class QuoteDetail(DetailView):
    queryset = Quote.objects.all()
    template_name = 'quote_detail.html'

    def get_context_data(self, **kwargs):
        context = super(QuoteDetail, self).get_context_data(**kwargs)
	context["CHANNEL"] = settings.CHANNEL
        return context

class QuoteSearch(ListView):
    template_name = 'quote_search_list.html'
    paginate_by = 50

    def get_queryset(self):
        def safe_stem(word):
            try:
                return stem(word)
            except Exception as e:
                return word

        search_query = self.request.GET.get('query', None)
        if not search_query:
            return []

        stemmed_words = [safe_stem(word) for word in search_query.split(" ")]
        query = Quote.objects.all()
        for word in stemmed_words:
            query = query.filter(quote__icontains=word)
        return query

    def get_context_data(self, **kwargs):
        context = super(QuoteSearch, self).get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get('query', '')
	context["CHANNEL"] = settings.CHANNEL
        return context
