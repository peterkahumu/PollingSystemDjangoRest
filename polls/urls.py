from django.urls import path
from .views import PollsList, PollDetail

urlpatterns = [
    path('', PollsList.as_view(), name='polls_list'),
    path('<int:pk>/', PollDetail.as_view(), name='polls_detail')
]