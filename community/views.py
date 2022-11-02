from django.shortcuts import render, redirect
from .models import Community, Comment
from .forms import CommunityForm, CommentForm

# Create your views here.
def index(request):
    communitys = Community.objects.all()
    context = {
        'communitys':communitys
    }
    return render(request, 'community/index.html', context)

def create(request):
    if request.method =='POST':
        community_form = CommunityForm(request.POST, request.FILES)
        if community_form.is_valid():
            community = community_form.save(commit=False)
            community.user = request.user
            community.save()
            return redirect('community:index')
    else:
        community_form = CommunityForm()
    context = {
        'community_form' : community_form,
    }
    return render(request, 'community/create.html', context)

def detail(request, pk):
    community = Community.objects.get(pk=pk)
    comments = community.comment_set.all()
    comment_form = CommentForm()
    context = {
        'community':community,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request, "community/detail.html", context)

def update(request, pk):
    community = Community.objects.get(pk=pk)
    if request.method == 'POST':
        community_form = CommunityForm(request.POST, request.FILES, instance=community)
        if community_form.is_valid():
            community_form.save()
            return redirect('community:detail', pk)
    else:
        community_form = CommunityForm(instance=community)
    context = {
        'community_form':community_form,
    }
    return render(request, 'community/update.html', context)

def delete(request, pk):
    community = Community.objects.get(pk=pk)
    community.delete()
    return redirect('community:index')

def comment_create(request, pk):
    if request.user.is_authenticated:
        community = Community.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.community = community
            comment.user = request.user
            comment.save()

            return redirect('community:detail', pk)

def comment_delete(request, community_pk, comment_pk):
    community = Community.objects.get(pk=community_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.user.pk == comment.user.pk:
        comment.delete()
        return redirect('community:detail', community.pk)
    else:
        return redirect('community:detail', community.pk)

def like(request, pk):
    community = Community.objects.get(pk=pk)
    # 좋아요 등록된 상태
    if request.user in community.like_user.all():
        community.like_user.remove(request.user)
    # 좋아요 없는 상태
    else:
        community.like_user.add(request.user)
    return redirect('community:detail', pk)
