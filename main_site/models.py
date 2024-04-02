from django.db import models

class Excursion(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title

class Image(models.Model):
    excursion = models.ForeignKey(Excursion, related_name='images', on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f"Image for {self.excursion.title}"
