from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=20)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    readcount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}, 작성자:{self.writer}'
    
    def incrementReadCount(self):
        self.readcount +=1
        self.save()


        