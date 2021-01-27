from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from restgameapi.serialization import Serializationclass
from restgameapi.models import Gamemodel
from rest_framework.decorators import api_view

@api_view(['GET'])
def apihelp(request):
	api_urls = {
		'List':'/gamelist/',
		'Detail View':'/gamedetail/<str:pk>/',
		'Create':'/gameadd/',
		'Update':'/gameupdate/<str:pk>/',
		'Delete':'/gamedelete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def gameList(request):
	games = Gamemodel.objects.all().order_by('-id')
	serializer = Serializationclass(games, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def gameDetail(request, pk):
	games = Gamemodel.objects.get(id=pk)
	serializer = Serializationclass(games, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def gameAdd(request):
	serializer = Serializationclass(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def gameUpdate(request, pk):
	games = Task.objects.get(id=pk)
	serializer = Serializationclass(instance=games, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def gameDelete(request, pk):
	game = Gamemodel.objects.get(id=pk)
	game.delete()

	return Response('Item succsesfully delete!')
