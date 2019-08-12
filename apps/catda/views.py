from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, redirect, get_list_or_404, reverse, get_object_or_404
from .models import CatdaSoccerPlayer, CatdaExecutiveTeam,CatdaTeamPosition, CatdaTechnicalTeam
from django.db.models import Count, Q
from apps.posts.models import Author, Post
from apps.posts.views import get_category_count
from .forms import CatdaSoccerPlayersForm,CatdaExecutiveForm, CatdaTechnicalMemberForm


def catda_index(request):
    featuredCatdaSoccerPlayer = CatdaSoccerPlayer.objects.filter(featured=True).order_by('-timestamp')[:3]
    featuredExecutiveMember = CatdaSoccerPlayer.objects.filter(featured=True).order_by('-timestamp')[:3]
    featuredCatdaTechnicalTeam = CatdaTechnicalTeam.objects.filter(featured=True).order_by('-timestamp')[:3]

    context = {
        'obj_player':featuredCatdaSoccerPlayer, 
        'obj_executive':featuredExecutiveMember, 
        'obj_technical':featuredCatdaTechnicalTeam, 
    }
    return render(request,'catda_template/index.html',context)



def catda_about(request):
    context ={
        'about_catda':"catda abouts"
    }

    return render(request,'catda_template/about.html',context)

def catda_contact(request):
    context ={
        'contact_catda':"catda contact"
    }

    return render(request,'catda_template/contact.html',context)





def catda_match(request):
    context ={
        'about_catda':"catda match"
    }

    return render(request,'catda_template/match.html',context)

def catda_team(request):
    catda_player_list = CatdaSoccerPlayer.objects.all()
    context = {
        'catda_player_list':catda_player_list,
        'team_catda':'Catda team'
    }
    
    return render(request,'catda_template/team.html', context)

def catda_news(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'category_count': category_count
    }
    
    return render(request,'catda_template/news.html', context)



def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def search(request):
    queryset = CatdaSoccerPlayer.objects.all()
    query = request.GET.get('spq')
    if query:
        queryset = queryset.filter(
            Q(full_name_icontains=query) |
            Q(team_positions_icontains=query)
        ).distinct()

    context ={
        'queryset':queryset
    }
    return render(request, 'team/search_soccer_players.html', context)

def player_detail(request, id):
    return render(request, 'team/player_detail.html', {})

def technical_member_detail(request, id):
    return render(request, 'team/technical_member_detail.html', {})


def executive_member_detail(request, id):
    return render(request, 'team/executive_member__detail.html', {})


def catda_player_list(request):
    players_list = CatdaSoccerPlayer.objects.all()
   
    context = {
        'players_list':players_list,
    }
    return render(request, 'catda_template/team/players/players_list.html', context)

def catda_player(request, id):
    player = get_object_or_404(CatdaSoccerPlayer, id=id)
    most_recent = CatdaSoccerPlayer.objects.order_by('-timestamp')[:3]
   
    context = {

        'player': player,
        'most_recent': most_recent,
    }
    return render(request, 'catda_template/team/players/player_detail.html', context)

def executive(request, id):
    executive = get_object_or_404(CatdaExecutiveTeam, id=id)
    most_recent = CatdaExecutiveTeam.objects.order_by('-timestamp')[:3]
   
    context = {
        'executive': executive,
        'most_recent': most_recent,
    }
    return render(request, 'team/executive_member.html', context)

def create_executive(request):
    title = 'Create Executive'
    form = CatdaExecutiveForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("executive-detail",kwargs={
                'id': form.instance.id
            }))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "team/executive_create.html", context)

def update_executive(request, id):
    title = 'Update Executive'
    executive = get_object_or_404(CatdaExecutiveTeam, id=id)
    form = CatdaExecutiveForm(
        request.POST or None,
        request.FILES or None, instance=executive)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("executive-detail",kwargs={
                'id': form.instance.id
            }))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "team/executive_create.html", context)

def delete_executive(request, id):
    executive = get_object_or_404(CatdaExecutiveTeam, id=id)
    executive.delete()
    return redirect(reverse("executive-list"))





