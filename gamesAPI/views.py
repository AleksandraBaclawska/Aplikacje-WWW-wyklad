from rest_framework.response import Response
from gamesAPI.serialization import Serializationclass, UserSerializer, PlayerSerializer
from gamesAPI.models import Gamemodel,Player
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import generics



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
	games = Gamemodel.objects.all().order_by('id')
	serializer = Serializationclass(games, many=True)
	return Response(serializer.data)

def playerList(request):
	players = Player.objects.all().order_by('id')
	serializer = Serializationclass(players, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def gameDetail(request, pk):
	games = Gamemodel.objects.get(id=pk)
	serializer = Serializationclass(games, many=False)
	return Response(serializer.data)

def playerDetails(request, pk):
	players = Player.objects.get(id=pk)
	serializer = Serializationclass(players, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def gameAdd(request):
	serializer = Serializationclass(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

def playerAdd(request):
	serializer = PlayerSerializer(data=request.data)

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

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

