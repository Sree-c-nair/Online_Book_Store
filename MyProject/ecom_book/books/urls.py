from django import urls
from django.urls import path
from .views import BookListView

urlpatterns = [
    path('book-list', BookListView.as_view(), name='list')

]
