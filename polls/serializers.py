from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from .models import Poll, Choice, Vote


class VoteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'