from django.urls import path
# from .views import PollsList, PollDetail
from .apiviews import *
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()
router.register('polls', PollViewset, basename='polls')



urlpatterns = [
    path('choices/', ChoiceList.as_view(), name='choice_list'),
    path('vote/', CreateVote.as_view(), name='create_vote'),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(),name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name='create_vote'),

    path("users/", CreateUser.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name = 'login'),
]

urlpatterns += router.urls
