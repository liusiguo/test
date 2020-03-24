from django.urls import path
from .views import Health, Book

app_name = "book"
urlpatterns = [
    path('health', Health.as_view(), name="health"),
    path('testrest', Book.as_view(), name="book"),
]
