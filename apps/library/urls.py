from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.library.views import (
    category_list, author_list, author_detail, book_list
)

app_name = 'library'

urlpatterns = [
    path('categories/', category_list),
    path('authors/', author_list),
    path('authors/<int:pk>', author_detail),
    path('books/', book_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
