from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class MenuItemSearchView(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    pagination_class = MenuItemPagination

def get_queryset(self):
    query = self.request.query_params.get('q', '')
    return MenuItem.objects.filter(name__icontains=query).order_by('name')