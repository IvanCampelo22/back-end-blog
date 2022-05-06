from email.policy import default
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.


class Post(models.Model):
    STATUS = (
        ('racunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=50)
    text = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    data_creation = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    up_image = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=10, 
                              choices=STATUS, 
                              default="rascunho")
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    class Meta:
        db_table = 'post'
        
    def __str__(self):
        return self.title