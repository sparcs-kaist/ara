from rest_framework import filters


class CategoryFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # filter by url params
        if request.GET.get('category_ids'):
            queryset = queryset.filter(categories__id__in=[int(id) for id in request.GET['category_ids'].split(',') if id])

        # filter by url kwargs
        if view.kwargs.get('category_slugs'):
            queryset = queryset.filter(categories__slug__in=[slug for slug in view.kwargs['category_slugs'].split(',') if slug])

        return queryset
