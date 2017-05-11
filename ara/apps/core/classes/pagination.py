from collections import OrderedDict

from rest_framework import response, pagination


class PageNumberPagination(pagination.PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return response.Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('total', self.page.paginator.num_pages),
            ('next', self.get_next_link()),
            ('prev', self.get_previous_link()),
            ('data', data)
        ]))
