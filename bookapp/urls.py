from django.conf.urls import url
from django.urls import path

from .views import Health, BookView, User


app_name = "book"
urlpatterns = [
    path('health', Health.as_view(), name="health"),
    path('testrest', BookView.as_view(), name="book"),
    url(r'^users/$', User.as_view(), name="users"),
    url(r'^users/(?P<pk>.*)/$', User.as_view(), name="user")
]
