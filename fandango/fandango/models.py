from django.db import models

class Theater(models.Model):
    name = models.CharField(max_length=100, default = "Theater")
    address = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=15,decimal_places=4, null=True)
    long = models.DecimalField(max_digits=15,decimal_places=4, null=True)
    theater_id = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=30)

#so i can see the theater names in admin
    def __str__(self):
        return self.name + ' (' + self.theater_id + ')'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    theaters = models.ManyToManyField(Theater)
    poster = models.URLField()
    

#so i can see the movie names in admin
    def __str__(self):
        return self.title + ' (' + str(self.id) + ')'

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, default="")
    time = models.CharField(max_length = 10)

#so i can see the showtimes names in admin
    def __str__(self):
        return self.movie.title + ' / ' + self.theater.name + ' / ' + self.time
