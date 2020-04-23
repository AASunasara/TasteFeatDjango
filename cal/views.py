from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import  item, item_preparation_detail, factorylog, note, worker
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

            instance.item_id = item.objects.get(item_id = request.POST['item_id'])
            instance.worker_id = worker.objects.get(worker_id = request.POST['worker_id'])
            instance.save()

            messages.success(request, 'Added Successfully.', extra_tags='home')
            return redirect('home')
        else:
            messages.error(request, 'Not added! Check the details.. ', extra_tags='home')
            return render(request, 'home.html', {'form': form})

    else:
        form = ItemPreForm(request.POST or None)
        return render(request, 'home.html', {'form': form})


@login_required(login_url='login')
def factorylogs(request):
    if request.method == 'POST':
        form = FactoryLogForm(request.POST or None)
        formn = NoteForm(request.POST or None)

        if form.is_valid():
            instancen = formn.save(commit=False)
            instancen.user_id = request.user
            instancen.save()
                        
            instance = form.save(commit=False)
            instance.note_id_id = instancen.note_id
            instance.save()
            messages.success(request, 'Added Successfully.', extra_tags='factorylog')
            return redirect('factorylogs')
        else:
            messages.error(request, "Check your details or Today's details are already added you can go and update it." , extra_tags='factorylog')
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
    items_list = item_preparation_detail.objects.all()
    items_filter = ItemsFilter(request.GET, queryset=items_list)
    rwtotal = items_filter.qs.aggregate(sum=Sum('rweight'))['sum'] 
    iwtotal = 0
    for item in items_filter.qs:
        iwtotal = iwtotal + (item.item_id.offset * item.rweight + item.rweight)  
    itotal = items_filter.qs.count()
    return render(request, 'show.html', {'filter': items_filter, 'rwtotal':rwtotal, 'iwtotal':iwtotal, 'itotal':itotal})

@login_required(login_url='login')
def factorylog_detail(request):
    factorylog_list = factorylog.objects.all()
    factorylog_filter = FactoryLogFilter(request.GET, queryset= factorylog_list)    
    dtotal = factorylog_filter.qs.count()
    return render(request, 'factorylog_detail.html', {'filter': factorylog_filter, 'dtotal':dtotal})

@login_required(login_url='login')
def edit_item(request, id=None):
    if request.method == 'POST':
        instance = get_object_or_404(item_preparation_detail, id=id )
        form = ItemPreForm(request.POST or None , instance = instance )
        if form.is_valid():
            instance = form.save(commit =  False)
            instance.save()
            messages.success(request, "Item's Details are updated!", extra_tags='edit_item')    
            return redirect('show')
        else:
            messages.error(request, 'Not Updated! Check the details.. ', extra_tags='home')
            return render(request, 'home.html', {'form':form})
    else:
        instance = get_object_or_404(item_preparation_detail, id=id )
        form = ItemPreForm(request.POST or None , instance = instance )
        return render(request, 'home.html', {'form':form})

@login_required(login_url='login')
def edit_factorylog(request, id=None):
    if request.method == 'POST':
        instance = get_object_or_404(factorylog, note_id = id )    
        instancen = get_object_or_404(note, note_id = id )
        form = FactoryLogForm(request.POST or None , instance = instance )
        formn = NoteForm(request.POST or None , instance = instancen )
        if form.is_valid():
            instance = form.save(commit =  False)
            instancen = formn.save(commit =  False)
            instance.save()
            instancen.save()
            messages.success(request, "Factorylog's are updated!", extra_tags='edit_factorylog')
            return redirect('factorylog_detail')
        else:    
            messages.error(request, "Can't Update! Check Details. " , extra_tags='factorylog')
            return render(request, 'factorylog.html', {'form':form, 'formn':formn})
    else:    
        instance = get_object_or_404(factorylog, note_id = id )    
        instancen = get_object_or_404(note, note_id = id )
        form = FactoryLogForm(request.POST or None , instance = instance )
        formn = NoteForm(request.POST or None , instance = instancen )
        return render(request, 'factorylog.html', {'form':form, 'formn':formn})

@login_required(login_url='login')
def delete_item(request, list_id):
    item = item_preparation_detail.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Item has been deleted!', extra_tags='show')
    return redirect('show')

@login_required(login_url='login')
def delete_factorylog(request, list_id):
    notee = note.objects.get(pk=list_id)
    notee.delete()
    # dont need to delete object of factorylog because factorylog.note_id is CASCADE for on_delete ;)
    messages.success(request, "Factorylog's details are deleted!", extra_tags='factorylog_detail')
    return redirect('factorylog_detail')