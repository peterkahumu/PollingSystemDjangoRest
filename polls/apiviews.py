from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Poll, Choice
from .serializers import *

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    

class ChoiceList(generics.ListCreateAPIView):

    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id = self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # ensure that users can only create choices for the polls they have created.
        poll = Poll.objects.get(pk = self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You cannot create choices for this poll.")
        return super().post(request, *args, **kwargs)

class CreateVote(APIView):
    serializer_class = VoteSerializer

    def post(self, request, pk, choice_pk):
        voted_by  = request.data['voted_by']
        data = {
            "choice": choice_pk,
            "poll": pk,
            "voted_by": voted_by
        }

        serializer = VoteSerializer(data=data)

        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class PollViewset(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]
    # overide destroy method to only allow users to delete polls they have created.

    def destroy(self, request, *args, **kwargs):
        print("Accessing the first poll", flush=True)
        poll = Poll.objects.get(pk=self.kwargs['pk'])
        
        print(f"Request user: {request.user}, Poll created by: {poll.created_by}", flush=True)


        if not request.user == poll.created_by:
            raise PermissionDenied("You cannot delete this poll.")
        return super().destroy(request, *args, **kwargs)
    

class CreateUser(generics.CreateAPIView):
    # exempt the create user from global authentication settings.(
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                return Response({"token": user.auth_token.key})
            else:
                return Response({"error": "User account is disabled."}, status=status.HTTP_403_FORBIDDEN)
        return Response({"error": "invalid credentials were provided."}, status=status.HTTP_400_BAD_REQUEST)
    
