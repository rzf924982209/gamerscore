from django.urls import path
from gamer_app import views
urlpatterns = [
    path('gamer/',views.Client.as_view()),
    path('client_sort/',views.Client_Sort.as_view())
]