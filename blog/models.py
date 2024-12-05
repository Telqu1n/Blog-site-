from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here
class Tag (models.Model):
    caption = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.caption}"
    
    
    
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()
    
    
class Post (models.Model): #This class is used to create a Post model
    title = models.CharField(max_length=50) # This field is used to store the title of the post
    Excerpts = models.CharField(max_length=200) #This field is used to store a short description of the post
    image_name = models.CharField(max_length=50) #This field is used to store the name of the image file
    date = models.DateField(auto_now=True) #auto_now=True is used to set the current date and time when a Post object is created
    slug = models.SlugField(unique=True,) #unique=True is used to ensure that the slug is unique for each Post object
    content = models.TextField(validators=[MinLengthValidator(10)]) #This field is used to store the content of the post
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts') #This field is used to store the author of the post
    tags = models.ManyToManyField(Tag) #This field is used to store the tags associated with the post  
    
    
    def post_name(self):
        return f"{self.title} by {self.author}"
    
    def __str__(self):
        return self.post_name()