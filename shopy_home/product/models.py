from django.db import models

class accessories(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='pic')
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

