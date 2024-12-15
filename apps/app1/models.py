from django.db import models



class Developer(models.Model):
    name = models.CharField(max_length=50)
    
    
class Game(models.Model):
    title = models.CharField(max_length=50)
    developer = models.ForeignKey(Developer, on_delete=models.PROTECT)
    
