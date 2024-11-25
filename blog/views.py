from datetime import date
from django.shortcuts import render

posts = [
  {
    "slug": "Hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Jack",
    "date": date(2024, 11, 25),
    "title": "Mountain Hiking",
    "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened...",
    "content": "This is the content of the blog post. I'll write more later."
  }
]


# Create your views here.
def starting_page (request):
  return render (request, 'blog/index.html') # This will render the index.html template

def posts (request):
  return render (request, 'blog/all-posts.html')

def post_detail (request, slug):
  return render (request, 'blog/post-detail.html')