from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('finalResults', views.finalResults, name='finalResults'),
    path('scoreInput', views.scoreInput, name='scoreInput'),
    path('scoreInputReceived', views.scoreInputReceived, name='scoreInputReceived')]