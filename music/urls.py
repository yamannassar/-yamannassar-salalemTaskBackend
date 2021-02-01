# from django.urls import path
# from . import views
# from django.urls import path

# urlpatterns = [
#     path('', views.musicOverview, name='music-overview'),
#     path('artists-list/', views.artistsList, name='artists-list'),
#     path('artists-list/<str:pk>', views.getArtist, name='artist-info'),
#     path('add-artist/', views.addArtist, name='artist-create'),
#     path('update-artist/<str:pk>', views.updateArtist, name='artist-update'),
#     path('delete-artist/<str:pk>', views.deleteArtist, name='artist-delete'),
#     path('albums-list/', views.albumsList, name='albums-list'),
#     path('albums-list/<str:artistPk>', views.albumsByArtist, name='albums-by-artist'),
#     path('add-album/', views.addAlbum, name='album-create'),
#     path('update-album/<str:pk>', views.updateAlbum, name='album-update'),
#     path('delete-album/<str:pk>', views.deleteAlbum, name='album-delete'),
#     path('songs-list/', views.songsList, name='albums-list'),
#     path('songs-list/<str:albumPk>', views.songsByAlbum, name='songs-by-album'),
#     path('add-song/', views.addSong, name='song-create'),
#     path('update-song/<str:pk>', views.updateSong, name='song-update'),
#     path('delete-song/<str:pk>', views.deleteSong, name='song-delete'),
# ]

from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from music.schema import albumSchema, artistSchema, songSchema

urlpatterns = [
    path("allArtists", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=artistSchema))),
    path("allAlbums", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=albumSchema))),
    path("allSongs", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=songSchema))),
]
