from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TodoList
from .serializers import TodoListSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

class TodoView(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

# class AllTodo(APIView):

#     def get(self, request):
#         all_data = TodoList.objects.all()
#         serializer = TodoListSerializer(all_data, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = TodoListSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "deatils": "New Todo Created"
#         })


# class DetailTodo(APIView):

#     def get(self, request, id):
#         single_data = TodoList.objects.get(id = id)
#         serializer = TodoListSerializer(single_data)
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         single_data = TodoList.objects.get(id = id)
#         single_data.delete()
#         return Response({
#             "detail": "Your Todo has been Deleted!"
#         })
    
#     def put(self, request, id):
#         single_date = TodoList.objects.get(id = id)
#         serializer = TodoListSerializer(single_date, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "details": "Your Todo has been Updated!"
#         })
    
#     def patch(self, request, id):
#         single_data = TodoList.objects.get(id =id)
#         serializer = TodoListSerializer(single_data, data = request.data, partial = True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "details": "Your Todo list had been Patched!"
#         })
    


