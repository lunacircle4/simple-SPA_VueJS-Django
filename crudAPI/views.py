from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *  
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json 

def readPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return JsonResponse({'post': model_to_dict(post)})
    
def readPosts(request):
    return JsonResponse({'posts': list(Post.objects.values())})

def createPost(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    #newPostForm = PostForm(request.POST)
    newPost = Post()
    newPost.title = body['title']
    newPost.content = body['content']
        #if newPostForm.is_valid():
    newPost.save()
    return JsonResponse({'result': 'success'})
    #else:
    #    return JsonResponse({'result': 'failed'})

def updatePost(request, pk):
    newPostForm = PostForm(request.POST, instance=get_object_or_404(Post, pk=pk))
    newPostForm.save()

def deletePost(request, pk):
    get_object_or_404(Post, pk=pk).delete()

