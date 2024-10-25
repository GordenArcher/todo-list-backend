from .models import TodoTable
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoTable
        fields = ['user', 'todo', 'date_created']


class TodoTableUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTable
        fields = ['user']