from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from .models import Post
from .forms import PostForm, PostModelForm
# Create your views here.

def postlist_view(request):
    posts = Post.objects.all()
    context = {
        'post_objects' : posts,
    }
    return render(request, 'index.html', context)

def add_post(request):
    # post_form = PostForm()
    # if request.method == 'POST':
    #     post_form = PostForm(request.POST)
    #     if post_form.is_valid():
    #         Post.objects.create(**post_form.cleaned_data)
    #         return redirect('/')
    post_form = PostModelForm(request.POST or None)
    if post_form.is_valid():
        post_form.save()
        return redirect('/')

    context = {
        'form' : post_form,
    }
    return render(request, 'add_post.html', context)

def get_post(request, postid):
    # try:
    #    obj = Post.objects.get(id=postid)
    # except Post.DoesNotExist:
    #    raise Http404
    obj = get_object_or_404(Post, id=postid)

    context = {
        'post' : obj,
    }
    return render(request, 'get_post.html', context)