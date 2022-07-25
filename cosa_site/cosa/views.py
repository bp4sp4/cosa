from django.shortcuts import render, get_object_or_404
from .models import Pmain


def index(request):
    pmain = Pmain.objects
    context = {'pmain':pmain}
    return render(request, '../templates/pmain.html', context)

