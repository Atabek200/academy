from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from .models import Application


def submit_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ApplicationForm()
    return render(request, 'user/application_form.html', {'form': form})


def confirm_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            application.status = 'Confirmed'
        elif 'reject' in request.POST:
            application.status = 'Rejected'
        application.save()
        return redirect('apply')
    return render(request, 'user/confirm_application.html', {'application': application})


def item_list(request):
    return render(request, 'user/item_list.html')


def success(request):
    return render(request, 'user/success.html')
