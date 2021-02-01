from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=250)
    photo = models.URLField(blank=True)

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=250)

    def __str__(self):
        return self.album_title

    class Meta:
        ordering = ['album_title']


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title

    class Meta:
        ordering = ['song_title']
