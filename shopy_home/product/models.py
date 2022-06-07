from django.db import models

class accessories(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='pic')
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class comment(model.Models):
    product=models.ForeignKey(accessories,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    
        

