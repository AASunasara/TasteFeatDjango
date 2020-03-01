from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import CreateView
from .models import days, items
from .forms import ItemsForm, DaysForm

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
            messages.success(request, 'Added Successfully.', extra_tags='home')
            return redirect('home')
        else:
            messages.success(request, 'Not added! Check the details.. ', extra_tags='home')
            return render(request, 'home.html', {'form': form} )

    else:
        form = ItemsForm(request.POST or None)
        return render(request, 'home.html', {'form': form})

def edit_item(request, id=None):
    instance = get_object_or_404(items, id=id )
    form = ItemsForm(request.POST or None , instance = instance )
    if form.is_valid():
        instance = form.save(commit =  False)
        instance.save()
    return render(request, 'home.html', {'form':form})

@login_required(login_url='login')
def day(request):
    if request.method == 'POST':
        form = DaysForm(request.POST or None)
    
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
            messages.success(request, 'Added Successfully.', extra_tags='day')
            return redirect('day')
        else:
            messages.success(request, "Today's Detail is already added you can go and update it." , extra_tags='day')
            return render(request, 'day.html', {'form': form} )

    else:
        form = DaysForm()
        return render(request, 'day.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been just logged out!', extra_tags='logout')
    return redirect('login')

@login_required(login_url='login')
def show(request):
    all_items = items.objects.filter(user_id=request.user)
    return render(request, 'show.html', {'all_items': all_items})

@login_required(login_url='login')
def todays_detail(request):
    all_items = days.objects.filter(user_id=request.user)
    return render(request, 'todays_detail.html', {'all_items': all_items})

@login_required(login_url='login')
def delete_item(request, list_id):
    item = items.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Item has been deleted!', extra_tags='show')
    return redirect('show')

@login_required(login_url='login')
def delete_day(request, list_id):
    day = days.objects.get(pk=list_id)
    day.delete()
    messages.success(request, 'Day has been deleted!', extra_tags='todays_detail')
    return redirect('todays_detail')

 
"""
class CreateItemView(CreateView):
    model = items
    form_class = ItemsForm
    template_name = '/home/akbarh/projects/django/srvdy/cal/templates/home.html'
    success_url = '/home/akbarh/projects/django/srvdy/cal/templates/home.html'

"""