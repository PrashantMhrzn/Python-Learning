from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TodoList
from .serializers import TodoListSerializer
from rest_framework import status
# Create your views here.
@api_view(['GET', 'POST'])
def all_todo(request):
    if request.method == 'GET':
        all_data = TodoList.objects.all()
        serializer = TodoListSerializer(all_data, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # sending JSON data to TodoListSerializer to be converted to obj
        serializer = TodoListSerializer(data = request.data)
        # check validation
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail": "New Todo Created"
        },status.HTTP_201_CREATED)
    
@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def all_detail(request, id):
    if request.method == 'GET':
        single_data = TodoList.objects.get(id = id)
        serializer = TodoListSerializer(single_data)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        single_data = TodoList.objects.get(id = id)
        single_data.delete()
        return Response({
            "detail": "The Post has been deleted."
        })
    elif request.method == 'PUT':
        # load the data from the db same as the api one
        single_data = TodoList.objects.get(id = id)
        # get the instance from the db and replace if items are updated
        serializer = TodoListSerializer(single_data, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail": "Post Updated Successfully!"
        }, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PATCH':
        # load the data from the db same as the api one
        single_data = TodoList.objects.get(id = id)
        # get the instance from the db and replace if items are updated
        # everything is the same as PUT just partial is True
        serializer = TodoListSerializer(single_data, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail": "Post Updated Successfully!"
        }, status=status.HTTP_200_OK)

