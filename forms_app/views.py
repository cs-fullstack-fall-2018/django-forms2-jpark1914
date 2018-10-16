from django.shortcuts import render
from .models import FormModel
from .forms import RestaurantForm
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)


def detail(request, pk):
    post = get_object_or_404(FormModel, pk=pk)
    return render(request, 'forms_app/food_detail.html', {'post': post})

def add(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('detail', pk=post.pk)
    else:
        form = RestaurantForm()

    return render(request, 'forms_app/add.html',{'form':form})



def edit(request, pk):
    post = get_object_or_404(FormModel, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('index')

    else:
        form = RestaurantForm(instance=post)

    return render(request,'forms_app/food_edit.html', {'form':form})

def food(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('form', pk=post.pk)
    else:
        form = RestaurantForm()
    return render(request,'forms_app/foodform.html', {'form': form})