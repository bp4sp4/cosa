from django.urls import path
from . import views

app_name = 'qamain'

urlpatterns = [
    path('', views.index, name="qamain"),
]
