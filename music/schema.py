import graphene
from graphene_django import DjangoObjectType

from .models import Album, Artist, Song


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = '__all__'


class SongType(DjangoObjectType):
    class Meta:
        model = Song
        fields = '__all__'


class ArtistQuery(graphene.ObjectType):
    all_artists = graphene.List(ArtistType)

    def resolve_all_artists(root, info):
        return Artist.objects.all()


class AlbumQuery(graphene.ObjectType):
    all_albums = graphene.List(AlbumType)

    def resolve_all_albums(root, info):
        return Album.objects.all()


class SongQuery(graphene.ObjectType):
    all_songs = graphene.List(SongType)

    def resolve_all_songs(root, info):
        return Song.objects.all()


artistSchema = graphene.Schema(query=ArtistQuery)
albumSchema = graphene.Schema(query=AlbumQuery)
songSchema = graphene.Schema(query=SongQuery)
