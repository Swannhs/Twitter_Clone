from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from tweets.models import Tweet


def home(request, *args, **kwargs):
    data = {
        'message': 'Hello word',
    }

    return JsonResponse(data, status=200)
