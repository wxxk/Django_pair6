from django.shortcuts import render, redirect
from .models import Store, Comment
from .forms import StoreForm, CommentForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores':stores
    }
    return render(request, 'store/index.html', context)

def create(request):
    if request.method =='POST':
        store_form = StoreForm(request.POST, request.FILES)
        if store_form.is_valid():
            store = store_form.save(commit=False)
            store.user = request.user
            store.save()
            return redirect('store:index')
    else:
        store_form = StoreForm()
    context = {
        'store_form' : store_form
    }
    return render(request, 'store/create.html', context)

def detail(request, pk):
    store = Store.objects.get(pk=pk)
    context = {
        'store':store
    }
    return render(request, "store/detail.html", context)

def update(request, pk):
    store = Store.objects.get(pk=pk)
    if request.method == 'POST':
        store_form = StoreForm(request.POST, request.FILES, instance=store)
        if store_form.is_valid():
            store_form.save()
            return redirect('store:detail', pk)
    else:
        store_form = StoreForm(instance=store)
    context = {
        'store_form':store_form
    }
    return render(request, 'store/update.html', context)

def delete(request, pk):
    store = Store.objects.get(pk=pk)
    store.delete()
    return redirect('store:index')