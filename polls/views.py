from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View

from .models import *
# Create your views here.
# I am going to use class based views for this project.

class PollsList(View):
    def get(self, request):
       MAX_OBJECTS = 20
       polls = Poll.objects.all()[:MAX_OBJECTS]
       data = {
           "results": list(polls.values('question', 'created_by__username', 'pub_date'))
       }

       return JsonResponse(data)

class PollDetail(View):
    def get(self, reqeust, pk):
        poll = get_object_or_404(Poll,pk = pk)
        data = {
            "results": {
                "question": poll.question,
                "created_by": poll.created_by.username,
                "pub_date": poll.pub_date
            } 
        }

        return JsonResponse(data)

