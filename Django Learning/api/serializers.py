from rest_framework import serializers
from .models import TodoList

class TodoListSerializer(serializers.Serializer):
    #  fields to convert to JSON from DB
    title = serializers.CharField()
    description = serializers.CharField()
    is_completed = serializers.BooleanField()

    # to create a data
    def create(self, validated_data):
        return TodoList.objects.create(**validated_data)
    
    # to update data
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance

