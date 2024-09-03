from django.db import models
from django.db.models import *
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.




class Category(Model):
    name = CharField(max_length=100)
    info = TextField()
    slug = SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Book(Model):
    

    name = CharField(max_length=255)
    category = ForeignKey(Category, on_delete=models.CASCADE,related_name='books')
    
    person=models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    author = CharField(max_length=50)
    baza_created = DateField()
    info = TextField()
    rasm = ImageField(upload_to="photo")
    file = FileField(upload_to="files")
    slug = SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
class Comments(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    