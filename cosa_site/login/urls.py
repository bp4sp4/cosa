from django.urls import path
from . import views

app_name = 'lmain'

urlpatterns = [
    path('', views.index, name="lmain"),
]
