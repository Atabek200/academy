from .forms import MasterSignUpForm
from .forms import ClientSignUpForm
from .models import Master, Client
from .models import Ticket
from .forms import TicketForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, ClientRegisterForm, MasterRegisterForm


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
    tickets = Ticket.objects.all()
    return render(request, 'user/ticket_list.html', {'tickets': tickets})


def ticket_detail(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    return render(request, 'user/ticket_detail.html', {'ticket': ticket})


def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
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


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        client_form = ClientRegisterForm(request.POST)
        master_form = MasterRegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and (client_form.is_valid() or master_form.is_valid()):
            user = user_form.save()
            if 'client' in request.POST:
                client = client_form.save(commit=False)
                client.user = user
                client.save()
            elif 'master' in request.POST:
                master = master_form.save(commit=False)
                master.user = user
                master.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        client_form = ClientRegisterForm()
        master_form = MasterRegisterForm()
    return render(request, 'register.html', {'user_form': user_form, 'client_form': client_form, 'master_form': master_form})


def login_view(request):
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
    return render(request, 'login.html', {'form': form})
