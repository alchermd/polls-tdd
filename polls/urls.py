from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/polls/')),
    path('polls/', views.polls_index),
    path('polls/<int:question_id>/', views.polls_show),
]
