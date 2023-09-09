from django.urls import path

from big_filter.views import TableListView, init_db


urlpatterns = [
    path('', TableListView.as_view(), name='first'),
]
