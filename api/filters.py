from rest_framework.filters import SearchFilter


class FullNameFilter(SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_terms = self.get_search_terms(request)
        full_name = ' '.join(str(x) for x in search_terms).rstrip()
        return queryset.filter(full_name=full_name)