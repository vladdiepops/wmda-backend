from spear.models import Question
from django.http import JsonResponse, Http404
from spear.serializer import SpearSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from django.core import serializers
# import json

@api_view(['GET', 'POST'])
def questionAll(request):
    #invoke serializer and return to client
    if request.method == 'GET':
        data = Question.objects.all()
        serializer = SpearSerializer(data, many=True)
        return Response({'questions': serializer.data})
    
    elif request.method == 'POST':
        serializer = SpearSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'question': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'POST', 'DELETE'])
def questionByID(request, id):
    try:
        data = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = SpearSerializer(data)
        return Response({'questions': serializer.data}, status = status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        serializer = SpearSerializer(data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'question': serializer.data})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    








# def findQuestionByID(index):
#     data = Question.objects.get(id = index)
#     return data

# def findMaxID():
#     data = Question.objects.all()
#     serializer = SpearSerializer(data, many=True)
#     parsedData = JsonResponse({'questions': serializer.data})

#     print(serializer.data[0])
#     print(data.get)
#     print('HERE COMES TREBLE')
#     #print(dir(parsedData.content))

# findMaxID()