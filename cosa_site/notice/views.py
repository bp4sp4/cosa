from django.shortcuts import render
from .models import Nmain


def index(request):
    # nmain = Nmain.objects
    # context = {'nmain':nmain}
    return render(request, '../templates/notice/nmain.html')
