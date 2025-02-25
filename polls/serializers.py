from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = "__all__"

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True,read_only=True, required=False)

    class Meta:
        model = Poll
        fields = "__all__"

# create the user serializers.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {
            'write_only':True
        }} # prevent getting the password in api responses.

        def create(self, validated_data):
            try:
                user = User(
                email = validated_data['email'],
                username = validated_data['username']
                )
                user.set_password(validated_data['password']) # ensure the password is hashed correctly.

                user.save()
                Token.objects.create(user=user)
                return user
            except Exception as e:
                raise serializers.ValidationError({"error": str(e)})
            
            