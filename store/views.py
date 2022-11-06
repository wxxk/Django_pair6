from django.shortcuts import render, redirect
from .models import Store, Comment
from .forms import StoreForm, CommentForm
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
def index(request):
    stores_buys = Store.objects.filter(buysell=True)
    stores_sells = Store.objects.filter(buysell=False)
    context = {
        "stores_buys": stores_buys,
        "stores_sells": stores_sells,
    }
    return render(request, "store/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        store_form = StoreForm(request.POST, request.FILES)
        if store_form.is_valid():
            store = store_form.save(commit=False)
            store.user = request.user
            store.save()
            return redirect("store:index")
    else:
        store_form = StoreForm()
    context = {
        "store_form": store_form,
    }

    return render(request, "store/form.html", context)


def detail(request, pk):
    store = Store.objects.get(pk=pk)
    comments = store.comment_set.all()
    comment_form = CommentForm()

    context = {
        "store": store,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "store/detail.html", context)


@login_required
def update(request, pk):
    store = Store.objects.get(pk=pk)
    if request.user == store.user:
        if request.method == "POST":
            store_form = StoreForm(request.POST, request.FILES, instance=store)
            if store_form.is_valid():
                store_form.save()
                return redirect("store:detail", pk)
        else:
            store_form = StoreForm(instance=store)
        context = {
            "store_form": store_form,
            "store": store,
        }
        return render(request, "store/form.html", context)
    else:
        return HttpResponseForbidden()


@login_required
def delete(request, pk):
    store = Store.objects.get(pk=pk)
    if request.user == store.user:
        store.delete()
        return redirect("store:index")
    else:
        return HttpResponseForbidden()


@login_required
def comment_create(request, pk):
    store = Store.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.store = store
        comment.user = request.user
        comment.save()
        context = {
            "comment_pk": comment.pk,
            "content": comment.content,
            "userName": comment.user.username,
        }
        return JsonResponse(context)


@login_required
def comment_delete(request, store_pk, comment_pk):
    store = Store.objects.get(pk=store_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        if request.user.pk == comment.user.pk:
            comment.delete()
            return redirect("store:detail", store.pk)
    else:
        return HttpResponseForbidden()


def like(request, pk):
    if request.user.is_authenticated:
        store = Store.objects.get(pk=pk)
        # 좋아요 등록된 상태
        if request.user in store.like_user.all():
            store.like_user.remove(request.user)
            is_liked = False
        # 좋아요 없는 상태
        else:
            store.like_user.add(request.user)
            is_liked = True
        context = {
            "is_like": is_liked,
            "likeCount": store.like_user.count(),
        }
        return JsonResponse(context)
    return redirect("store:detail", pk)


def search(request):
    all_data = Store.objects.all()
    search = request.GET.get("search", "")

    search_list = all_data.filter(
        Q(title__icontains=search)
        | Q(content__icontains=search)
        | Q(type__icontains=search)
    )

    buy_search_list = search_list.filter(buysell=1)
    sell_search_list = search_list.filter(buysell=0)

    context = {
        "search": search,
        "buy_search_list": buy_search_list,
        "sell_search_list": sell_search_list,
        "search_list_len": len(search_list),
    }

    return render(request, "store/search.html", context)
