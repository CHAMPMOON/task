from django.views.generic import ListView
from dotenv import Any

from .models import Data


class DataListView(ListView):
    model = Data
    template_name = 'data/data_list.html'
    context_object_name = 'data'
