from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Item
from django.core.cache import cache


def submit_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplicationForm()
    return render(request, 'user/application_form.html', {'form': form})


def item_list(request):
    return render(request, 'user/item_list.html')


def success(request):
    return render(request, 'user/success.html')
