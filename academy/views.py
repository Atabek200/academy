from .forms import MasterSignUpForm
from .forms import ClientSignUpForm
from .models import Master, Client
from .models import Ticket
from .forms import TicketForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate


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


def ticket_list(request):
    tickets = Ticket.objects.all().filter(client=request.user.client_profile)
    return render(request, 'user/ticket_list.html', {'tickets': tickets})


def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk, client=request.user.client_profile)
    return render(request, 'user/ticket_detail.html', {'ticket': ticket})


def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)  # Создаем объект, но не сохраняем его в базу данных пока.
            ticket.client = request.user.client_profile  # Устанавливаем клиента из текущего пользователя.
            ticket.save()  # Теперь сохраняем объект в базу данных.
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'user/ticket_form.html', {'form': form})


def ticket_update(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'user/ticket_form.html', {'form': form})


def ticket_list(request):
    tickets = Ticket.objects.all().filter(master=request.user.master_profile)
    return render(request, 'user/ticket_list.html', {'tickets': tickets})


def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk, master=request.user.master_profile)
    return render(request, 'user/ticket_detail.html', {'ticket': ticket})


def ticket_update(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'user/ticket_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if hasattr(user, 'master_profile'):
                return redirect('master_page')
            elif hasattr(user, 'client_profile'):
                return redirect('client_page')
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})