def technical_team_list(request):
    tech_team_listing = CatdaTechnicalTeam.objects.all()
    
    context = {
        'tech_team_listing': tech_team_listing
    }
    return render(request, 'team/technical_team_list.html', context)

def technical_member(request, id):
    technical_member = get_object_or_404(CatdaTechnicalTeam, id=id)
    most_recent = CatdaTechnicalTeam.objects.order_by('-timestamp')[:3]
   
    context = {
        'technical_member': technical_member,
        'most_recent': most_recent,
    }
    return render(request, 'team/technical_member_detail.html', context)


def create_technical_member(request):
    title = 'Create Technical Member'
    form = CatdaTechnicalMemberForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("technical-member-detail",kwargs={
                'id': form.instance.id
            }))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "team/technical_member_create.html", context)


def update_technical_member(request, id):
    title = 'Update technical'
    technical_member = get_object_or_404(CatdaTechnicalTeam, id=id)
    form = CatdaTechnicalMemberForm(
        request.POST or None,
        request.FILES or None, instance=technical_member)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("technical-member-detail",kwargs={
                'id': form.instance.id
            }))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "team/technical_member_create.html", context)

def delete_technical_member(request, id):
    team_member = get_object_or_404(CatdaTechnicalTeam, id=id)
    team_member.delete()
    return redirect(reverse("technical-member-list"))

def executive_team_list(request):
    executives_listing = CatdaExecutiveTeam.objects.all()
    
    context = {
        'executives_listing': executives_listing
    }
    return render(request, 'team/executive_team_list.html', context)


def create_player(request):
    title = 'Create Player'
    form = SoccerPlayersForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("player-detail",kwargs={
                'id': form.instance.id
            }))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "team/player_create.html", context)



def update_player(request, id):
    title = 'Update'
    player = get_object_or_404(SoccerPlayer, id=id)
    form = SoccerPlayersForm(
        request.POST or None,
        request.FILES or None, instance=player)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author =author
            form.save()
            return redirect (reverse("player-detail",kwargs={
                'id': form.instance.id
            }))

    context = {
        'title':title,
        'form': form
    }

    return render(request, "team/player_create.html", context)


def delete_player(request, id):
    player = get_object_or_404(SoccerPlayer, id=id)
    player.delete()
    return redirect(reverse("player-list"))

def partial_view(request, *args, **kwargs):
    result = kwargs['arg1'] + kwargs['arg2']
    kwargs['result'] = result
    return render(request, 'catda_template/partial_view.html', kwargs)



def partial_footer(request):
    info = "Am a test paragraph"

    context={
        'info':info
    }

    return render(request,'catda_template/partial_footer.html',context)

def prime_partial_footer(request):
    info = "Am a test paragraph"
    most_recent = Post.objects.order_by('-timestamp')[:3]


    context={
        'info':info,
        'most_recent':most_recent
    }

    return render(request,'catda_template/footer.html',context)


def prime_partial_sidebar(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]



    context={
        'most_recent': most_recent,
        'category_count': category_count,

    }

    return render(request,'catda_template/sidebar.html',context)




def prime_partial_news_highlight(request):
    most_recent = Post.objects.order_by('-timestamp')[:3]

    context={
        'most_recent': most_recent,
    }

    return render(request,'catda_template/news-highlight.html',context)


def partial_players(request):
    most_recent_players = CatdaSoccerPlayer.objects.order_by('-timestamp')[:4]
   
    context = {

        'most_recent_players': most_recent_players,
    }
    return render(request, 'catda_template/team/players/featured-players.html', context)


def privacy_policy(request):
    
    return render(request, 'catda_template/privacy-policy.html')



# class PartialView(TemplateView):
#     template_name = 'partial_view.html'

#     def get_context_data(self, **kwargs):
#         result = kwargs['arg1'] + kwargs['arg2']
#         kwargs['result'] = result
#         return super(PartialView, self).get_context_data(**kwargs)

