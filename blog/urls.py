from django.urls import path

urlspattern =[
  path(''),
  path('posts'),
  path ('posts/slug:slug>') # <slug> is a placeholder for the actual slug value/ e.g. posts/my-first-post. 
]

