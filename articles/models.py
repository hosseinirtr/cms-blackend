from django.db import models

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=144, )
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"{self.title} at {self.date}"
