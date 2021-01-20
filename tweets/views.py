from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
from tweets.models import Tweet


def list_view(request, *args, **kwargs):
    all_list = Tweet.objects.all();
    tweet_list = [{'id': x.id, 'content': x.content} for x in all_list]
    data = {
        'response': tweet_list
    }
    return JsonResponse(data)


def details_view(request, tweet_id, *args, **kwargs):
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

    return JsonResponse(data, status=status)
