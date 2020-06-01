from django.shortcuts import render
from .wineUpdater import add
from datetime import datetime


def index(request):
    if request.method == 'POST':
        add('wine3', 'winery1', datetime.utcnow(), 9.95)

    return render(request, 'mainsite/main.html', {})
