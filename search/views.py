from django.db.models import Q
from django.views.generic import ListView

from main.models import Contact


class SearchView(ListView):
    model = Contact
    context_object_name = 'contacts'
    paginate_by = 10
    template_name = 'search/index.html'

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()

        q = self.request.GET.get('q')
        if q:
            return queryset.filter(
                Q(title=q))
                 

        return queryset
