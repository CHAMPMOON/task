from django.urls import path
from .views import DataListView

app_name = 'data'

urlpatterns = [
    path('', DataListView.as_view(), name='data-list'),
]
