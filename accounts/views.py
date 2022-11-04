from django.shortcuts import redirect, render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from store.models import Store, Comment

# 회원가입, 회원정보수정
from .forms import CustomUserCreationForm, CustomUserChangeForm

# 로그인, 비밀번호변경
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login

# 로그아웃
from django.contrib.auth import logout as auth_logout

# 좋아요 비동기
from django.http import JsonResponse

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
def index(request):
    return render(request, "accounts/index.html")


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseForbidden()
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect("store:index")
        else:
            form = CustomUserCreationForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("store:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("store:index")


def profile(request, pk):
    profile = get_user_model().objects.get(pk=pk)
    comments = Comment.objects.filter(user=profile)
    store = Store.objects.filter(user=profile)

    q_page = request.GET.get("q")
    user_store = store
    store_data = Paginator(user_store, 5)
    store_page = store_data.get_page(q_page)

    p_page = request.GET.get("p")
    user_comments = comments
    comments_data = Paginator(user_comments, 5)
    comments_page = comments_data.get_page(p_page)

    context = {
        "profile": profile,
        "stores": profile.store_set.all(),
        "comments": profile.comment_set.all(),
        "comments_page": comments_page,
        "store_page": store_page,
    }
    return render(request, "accounts/profile.html", context)


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts:detail")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return render(request, "store/index.html")


def follow(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
            is_followed = False
        else:
            user.followers.add(request.user)
            is_followed = True
        context = {
            "is_followed": is_followed,
            "followers_count": user.followers.count(),
            "followings_count": user.followings.count(),
        }
        return JsonResponse(context)
