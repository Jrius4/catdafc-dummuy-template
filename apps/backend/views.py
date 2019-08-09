# from django.shortcuts import render
from apps.catda.models import CatdaSoccerPlayer
from apps.catda.forms import CatdaSoccerPlayersForm

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, redirect, get_list_or_404, reverse, get_object_or_404
# from apps.soccerplayers.models import SoccerPlayer, ExecutiveTeam,TeamPosition, TechnicalTeam
from django.db.models import Count, Q
from apps.posts.models import Author
from apps.catda.forms import CatdaSoccerPlayersForm,CatdaExecutiveForm, CatdaTechnicalMemberForm
from apps.catda.views import get_author

# Posts imports
from apps.posts.models import Post, PostView
from apps.posts.forms import  PostFormSample, CommentForm, PostForm


def backend(request):
     
    context = {
        'intro': "backend dashboard"
    }
    return render(request, 'backend/admin/index.html', context)

def player_index(request):

    soccer_player_list = CatdaSoccerPlayer.objects.all()

    context={
        'soccer_player_list':soccer_player_list
    }

    return render(request,'backend/admin/players/index.html', context)



def create_splayer(request):
    title = 'Create Player'
    form = CatdaSoccerPlayersForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("backend-players"))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "backend/admin/players/create.html", context)



def update_splayer(request, id):
    title = 'Update'
    player = get_object_or_404(CatdaSoccerPlayer, id=id)
    form = CatdaSoccerPlayersForm(
        request.POST or None,
        request.FILES or None, instance=player)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("backend-players"))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "backend/admin/players/create.html", context)

def delete_splayer(request, id):
    player = get_object_or_404(CatdaSoccerPlayer, id=id)
    player.delete()
    return redirect(reverse("backend-players"))

# Post Backend


def catda_post_index(request):

    catda_post_list =  Post.objects.all().order_by('-timestamp')

    context={
        'catda_post_list':catda_post_list
    }

    return render(request,'backend/admin/posts/index.html', context)



def catda_post_create(request):
    title='Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("backend-posts"))
    context = {
        'title':title,
        'form': form
    }
    return render(request, "backend/admin/posts/create.html", context)


def catda_post_update(request, id):
    title='Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(
        request.POST or None,
        request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("backend-posts"))
    context = {
        'title':title,
        'form': form
    }
    return render(request, "backend/admin/posts/create.html", context)


def catda_post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("backend-posts"))

def partial_scripts(request, *args, **kwargs):
    kwargs['input']
    
    return render(request, '"backend/inc/script.html', kwargs)

