from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django_seed import Seed
from random import randint
from .models import *

list_user = User.objects.all()
list_polls = Poll.objects.all()

def get_vot():
    global list_user, list_polls
    u = list_user[randint(0,len(list_user)-1)]
    p = list_polls[randint(0,len(list_polls)-1)]
    c_l = p.choices.all()
    c= c_l[randint(0,len(c_l)-1)]
    return (u,p,c)

def add_vote():
    u,p,c = get_vot()
    seeder = Seed.seeder()
    seeder.add_entity(Vote, 1, {
        'voted_by':u,
        'poll':p,
        'choice':c
    })
    inserted_pks = seeder.execute()

def add_user():
    seeder = Seed.seeder()
    seeder.add_entity(User, 10)

def fake(request):
    # seeder = Seed.seeder()
    # seeder.add_entity(Poll, 1, {
    #     'created_by':get_user()
    # })
    # seeder.add_entity(Choice, 2)
    # seeder.add_entity(Vote, 1, {
    #     'voted_by':get_user()
    # })
    # inserted_pks = seeder.execute()
    for i in range(100000):
        try:
            add_vote()
        except:
            print('error{}'.format(i))
    print("fini")
    return redirect('vote-list')

# Create your views here.
def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)