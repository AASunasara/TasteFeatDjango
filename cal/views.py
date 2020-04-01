from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import item_preparation_detail, factorylog, note, item, worker
from .forms import ItemPreForm, FactoryLogForm, NoteForm
from django.contrib.auth.forms import AuthenticationForm, authenticate
from django.contrib.auth.views import  auth_login
from .filters import ItemsFilter, FactoryLogFilter
import datetime
from django.db.models import Sum, Value
from itertools import chain 
from django.db.models import CharField

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
        form = ItemPreForm(request.POST or None)

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
def factorylogs(request):
    if request.method == 'POST':
        form = FactoryLogForm(request.POST or None)
        formn = NoteForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instancen = formn.save(commit=False)
            instance.user_id = request.user
            instancen.user_id = request.user

            instance.save()
            instancen.save()
            messages.success(request, 'Added Successfully.', extra_tags='factorylog')
            return redirect('factorylogs')
        else:
            messages.success(request, "Check your details or Today's details are already added you can go and update it." , extra_tags='factorylog')
            return render(request, 'factorylog.html', {'form': form, 'formn': formn} )

    else:
        form = FactoryLogForm(request.POST or None)
        formn = NoteForm(request.POST or None)
        return render(request, 'factorylog.html', {'form': form, 'formn': formn})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been just logged out!', extra_tags='logout')
    return redirect('login')

@login_required(login_url='login')    
def show(request):
    items_list = item.objects.all()
    items_filter = ItemsFilter(request.GET, queryset=items_list)
    rwtotal = items_filter.qs.aggregate(sum=Sum('rweight'))['sum'] 
    iwtotal = items_filter.qs.aggregate(sum=Sum('iweight'))['sum'] 
    itotal = items_filter.qs.count()
    return render(request, 'show.html', {'filter': items_filter, 'rwtotal':rwtotal, 'iwtotal':iwtotal, 'itotal':itotal})
import json
import django
@login_required(login_url='login')
def factorylog_detail(request):
    factorylog_list = factorylog.objects.all()
    note_list = note.objects.filter()
    # s = django.core.serializers.serialize('json',request)
    print (django.core.serializers.serialize('json',request))
    for i in note_list:
        print(i.factorylog_id.date)
    # n = note_list[0].factorylog_id
    # print(n.date, n.fact_close_time)
    # factorylog_filter = FactoryLogFilter(request.GET, queryset= note_list[0].factorylog_id)

    # all_items = list(factorylog_filter.qs) + list(note_list)
    
    # dtotal = factorylog_filter.qs.count()
    return render(request, 'factorylog_detail.html', {'filter': note_list, 'dtotal':1})

@login_required(login_url='login')
def edit_item(request, id=None):
    instance = get_object_or_404(items, id=id )
    form = ItemPreForm(request.POST or None , instance = instance )
    if form.is_valid():
        instance = form.save(commit =  False)
        instance.save()
        messages.success(request, "Item's Details are updated!", extra_tags='edit_item')    
        return redirect('show')
    else:
        return render(request, 'home.html', {'form':form})

@login_required(login_url='login')
def edit_factorylog(request, id=None):
    instance = get_object_or_404(factorylog, id=id )
    instancen = get_object_or_404(notes, id=id )
    form = FactoryLogForm(request.POST or None , instance = instance )
    formn = NoteForm(request.POST or None , instance = instancen )
    if form.is_valid():
        instance = form.save(commit =  False)
        instancen = formn.save(commit =  False)
        instance.save()
        instancen.save()
        messages.success(request, "Factorylog's Details are updated!", extra_tags='edit_factorylog')
        return redirect('factorylog_detail')
    else:    
        return render(request, 'factorylog.html', {'form':form, 'formn':formn})

@login_required(login_url='login')
def delete_item(request, list_id):
    item = item.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Item has been deleted!', extra_tags='show')
    return redirect('show')

@login_required(login_url='login')
def delete_factorylog(request, list_id):
    factorylogs = factorylog.objects.get(pk=list_id)
    note = note.objects.get(pk=list_id)
    factorylogs.delete()
    note.delete()
    messages.success(request, "Factorylog's details are deleted!", extra_tags='factorylog_detail')
    return redirect('factorylog_detail')
