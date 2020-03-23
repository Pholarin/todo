from django.db import models
from django.conf import settings


# Create your models here.
class Task(models.Model):
    mytask=models.CharField(max_length=220)
    descr=models.TextField()
    dateCreated=models.DateTimeField(auto_now_add=True)
    mark=models.BooleanField(default=False)
    user= models.ForeignKey(to = settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


    class Meta():
        ordering=('-dateCreated',)
        
    def __str__(self):

        return '{}  {}'.format(self.dateCreated,self.mytask)


