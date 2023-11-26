from django.contrib import admin
from django.urls import include, path
from polls.views import welcome

urlpatterns = [
    path("", welcome, name = "welcome"),
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
]
