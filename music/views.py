from rest_framework import serializers
from .models import Album, Artist, Song
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtistSerializer, AlbumsSerializer, SongsSerializer

# Create your views here.


@api_view(['GET'])
def musicOverview(request):
    music_urls = {
        'List': '/artists-list/'
    }
    return Response(music_urls)


@api_view(['GET'])
def artistsList(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many="True")
    return Response(serializer.data)


@api_view(['GET'])
def getArtist(request, pk):
    artists = Artist.objects.get(id=pk)
    serializer = ArtistSerializer(artists)
    return Response(serializer.data)


@api_view(['POST'])
def addArtist(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateArtist(request, pk):
    artist = Artist.objects.get(id=pk)
    serializer = ArtistSerializer(instance=artist, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteArtist(request, pk):
    artist = Artist.objects.get(id=pk)
    artist.delete()
    return Response("The artist " + artist.artist_name + " deleted successfully")


@api_view(['GET'])
def albumsList(request):
    albums = Album.objects.all()
    serializer = AlbumsSerializer(albums, many="True")
    return Response(serializer.data)


@api_view(['GET'])
def albumsByArtist(request, artistPk):
    album = Album.objects.filter(artist=artistPk)
    serializer = AlbumsSerializer(album, many="True")
    return Response(serializer.data)


@api_view(['POST'])
def addAlbum(request):
    serializer = AlbumsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateAlbum(request, pk):
    album = Album.objects.get(id=pk)
    serializer = AlbumsSerializer(instance=album, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteAlbum(request, pk):
    album = Album.objects.get(id=pk)
    album.delete()
    return Response("The album " + album.album_title + " deleted successfully")


@api_view(['GET'])
def songsList(request):
    songs = Song.objects.all()
    serializer = SongsSerializer(songs, many="True")
    return Response(serializer.data)


@api_view(['GET'])
def songsByAlbum(request, albumPk):
    song = Song.objects.filter(album=albumPk)
    serializer = SongsSerializer(song, many="True")
    return Response(serializer.data)


@api_view(['POST'])
def addSong(request):
    serializer = SongsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateSong(request, pk):
    song = Song.objects.get(id=pk)
    serializer = SongsSerializer(instance=song, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteSong(request, pk):
    song = Song.objects.get(id=pk)
    song.delete()
    return Response("The song " + song.song_title + " deleted successfully")
