from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
from tweets.models import Tweet


def home(request, *args, **kwargs):
    return HttpResponse(f'<h2>hi</h2>')

    # return JsonResponse(data, status=200)


def view(request, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404

    data = {
        'id': tweet_id,
        'content': obj.content
    }
    return JsonResponse(data)
