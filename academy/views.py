from .forms import MasterSignUpForm
from .forms import ClientSignUpForm
from .models import Master, Client
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Ticket
from .forms import TicketForm


def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def master_signup(request):
    if request.method == 'POST':
        form = MasterSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            Master.objects.create(
                user=user,
                contact_phone=form.cleaned_data.get('contact_phone'),
                specialization=form.cleaned_data.get('specialization'),
                photo=form.cleaned_data.get('photo')
            )
            login(request, user)
            return redirect('home')
    else:
        form = MasterSignUpForm()
    return render(request, 'user/registrations_master.html', {'form': form})


def client_signup(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(
                user=user,
                contact_phone=form.cleaned_data.get('contact_phone'),
                address=form.cleaned_data.get('address')
            )
            login(request, user)
            return redirect('home')
    else:
        form = ClientSignUpForm()
    return render(request, 'user/registrations_client.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})


def ticket_detail(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})


def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form})


def ticket_update(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/ticket_form.html', {'form': form})
