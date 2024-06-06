from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Master)
admin.site.register(Specialization)
admin.site.register(Status)
admin.site.register(Ticket)
