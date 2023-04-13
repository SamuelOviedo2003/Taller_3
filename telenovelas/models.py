from django.db import models

# Create your models here.
class Telenovelas(models.Model):
    image=models.ImageField(upload_to='movie/images/',default='')
    title=models.CharField(max_length=100,default='')
    description=models.CharField(max_length=250,default='')

    def __str__(self):
        return self.title