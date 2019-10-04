from rest_framework.routers import DefaultRouter
from .apiviews import *
from django.urls import path
from .views import fake


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')
router.register('choice', ChoiceViewSet, base_name='choice')
router.register('vote', VoteViewSet, base_name='vote')

urlpatterns = [
   path('fake', fake, name='fake'),
]

urlpatterns += router.urls