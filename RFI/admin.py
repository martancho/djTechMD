from django.contrib import admin
from .models import Profile, Contact
from .forms import ContactForm
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ["__str__", "client_name", "client_address"]
	form = ContactForm
	
admin.site.register(Contact)