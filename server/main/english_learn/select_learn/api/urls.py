from django.urls import include, path
from rest_framework.routers import DefaultRouter

from select_learn.api import views


urlpatterns = [
    path("words-all/", views.UserWordsAll.as_view()),
    path("add-words/", views.UserSentenceAPIView.as_view()),
]
