from django.urls import path
# from .views import PollsList, PollDetail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote

urlpatterns = [
    path('', PollList.as_view(), name='polls_list'),
    path('<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('choices/', ChoiceList.as_view(), name='choice_list'),
    path('vote/', CreateVote.as_view(), name='create_vote'),
]