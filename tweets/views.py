from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
from tweets.models import Tweet


def home(request, *args, **kwargs):
    return HttpResponse(f'<h2>hi</h2>')

    # return JsonResponse(data, status=200)


def view(request, tweet_id, *args, **kwargs):
    data = {
        'id': tweet_id,
    }
    status = 202
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not found'
        status = 404

    return JsonResponse(data,status=status)
