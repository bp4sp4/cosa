from django.urls import path
from . import views

app_name = 'cosa'

urlpatterns = [
    path('', views.index, name='cosa'),

]