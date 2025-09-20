
from django.urls import path
from users.views import BirthdayListView, BirthdayCreateView


urlpatterns = [
    path('', BirthdayListView.as_view(), name='home'),
    path('add/', BirthdayCreateView.as_view(), name='add_birthday'),
]
