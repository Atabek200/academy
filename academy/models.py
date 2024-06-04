from django.contrib.auth.models import User
from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    address = models.TextField()
    contact_phone = models.CharField(max_length=13)

    def __str__(self):
        return self.user.username


class Master(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='master')
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    contact_phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='master_photos/', null=True, blank=True)


class Masters(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    master = models.ForeignKey(Master, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
