from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import days, items
from .forms import ItemsForm, DaysForm
from django.contrib.auth.forms import AuthenticationForm, authenticate
from django.contrib.auth.views import  auth_login
from .filters import ItemsFilter, DaysFilter
import datetime
from django.db.models import Sum

def LoginView(request):
    
        if request.user.is_authenticated:
            return redirect('home')
            
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
                        
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('home')
            else:
                messages.error(request,'Username or Password may not correct!.', extra_tags='login')
                return redirect('login')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})


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
            messages.success(request, "Check your details or Today's details are already added you can go and update it." , extra_tags='day')
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
    items_list = items.objects.all()
    items_filter = ItemsFilter(request.GET, queryset=items_list)
    rwtotal = items_filter.qs.aggregate(sum=Sum('rweight'))['sum'] 
    iwtotal = items_filter.qs.aggregate(sum=Sum('iweight'))['sum'] 
    itotal = items_filter.qs.count()
    return render(request, 'show.html', {'filter': items_filter, 'rwtotal':rwtotal, 'iwtotal':iwtotal, 'itotal':itotal})

@login_required(login_url='login')
def todays_detail(request):
    days_list = days.objects.all()
    days_filter = DaysFilter(request.GET, queryset=days_list)
    dtotal = days_filter.qs.count()
    return render(request, 'todays_detail.html', {'filter': days_filter, 'dtotal':dtotal})

@login_required(login_url='login')
def edit_item(request, id=None):
    instance = get_object_or_404(items, id=id )
    form = ItemsForm(request.POST or None , instance = instance )
    if form.is_valid():
        instance = form.save(commit =  False)
        instance.save()
        messages.success(request, "Item's Details are updated!", extra_tags='edit_item')    
        return redirect('show')
    else:
        return render(request, 'home.html', {'form':form})

@login_required(login_url='login')
def edit_day(request, id=None):
    instance = get_object_or_404(days, id=id )
    form = DaysForm(request.POST or None , instance = instance )
    if form.is_valid():
        instance = form.save(commit =  False)
        instance.save()
        messages.success(request, "Days's Details are updated!", extra_tags='edit_day')
        return redirect('todays_detail')
    else:    
        return render(request, 'day.html', {'form':form})

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
    messages.success(request, "Day's details are deleted!", extra_tags='todays_detail')
    return redirect('todays_detail')
