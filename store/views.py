from django.shortcuts import render, redirect
from .models import Store, Comment
from .forms import StoreForm, CommentForm

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def create(request):
    if request.method =='POST':
        store_form = StoreForm(request.POST, request.FILES)
        if store_form.is_valid():
            store_form.save()
            return redirect('store:index')
    else:
        store_form = StoreForm()
    context = {
        'store_form' : store_form
    }
    return render(request, 'store/create.html', context)