from django.urls import path
from django.views.generic import RedirectView

from .views import polls_index

urlpatterns = [
    path('', RedirectView.as_view(url='/polls/')),
    path('polls/', polls_index),
]
