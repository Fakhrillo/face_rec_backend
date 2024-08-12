from django.urls import path
from .views import UserView, UserCheck
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', UserView.as_view()),
    path('identify-person/', UserCheck.as_view()),
]